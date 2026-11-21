"""Build the Lua half of the English translation: every culture-invariant text in the game assets
(data tables, data assets, UI screen templates) that Game.locres can't reach.

Usage: python -I build_lua_text.py <translate folder> <units.json> <translations.json> <template Main.lua> <out Main.lua>
                                    [--overrides=row_overrides.json] [--wrap]

--overrides: per-row text from row_overrides.json, written on top of whatever the row has (locres text
  included). Field paths are dotted: "TechDesc", "FormatItemTechDesc.TextMain", and
  "FormatDescribe.TextParams.<Key>" for the TextParams entry with that Key.
--wrap: every text widget on a UI screen (Blueprints/UI) gets AutoWrapText, so long English goes onto
  the next line instead of being cut off.

Scans the FModel JSONs for CultureInvariantString, matches the Chinese to a translated line, and
writes one instruction per spot into the DATA block of the template:
  data tables  -> {table path, C++ row struct, {row = {{path, text}, ...}}}
  other objects (data assets, widget templates, blueprint defaults) -> {object path, {{path, text}, ...}}
A path is a list of steps: "Field", a 0-based array index (number), or {k = map key}.
Left out: developer notes (Comment), GOAP goal labels, rows of Blueprint-made structs (Lua can't
build those), and plain FString designer placeholders.
"""
import json, os, re, sys, collections

ROOT, UNITS, TRANS, TEMPLATE, OUT = sys.argv[1:6]
OPTS = sys.argv[6:]
OVERRIDES = next((o.split("=", 1)[1] for o in OPTS if o.startswith("--overrides=")), None)
# Culture-invariant text that is only a Chinese separator: plain ASCII (the user: no special characters).
PUNCT = {"、": ", ", "：": ": ", "，": ", ", "；": "; "}
WRAP = "--wrap" in OPTS
TEXT_WIDGETS = {"TextBlock", "CommonTextBlock", "RichTextBlock", "CommonRichTextBlock", "W_ERWTextBlock_C"}
units = json.load(open(UNITS, encoding="utf-8"))
trans = json.load(open(TRANS, encoding="utf-8"))
by_zh = {u["zh"]: i for i, u in units.items() if i in trans}
# LanguageMapping = the language picker; each language keeps its own name there
SKIP_FIELD = re.compile(r"^(Comment|GoalText_\d+_[0-9A-F]{32}|LanguageMapping)$")


def lua(s):
    if isinstance(s, bool):
        return "true" if s else "false"
    if isinstance(s, (int, float)):
        return str(s)
    out = ['"']
    for ch in s:
        o = ord(ch)
        if ch == "\\": out.append("\\\\")
        elif ch == '"': out.append('\\"')
        elif ch == "\n": out.append("\\n")
        elif ch == "\r": out.append("\\r")
        elif ch == "\t": out.append("\\t")
        elif o < 32: out.append("\\%03d" % o)
        else: out.append(ch)
    out.append('"')
    return "".join(out)


def is_map(lst):
    return isinstance(lst, list) and lst and all(isinstance(x, dict) and set(x) == {"Key", "Value"} for x in lst)


def steps(node, path):
    """JSON path (below the object/row) -> Lua steps, or None if it can't be expressed."""
    out, cur, i = [], node, 0
    while i < len(path):
        p = path[i]
        if isinstance(p, int):
            if is_map(cur):
                key = cur[p]["Key"]
                if isinstance(key, (dict, list)):
                    return None
                if isinstance(key, str) and re.fullmatch(r"-?\d+", key):
                    key = int(key)
                if isinstance(key, str) and "::" in key:
                    return None  # enum keys: not needed so far
                out.append({"k": key})
                cur = cur[p]["Value"]
                i += 1
                if i < len(path) and path[i] == "Value":
                    i += 1
                continue
            out.append(p)
            cur = cur[p]
        else:
            if SKIP_FIELD.match(p):
                return None
            out.append(p)
            cur = cur[p]
        i += 1
    return out


def lua_steps(st):
    parts = []
    for s in st:
        if isinstance(s, dict):
            parts.append("{k=%s}" % lua(s["k"]))
        else:
            parts.append(lua(s))
    return "{" + ",".join(parts) + "}"


