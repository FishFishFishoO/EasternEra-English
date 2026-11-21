"""Write the new English into a copy of the game's English Game.locres (format version 3).

Usage: python -I build_locres.py <base en Game.locres> <units.json> <translations.json> <out Game.locres> [<translate folder>]

Every namespace, key, key hash and source-string hash is copied from the base file, so the game
matches the entries exactly as before; only the English text changes. Keys with no new line
(trait text, which the Traits mod owns, and anything not exported) keep the game's own English.

With <translate folder>: also ADDS entries for text that has a namespace + key in the game assets
(FText, string tables) but no line in the game's locres. Key hash = CityHash64 (ue_hash.py), source
hash = Unreal's StrCrc32; both checked against the base file before anything is added.
Culture-invariant text has no key and can't go in here (the Lua mod handles it).
"""
import json, os, struct, sys, collections, zlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ue_hash import text_hash

BASE, UNITS, TRANS, OUT = sys.argv[1:5]
ARGS = [a for a in sys.argv[5:] if not a.startswith("--")]
ASSETS = ARGS[0] if ARGS else None
# --overrides=row_overrides.json: its "locres_key_overrides" {"Namespace/Key": text} win over the units
OVERRIDES = next((a.split("=", 1)[1] for a in sys.argv[5:] if a.startswith("--overrides=")), None)


def src_hash(s):
    """FCrc::StrCrc32 over TCHARs: every UTF-16 unit fed as 4 little-endian bytes."""
    u = s.encode("utf-16-le")
    return zlib.crc32(b"".join(u[i:i + 2] + b"\0\0" for i in range(0, len(u), 2))) & 0xFFFFFFFF
MAGIC = bytes.fromhex("0e147475674a03fc4a15909dc3377f1b")


class R:
    def __init__(self, b):
        self.b, self.p = b, 0

    def take(self, n):
        v = self.b[self.p:self.p + n]; self.p += n; return v

    def i32(self): return struct.unpack("<i", self.take(4))[0]
    def u32(self): return struct.unpack("<I", self.take(4))[0]
    def i64(self): return struct.unpack("<q", self.take(8))[0]

    def fstr(self):
        n = self.i32()
        if n == 0:
            return ""
        if n > 0:
            return self.take(n)[:-1].decode("latin-1")
        return self.take(-n * 2)[:-2].decode("utf-16-le")


def wstr(s):
    # the game's own file writes "" as a 1-char string holding only the terminator; keep that
    if all(ord(c) < 128 for c in s):
        d = s.encode("ascii") + b"\0"
        return struct.pack("<i", len(d)) + d
    d = s.encode("utf-16-le") + b"\0\0"
    return struct.pack("<i", -(len(d) // 2)) + d


b = open(BASE, "rb").read()
r = R(b)
assert r.take(16) == MAGIC and r.take(1)[0] == 3, "not a version 3 locres"
str_off = r.i64()
entries = r.u32()
# localized strings first
save = r.p; r.p = str_off
strings = []
for _ in range(r.i32()):
    s = r.fstr(); r.i32()  # ref count, rebuilt on write
    strings.append(s)
r.p = save
names = []  # [(ns_hash, ns, [(key_hash, key, src_hash, text)])]
for _ in range(r.u32()):
    nh, ns = r.u32(), r.fstr()
    keys = []
    for _ in range(r.u32()):
        kh, k = r.u32(), r.fstr()
        sh, idx = r.u32(), r.i32()
        keys.append([kh, k, sh, strings[idx]])
    names.append((nh, ns, keys))
assert sum(len(k) for _, _, k in names) == entries
assert all(text_hash(k[1]) == k[0] for _, _, keys in names for k in keys), "key hash check failed"

units = json.load(open(UNITS, encoding="utf-8"))
trans = json.load(open(TRANS, encoding="utf-8"))
new = {}
for i, u in units.items():
    if i in trans:
        for ns, k in u["keys"]:
            new[(ns, k)] = trans[i]

key_over = {}
if OVERRIDES:
    for nk, text in json.load(open(OVERRIDES, encoding="utf-8")).get("locres_key_overrides", {}).items():
        ns, k = nk.split("/", 1)
        key_over[(ns, k)] = text
new.update(key_over)

added = 0
if ASSETS:
    have = {(ns, e[1]) for _, ns, keys in names for e in keys}
    by_zh = {u["zh"]: i for i, u in units.items()}
    found = {}  # (ns, key) -> source

    def walk(o):
        if isinstance(o, dict):
            if "Key" in o and "SourceString" in o and "TableId" not in o and isinstance(o.get("Key"), str):
                found.setdefault((o.get("Namespace") or "", o["Key"]), o["SourceString"])
            st = o.get("StringTable")
            if isinstance(st, dict) and isinstance(st.get("KeysToEntries"), dict):
                for k, v in st["KeysToEntries"].items():
                    found.setdefault((st.get("TableNamespace") or "", k), v)
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    for root, dirs, files in os.walk(ASSETS):
        dirs[:] = [d for d in dirs if d not in ("Localization", "OpenNovel", "DeepL")]
        for f in files:
            if f.endswith(".json"):
                try:
                    walk(json.load(open(os.path.join(root, f), encoding="utf-8")))
                except (ValueError, UnicodeDecodeError):
                    pass
    nsidx = {ns: n for n, (_, ns, _) in enumerate(names)}
    for (ns, k), src in sorted(found.items()):
        if (ns, k) in have or src not in by_zh or by_zh[src] not in trans:
            continue
        text = key_over.get((ns, k), trans[by_zh[src]])
        if ns not in nsidx:
            nsidx[ns] = len(names)
            names.append((text_hash(ns), ns, []))
        names[nsidx[ns]][2].append([text_hash(k), k, src_hash(src), text])
        added += 1
    entries += added
changed = same = 0
for _, ns, keys in names:
    for e in keys:
        t = new.get((ns, e[1]))
        if t is None:
            continue
        if t == e[3]:
            same += 1
        else:
            e[3] = t; changed += 1

# write: header, namespaces, then the string table
idx, table, refs = {}, [], collections.Counter()
for _, _, keys in names:
    for e in keys:
        if e[3] not in idx:
            idx[e[3]] = len(table); table.append(e[3])
        refs[e[3]] += 1
body = bytearray()
body += struct.pack("<I", len(names))
for nh, ns, keys in names:
    body += struct.pack("<I", nh) + wstr(ns) + struct.pack("<I", len(keys))
    for kh, k, sh, t in keys:
        body += struct.pack("<I", kh) + wstr(k) + struct.pack("<Ii", sh, idx[t])
head_len = 16 + 1 + 8 + 4
out = bytearray(MAGIC) + bytes([3]) + struct.pack("<q", head_len + len(body)) + struct.pack("<I", entries) + body
out += struct.pack("<i", len(table))
for t in table:
    out += wstr(t) + struct.pack("<i", refs[t])
open(OUT, "wb").write(out)
print(f"{entries} entries; {changed} now use the new English, {same} were already the same, "
      f"{added} added for keyed text the game's file was missing; {len(table)} unique strings -> {OUT}")
