# Building the mod

You need Python 3, Unreal Engine 5.6 (for `UnrealPak.exe`) and an **FModel export** of the game (Blueprints, Configs, Localization, Movies), plus the line list (`units_with_official_en.json`) made from that export. The line list holds the game's own text, so it isn't published here.

1. **Translations with game code:** `python make_translations.py <units.json> ../translation/EasternEra_en.json translations.json`
   puts the game's colour tags, images and placeholders back into each English line.
2. **Language file:** `python build_locres.py <export>/Localization/Game/en/Game.locres <units.json> translations.json Game.locres <export> --overrides=../translation/row_overrides.json`
   writes `Game.locres` for the `en` culture. `locres_key_overrides` in the overrides file set single text keys (for example a name format or a tag that shares Chinese with other text).
3. **Lua part:** `python build_lua_text.py <export> <units.json> translations.json lua_template.lua Main.lua --overrides=../translation/row_overrides.json`
   writes the Lua mod: text the language file can't reach (culture-invariant text in data tables and UI templates), per-row and per-object fixes, lone Chinese separators turned into ASCII, and the layout fixes listed at the top of `lua_template.lua` (shrunk labels, a tooltip that ignores the mouse).
4. **Pak:** pack `Game.locres` with UnrealPak, mounted at `../../../EasternEra/Content/Localization/Game/en/`:
   `UnrealPak.exe pakchunk990-XianxiaEnglish-Windows_P.pak -create=response.txt`
   where `response.txt` holds one line: `"<path>\Game.locres" "../../../EasternEra/Content/Localization/Game/en/Game.locres"`.

`row_overrides.json` sections: `"Configs/<table>.json": {row: {field: text}}` for data-table rows (dotted paths; `TextParams.<Key>` for a format parameter, `Name.5` for item 5 of an array), `"objects"` for single assets, `"locres_key_overrides"` for `Namespace/Key` text. Keys starting with `_` are notes.