tables = collections.OrderedDict()   # path -> {struct, name, rows: {row: [(steps, text)]}}
objects = collections.OrderedDict()  # path -> [(steps, text)]
wrap = collections.OrderedDict()     # text widget template path -> True
skipped = collections.Counter()
skipped_where = collections.Counter()  # table: field path of each left-out spot (for --report)
seen = set()


def obj_path(exports, idx, pkg):
    names, n = [], idx
    while True:
        e = exports[n]
        names.append(e["Name"])
        o = e.get("Outer")
        if not isinstance(o, dict):
            break
        m = re.search(r"\.(\d+)$", o.get("ObjectPath", ""))
        if not m:
            return None
        n = int(m.group(1))
    names.reverse()
    return pkg + "." + names[0] + ("" if len(names) == 1 else ":" + ".".join(names[1:]))


def walk(o, path, found):
    if isinstance(o, dict):
        if "CultureInvariantString" in o:
            found.append((path, o["CultureInvariantString"]))
        for k, v in o.items():
            walk(v, path + [k], found)
    elif isinstance(o, list):
        for n, v in enumerate(o):
            walk(v, path + [n], found)


for root, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in ("Localization", "OpenNovel", "DeepL")]
    for fn in sorted(files):
        if not fn.endswith(".json"):
            continue
        full = os.path.join(root, fn)
        rel = os.path.relpath(full, ROOT).replace("\\", "/")[:-5]
        try:
            exports = json.load(open(full, encoding="utf-8"))
        except ValueError:
            continue
        if not isinstance(exports, list):
            continue
        pkg = "/Game/" + rel
        if WRAP and rel.startswith("Blueprints/UI/"):
            # every text box on a UI screen, whatever its text: most UI text now comes from the locres,
            # and runtime text (names, numbers) gets cut off just as easily
            for n, x in enumerate(exports):
                if x.get("Type") in TEXT_WIDGETS and not x.get("Properties", {}).get("AutoWrapText"):
                    op = obj_path(exports, n, pkg)
                    if op and ":WidgetTree." in op:
                        wrap[op] = True
        found = []
        walk(exports, [], found)
        for path, zh in found:
            if zh in by_zh:
                en = trans[by_zh[zh]]
            elif zh in PUNCT:
                en = PUNCT[zh]  # a lone Chinese separator (、 between skill tags, ： after labels)
            else:
                continue
            idx = path[0]
            e = exports[idx]
            if e.get("Type") == "DataTable" and len(path) > 3 and path[1] == "Rows":
                rs = (e.get("Properties", {}).get("RowStruct") or {}).get("ObjectName", "")
                m = re.match(r"ScriptStruct'(\w+)'", rs)
                row = path[2]
                st = steps(e["Rows"][row], path[3:])
                if st is None:
                    skipped["note/label/enum key"] += 1
                    skipped_where[e["Name"] + ": " + "/".join(str(p) for p in path[3:] if not isinstance(p, int))] += 1
                    continue
                if not m:
                    skipped["Blueprint struct row: " + e["Name"]] += 1; continue
                tp = pkg + "." + e["Name"]
                key = (tp, row, json.dumps(st))
                if key in seen: continue
                seen.add(key)
                t = tables.setdefault(tp, {"struct": "F" + m.group(1), "name": e["Name"], "rows": collections.OrderedDict()})
                t["rows"].setdefault(row, []).append((st, en))
            elif len(path) > 2 and path[1] == "Properties":
                op = obj_path(exports, idx, pkg)
                st = steps(e["Properties"], path[2:])
                if op is None or st is None:
                    skipped["object path/enum key"] += 1; continue
                key = (op, json.dumps(st))
                if key in seen: continue
                seen.add(key)
                objects.setdefault(op, []).append((st, en))
                if e.get("Type") in TEXT_WIDGETS and ":WidgetTree." in op and not e["Properties"].get("AutoWrapText"):
                    wrap[op] = True
            else:
                skipped["other place: " + str(e.get("Type"))] += 1

