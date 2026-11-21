"""Turn the fresh translation (EasternEra_en.json, tokens like {T1}..{/T}, {BR}) into translations.json
with the game code put back, the format build_locres.py and build_lua_text.py read.

Usage: python -I make_translations.py <units_with_official_en.json> <EasternEra_en.json> <out translations.json>
"""
import json, sys

UNITS, EN, OUT = sys.argv[1:4]


def restore(s, info):
    """Same as import_epub.restore: undo epub_common.encode."""
    if "ws" in info:
        s = info["ws"][0] + s + info["ws"][1]
    for n, tag in enumerate(info.get("tags", []), 1):
        s = s.replace("{T%d}" % n, tag)
    for n, tag in enumerate(info.get("imgs", []), 1):
        s = s.replace("{I%d}" % n, tag)
    s = s.replace("{/T}", "</>").replace("{BR}", info.get("nl", "\n")).replace("{R}", "/r")
    if "wrap" in info:
        a, tag, b = info["wrap"]
        s = a + tag + s + "</>" + b
    return s


units = json.load(open(UNITS, encoding="utf-8"))
en = json.load(open(EN, encoding="utf-8"))
out = {i: restore(en[i], u.get("info", {})) for i, u in units.items() if i in en}
json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(f"{len(out)}/{len(units)} lines -> {OUT}")
