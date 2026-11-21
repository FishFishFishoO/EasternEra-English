# Eastern Era: English Translation

A new English translation of **Eastern Era**, made from the original Chinese. It replaces the game's built-in English everywhere: menus, quests, items, martial arts, traits, dialogue and the tutorial.

- **Wuxia, not Xianxia.** Terms fit a martial arts world: Training, Dantian, Lightness Skill, Hidden Weapons, Star Crystal.
- **One term everywhere.** A stat, item or building has the same name in every menu, tooltip and quest.
- **Says what things do.** Items, traits, perks and buildings state their real effects, checked against the game's data.
- **Fits the screen.** Long names are shortened, and a few UI labels are drawn slightly smaller so English isn't cut off.
- **Plain text.** No special characters, which the game's font doesn't show well.
- **Names in pinyin**, surname first ("Tang Yi").

Status: **in testing** on game version 1.3. Please report anything that reads oddly, doesn't fit, or still shows Chinese.

## Install

1. Download `EasternEra-English.zip` from **[Releases](../../releases)** (on the right of this page).
2. Open your game folder: in Steam, right-click Eastern Era > **Manage** > **Browse local files**, then open `EasternEra\Content`.
3. Copy `Paks\pakchunk990-XianxiaEnglish-Windows_P.pak` into `Content\Paks`.
4. Copy the `Mods\xianxiaenglish` folder into `Content\Mods` (make the `Mods` folder if it isn't there).
5. Start the game, set the language to **English**, and turn on **Xianxia English** in the Mod List.

The translation has two parts and needs both: the `.pak` holds the main text, and the Lua mod sets text the game keeps outside its language file.

**Uninstall:** delete the `.pak` file and the `xianxiaenglish` folder.

## Good to know

- Characters created before you installed keep their old name spacing over their heads ("NiuGuang"). New characters, and everyone in a new game, show "Niu Guang".
- Two spots the game builds in its own code can't be changed from text: skill requirements show as "Intelligence3", and the skill type line may show a wide colon after "Type".

## What's in this repo

| Folder | What's in it |
|---|---|
| `mod/` | The ready-to-use mod, the same files as the Release zip. |
| `translation/` | The English text (`EasternEra_en.json`, keyed by line), per-row fixes (`row_overrides.json`) and the glossary of every term decision (`glossary.md`). |
| `tools/` | The scripts that build the mod. See [tools/BUILD.md](tools/BUILD.md). |

The game's own text is not included. Building needs your own export of the game files (see the build notes).

Translation by FishFishFish.