n_over = 0
if OVERRIDES:
    ov = json.load(open(OVERRIDES, encoding="utf-8"))
    for rel, rows in ov.items():
        if not rel.endswith(".json") or not isinstance(rows, dict):
            continue
        exports = json.load(open(os.path.join(ROOT, rel), encoding="utf-8"))
        e = next(x for x in exports if x.get("Type") == "DataTable")
        m = re.match(r"ScriptStruct'(\w+)'", (e.get("Properties", {}).get("RowStruct") or {}).get("ObjectName", ""))
        assert m, "no C++ row struct for " + rel
        tp = "/Game/" + rel[:-5] + "." + e["Name"]
        t = tables.setdefault(tp, {"struct": "F" + m.group(1), "name": e["Name"], "rows": collections.OrderedDict()})
        for row, fields in rows.items():
            assert row in e["Rows"], "row %s not in %s" % (row, rel)
            for field, text in fields.items():
                path, cur = [], e["Rows"][row]
                for part in field.split("."):
                    if is_map(cur):
                        idx = next(i for i, x in enumerate(cur) if x["Key"] == part)
                        path += [idx, "Value"]; cur = cur[idx]["Value"]
                    elif isinstance(cur, list):  # "Name.5" = item 5 of an array field
                        path.append(int(part)); cur = cur[int(part)]
                    else:
                        path.append(part); cur = cur[part]
                assert isinstance(cur, dict) and ("SourceString" in cur or "CultureInvariantString" in cur),                     "%s/%s/%s is not a text field" % (rel, row, field)
                st = steps(e["Rows"][row], path)
                sets = t["rows"].setdefault(row, [])
                sets[:] = [x for x in sets if json.dumps(x[0]) != json.dumps(st)]  # the override wins
                sets.append((st, text))
                n_over += 1
    # "objects": {"Configs/X.json": {"Field.0.Sub": text}}: text on a single asset (not a table row),
    # for when the same string-table key also shows somewhere that must keep the shared text
    for rel, fields in (ov.get("objects") or {}).items():
        exports = json.load(open(os.path.join(ROOT, rel), encoding="utf-8"))
        for field, text in fields.items():
            parts = [int(p) if p.isdigit() else p for p in field.split(".")]
            idx = next(i for i, x in enumerate(exports) if parts[0] in (x.get("Properties") or {}))
            cur = exports[idx]["Properties"]
            for p in parts:
                cur = cur[p]
            assert isinstance(cur, dict) and ("SourceString" in cur or "CultureInvariantString" in cur), \
                "%s/%s is not a text field" % (rel, field)
            op = obj_path(exports, idx, "/Game/" + rel[:-5])
            st = steps(exports[idx]["Properties"], parts)
            assert op and st, "can't reach %s/%s" % (rel, field)
            sets = objects.setdefault(op, [])
            sets[:] = [x for x in sets if json.dumps(x[0]) != json.dumps(st)]
            sets.append((st, text))
            n_over += 1

lines = ["local TABLES = {"]
for tp, t in tables.items():
    lines.append("  {path=%s, struct=%s, name=%s, rows={" % (lua(tp), lua(t["struct"]), lua(t["name"])))
    for row, sets in t["rows"].items():
        lines.append("    [%s]={%s}," % (lua(row), ",".join("{%s,%s}" % (lua_steps(s), lua(x)) for s, x in sets)))
    lines.append("  }},")
lines.append("}")
lines.append("local OBJECTS = {")
for op, sets in objects.items():
    lines.append("  {path=%s, sets={%s}}," % (lua(op), ",".join("{%s,%s}" % (lua_steps(s), lua(x)) for s, x in sets)))
lines.append("}")
lines.append("local WRAP = {")
for op in (wrap if WRAP else []):
    lines.append("  %s," % lua(op))
lines.append("}")
data = "\n".join(lines)

tpl = open(TEMPLATE, encoding="utf-8").read()
begin, end = "-- ==== DATA BEGIN (written by build_lua_text.py) ====", "-- ==== DATA END ===="
a, b = tpl.index(begin) + len(begin), tpl.index(end)
open(OUT, "w", encoding="utf-8", newline="\n").write(tpl[:a] + "\n" + data + "\n" + tpl[b:])
nt = sum(len(s) for t in tables.values() for s in t["rows"].values())
no = sum(len(s) for s in objects.values())
print(f"{len(tables)} tables, {sum(len(t['rows']) for t in tables.values())} rows, {nt} table fields; "
      f"{len(objects)} objects, {no} object fields -> {OUT}")
print(f"{n_over} row overrides; {len(wrap) if WRAP else 0} text widgets set to wrap")
print("left out:", dict(skipped))
if "--report" in OPTS:
    for k, n in skipped_where.most_common(40):
        print("  %5d  %s" % (n, k))
