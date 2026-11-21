# Eastern Era translation glossary (fresh run, started 2026-11-19)

Made with the chinese-to-english skill. Nothing from the old OpenNovel run is used.

## Style note

- Game text: labels, buttons, item/skill/building names, descriptions, quest text, letters, NPC dialogue.
- Genre: wuxia with a light cultivation layer (Dantian, realms, Qi Shield). Grounded, not modern.
- Labels and buttons: short, no subject, Title Case like the game's own English UI.
- Spelling: American (color, honor, armor, defense, traveling, practice). One "…" for 「……」. "Lv 1", never "Lv.1". "Exp", never "exp". User choice 2026-11-20.
- Descriptions: plain sentences, one pattern per repeated structure.
- Dialogue: spoken English in the speaker's voice. Elders formal, bandits crude, merchants chatty. 说/道 = said. Nothing added.
- Flavour text (item lore, art descriptions): plain and brief, same length as the Chinese.
- Keep every placeholder, tag and line break exactly (game-and-ui-text.md); run check_strings.py on every batch.

## Sources, in order of priority

1. Decisions in this file (the "Decided" table below).
2. The skill's Eastern Era glossary: `references/glossaries/eastern-era.md` (official English for mechanics, stats, realms; pinyin sects and places).
3. The skill's `names-and-terms.md` and `words-and-style.md`.
4. People: `names.md` next to this file (1,604 named characters with gender; built by `Fishs-Mods/Tools/translation/build_names.py`).
5. Anything else: the game's official English for the same key (`units_with_official_en.json`, field `en_official`) is a reference for mechanics only, never copied for prose.

## Decided

| Chinese | English | Type | Notes |
|---|---|---|---|
| 阿 + name | A-Name | person | 冯阿三 Feng A-San |
| 了 + name (monks) | Liao- | person | 了尘 Liaochen |
| 珩 / 爪 / 都 in names | heng / zhua / du | person | pypinyin gets these wrong |
| 亚瑟 | Arthur | person | male, Post Station knight |
| 宫本武藏 | Miyamoto Musashi | person | male |
| 百晓生 | Bai Xiaosheng | person | male, Post Station rankings keeper |
| 书籍商 / 杂货商 / 特产商 / 装备商 | Book / General / Specialty / Equipment Merchant | role | |

### User decisions 2026-11-19

Forms of address are ENGLISH (no pinyin titles). Capitalise when used as a name or direct address, lowercase in description.

| Chinese | English | Type | Notes |
|---|---|---|---|
| 师父, 师尊 | Master | address | "my master" in description |
| 师祖 | Grandmaster | address | |
| 师兄 / 师姐 | Senior Brother / Senior Sister | address | 大师兄 Eldest Senior Brother |
| 师弟 / 师妹 | Junior Brother / Junior Sister | address | 小师妹 Youngest Junior Sister |
| 师叔 / 师伯 | Martial Uncle | address | |
| 前辈 | Senior | address | |
| 晚辈 (self) | I (this junior where the humility is the point) | self | |
| 少侠 | young hero | address | |
| 大侠 | hero | address | |
| 女侠 | heroine | address | |
| 姑娘 | miss / young lady | address | with surname: Miss Long |
| 公子 | young master | address | |
| 掌门 | Sect Master | rank | |
| 长老 | Elder | rank | |
| 堂主 | Hall Master | rank | |
| X大师 | Master X | honorific | 玄空大师 Master Xuankong (Buddhist) |
| X真人 | Daoist Master X | honorific | 云鹤真人 Daoist Master Yunhe |
| 傀儡 | Puppet | term | NOT the game's "Automaton" |
| 机关 | Mechanism; 机关X → Mechanical X | term | 机关兽 Mechanical Beast, 机关狗 Mechanical Dog |
| 星能 | Star Energy | term | user choice 2026-11-20 (was Star Energy); NOT "Stellar Energy" |
| 星棱 | Star Crystal | term | user choice 2026-11-20 (was Star Prism); NOT "Stellar Crystal" |

## Terms fixed while translating (in batch order)

| Chinese | English | Type | Notes |
|---|---|---|---|
| 机关台 | Mechanism Bench | building | |
| 百宝楼 | Hundred Treasures Tower | building | |
| 星能塔 | Star Energy Tower | building | |
| 大世界 | Overworld | UI | |
| 游历 | Travel | UI | |
| 图鉴 | Codex | UI | |
| 妖兽 | demon beast | creature | |
| 出战弟子 | Fighting Disciples | UI | |
| 俘虏处置 | Captive Handling | UI | |
| 正义值 | Righteousness | stat | |
| 天下第一 | Best Under Heaven | title | |
| 洗炼, 洗练 | Refine | UI | Refine Points, Refine Target |
| 参悟 | Comprehend | UI | |
| 词条 | affix | UI | |
| 层 (martial art level) | Lv | UI | 13层 Lv 13 |
| 比武台 | Martial Arena | building | |
| 修炼房 | Cultivation Room | room | |
| 丹鼎房 | Cauldron Room | room | |
| 运功 | circulate | UI | 已运功 Circulating |
| 功力 | Mastery | UI | |
| 结拜 | Sworn Sibling | UI | 结拜仪式 Sworn Sibling Ceremony |
| 枪棍 | Spear & Staff | weapon class | |
| 美观 | Beauty | room stat | |
| 光照 | Light | room stat | |
| 九阴真经 | Nine Yin Scripture | art | |
| 太极神功 | Taiji Divine Skill | art | |
| 流云剑 | Flowing Cloud Sword | art | |
| 开启丹田 | Open Dantian | UI | 丹田未开 → Dantian not open |
| 感悟值 | Insight | stat | |
| 饱腹度 | Fullness | stat | |
| 时辰 (game rate) | h / hour | unit | |
| 灵位 | Memorial Tablet | building part | |
| 祠堂 | Ancestral Hall | building | |
| 堂口 | Hall | UI | 所属堂口 Assigned Hall |
| 研究台 / 沙盘 / 演星台 | Research Desk / Sand Table / Stargazing Platform | building | |
| 初级/中级/高级科技点数 | Basic/Intermediate/Advanced Tech Points | UI | |
| 金丹初期 | Early Golden Core | realm | |
| 震古烁今 | Timeless | realm? | not in the 16-realm list |
| 止血粉 / 五石粉 / 安宫牛黄丸 | Styptic Powder / Five Stones Powder / Angong Niuhuang Pill | item | |
| 宗主 | Sect Lord | rank | 掌门 is Sect Master |
| 护法 | Protector | rank | |
| 分堂 | branch hall | UI | |
| 天阶/地阶/玄阶/黄阶 | Heaven/Earth/Mystic/Yellow-Grade | grade | 货柜 counter, 货架 shelf |
| 剧本 | Scenario | UI | new-game backstory picks |
| 例银 | Stipend | UI | 掌门例银 Sect Master Stipend, 堂主例银 Hall Master Stipend |
| sect suffixes | game official table kept (门 Order, 宗 Sect, 派 School, 教 Order, 帮 Syndicate, 会 Guild, 堂 Chapter...) | UI | per eastern-era.md; 山 Mountain, 岛 Island, 众 Band, 舵 Branch, 行会 Trade Guild, 堡 Fort |
| 历飞羽 | Li Feiyu | person | male; source also writes 历飞三羽/历飞3羽 (typos) |
| 汤姆 / 杰瑞 | Tom / Jerry | placeholder | |
| 城主 | City Lord | rank | |
| 镇守 | Garrison Commander | rank | |
| 繁荣 | Prosperity | stat | |
| 治安 | Public Order | stat | |
| 乱葬岗 | Mass Grave | building | |
| 薄葬名录 | Pauper's Burial Register | UI | |
| 怨气 | Resentment | stat | |
| 祭拜 | Pay Respects | action | |
| 能量网 / 能量管道 | Energy Network / Energy Pipes | UI | |
| 冰心诀 | Ice Heart Formula | art | |
| 场外操作 | Off-Field Action | tournament | |
| 诽谤 | Slander | tournament | |
| 结交 / 断交 | Befriend / Cut Ties | diplomacy | |
| 死敌 | Sworn Enemy | relation | |
| 内劲 | Inner Strength | art type | 内功 stays Internal Art |
| 斧棒 / 锤锏 / 弓弩 | Axe & Staff / Hammer & Mace / Bows & Crossbows | weapon class | |
| 火器 | Firearms | weapon class | |
| 暗器 | Hidden Weapon | weapon class | user choice 2026-11-20 (was Projectile); 弹道 stays "projectile" |
| 历练 | Adventure | UI | 历练派遣 Send on Adventure |
| 清明 | Qingming | festival | |
| 大还丹 | Great Restoration Pill | item | |
| 六扇门 | Six Doors | org | |
| 襄阳城 | Xiangyang City | place | |
| 玄冥宗 | Xuanming Sect | sect | |
| 绝尘峪 / 落霞坞 / 南海群岛 | Juechen Valley / Luoxia Hollow / Nanhai Islands | place | |
| 曲谱 | Music | UI | |
| 星棱石 | Star Crystal | material | |
| 天灯之劫 | the Sky Lantern Calamity | lore | |
| 成化 | Chenghua | era | 成化帝 the Chenghua Emperor |
| 中原 | Central Plains | place | |
| 机关兽 | mechanical beast | creature | |
| 金钟罩 | Golden Bell Shield | art | |
| 玄渊门 | Xuanyuan Sect | sect | the player sect origin |
| 赤霞剑派 | Chixia Sword Sect | sect | |
| 万毒门 | Wandu Sect | sect | (万毒帮 is Wandu Gang) |
| 唐门 | Tang Sect | sect | |
| 少林 | Shaolin | sect | |
| 少掌门 | young Sect Master | rank | |
| captive {0} pronoun | they/them | rule | 他 in ransom/prison text is generic; captive can be any gender |
| 声名初显 / 名门正派 / 武林盟主 | Rising Fame / Renowned Righteous Sect / Martial Alliance Leader | difficulty | 初涉江湖 New to the Jianghu |
| 丐帮 | Beggar Sect | sect | user choice 2026-11-20 (was Gaibang); exception to 帮 = Gang |
| 舵主 / 分舵 | branch head / branch | rank | |
| 达摩洞 | Damo Cave | place | |
| 老君观 | Laojun Temple | place | |
| 西子湖 | West Lake | place | |
| 港帮 / 潜帮 | Harbor Gang / Qian Gang | org | |
| 天下会 | Tianxia Society | sect | |
| 帝都 | the imperial capital | place | |
| apprenticeship events | present tense; "A disciple ..." event names | style | |
| 西岳峰 / 凌云顶 / 少室山 / 青城山 / 武当山 | Xiyue Peak / Lingyun Summit / Mount Shaoshi / Mount Qingcheng / Mount Wudang | place | |
| 唐家堡 | Tangjia Fort | place | |
| 客卿 | retainer | rank | |
| 乡勇 | village militia | role | |
| 衙役 / 巡捕 | yamen runner / constable | role | |
| 刀客 | sabersman | role | |
| towns (apprenticeship) | 棘林村 Jilin Village, 云杉坪 Yunshan Flat, 铁木坡 Tiemu Slope, 枫杨渡 Fengyang Ferry, 松风谷 Songfeng Valley, 丹霞寨 Danxia Stronghold, 乌头村 Wutou Village, 蜀客村 Shuke Village, 玄石寨 Xuanshi Stronghold, 葵峪镇 Kuiyu Town, 翠泉坞 Cuiquan Hollow, 玉田乡 Yutian Township, 沙枣村 Shazao Village, 稻香村 Daoxiang Village, 牛家庄 Niujia Manor, 晓铃滩 Xiaoling Shoal, 青牛涧 Qingniu Gully, 鹭湾村 Luwan Village, 白溪渡 Baixi Ferry, 渔湾村 Yuwan Village, 珠贝村 Zhubei Village | place | |
| 伏虎岭 / 星台山 / 风陵渡 / 燕子坞 / 天山 | Fuhu Ridge / Xingtai Mountain / Fengling Ferry / Yanzi Hollow / Tianshan | place | |
| breakthrough talents | meaning, short: 集气 Gather Qi, 锋锐 Keen Edge | trait | |
| 夯土 | Basic (starter building tier) | material | 夯土地基 Basic Foundation, 大型夯土地基 Large Basic Foundation, 夯土墙 Basic Wall, 夯土小屋 Basic Hut, 夯土长屋 Basic Longhouse, 夯土建筑 Basic Walls & Roofs (user choice 2026-11-20) |
| 青石 | Bluestone | material | |
| 汤池 | Bathing Pool | building | |
| 投壶 | Pitch-Pot | building | |
| 制药台 | Medicine Table | building | |
| 炼药炉 | Alchemy Furnace | building | |
| 疗养床 | Recovery Bed | building | 星能疗养床 Star Energy Recovery Bed |
| 窝棚 | Shack | building | |
| 院墙 / 栅栏 / 篱笆 | Courtyard Wall / Palisade / Fence | building | |
| 月洞门 | Moon Gate | building | |
| 抄录台 / 阅读台 | Transcription Desk / Reading Desk | building | |
| 烽沙帮 | Fengsha Gang | org | FS furniture desc: "A band of intruders of unknown origin who call themselves the Fengsha Gang made some objects from their homeland as they remember it. This is one of them: ..." |
| 货栈 | Warehouse | building | |
| 打造台 / 手工台 / 工艺台 | Smithing Bench / Handcraft Bench / Craftwork Bench | building | |
| 书案 | Writing Desk | building | |
| 演武台 | Practice Stage | building | 比武台 Martial Arena |
| 寒玉床 / 药浴池 / 蒲团 / 观武案 | Cold Jade Bed / Medicinal Bath / Meditation Cushion / Martial Assessment Desk | building | |
| 摆件 / 挂件 / 挂画 / 香炉 | Ornament / Wall Hanging / Hanging Scroll / Censer | prefix | |
| 美观度 / 清洁度 | Beauty / Cleanliness | room stat | |
| 筑基丹 | Foundation Pill | item | |
| 墨家 | Mohist | lore | 墨家机关 Mohist mechanisms |
| 星能井 | Star Energy Well | building | |
| 星能传导塔 | Star Energy Tower | building | short, = 星能塔 |
| 傀儡台 / 傀儡改装台 | Puppet Platform / Puppet Refit Platform | building | |
| 机关鸟 | mechanical bird | unit | |
| 牌坊 / 引路石 / 迎客亭 | Memorial Archway / Guiding Stone / Welcome Pavilion | building | |
| 飞梭 / 飞梭台 | flying shuttle / Shuttle Platform | building | |
| 物资库 | Supply Store | building | |
| 十八铜人 | Eighteen Bronze Men | building | |
| 真武大帝 | Zhenwu the Great Emperor | deity | |
| 琅嬛 | Langhuan | deity | goddess |
| 天演殿 | Tianyan Hall | building | |
| 感悟 (stat) | Insight | stat | |
| 息壤 | Xirang | material | self-growing soil of legend |
| 玄铁 | Black Iron | material | |
| 江南 | Jiangnan | place style | |
| 霸下 | Baxia | creature | |
| 三潭印月 | Three Pools Mirroring the Moon | landmark | |
| 箭塔 | arrow tower | building | |
| 土坟 / 侠冢 / 乱葬岗 | Earth Grave / Hero's Tomb / Mass Grave | building | |
| 膳堂 / 厢房 / 天工堂 / 研究室 / 灶房 | Dining Hall / Bedroom / Hall of Heavenly Works / Study / Kitchen | room | |
| 刑台 / 站笼 / 鞭刑架 | Execution Platform / Standing Cage / Flogging Rack | building | |
| 温度等级 | 极寒 Freezing, 寒冷 Cold, 适宜 Comfortable, 炎热 Hot, 酷热 Scorching | room | |
| martial art names | meaning in plain English; famous wuxia moves keep their known images; acupoint/sword names in pinyin (少商 Shaoshang); no 《》 in game text | style | QA at the end: every short name must match inside longer lines |
| 赤霄 / 绿沉 | Chixiao / Lüchen | weapon | famous names, pinyin |
| practice rooms | 精武堂 Martial Arts Hall, 藏锋阁 Sword Pavilion, 射圃 Archery Training Ground, 养气斋 Qi Pavilion, 澄心堂 Meditation Hall, 锐锋堂 Spear Pavilion, 凌云阁 Lightness Skill Training Hall | room | user choice 2026-11-20; techs 905/906 named Ranged Training / Weapon Training via row_overrides locres_key_overrides |
| element rooms | 清庚居 Qinggeng Lodge, 青衍居 Qingyan Lodge, 玄渊室 Xuanyuan Chamber, 丹曜居 Danyao Lodge, 厚德居 Houde Lodge | room | pinyin names |
| 病房 / 库房 / 武库 / 监狱 | Infirmary / Storeroom / Armory / Prison | room | |
| 心法 | Method | art suffix | 烈羽心法 Blazing Feather Method |
| 功 / 神功 / 诀 / 式 | Skill / Divine Skill / Formula / Stance | art suffix | |
| surnames | pinyin, game official spelling errors fixed (夏 Xia, 陆 Lu, 牛 Niu, 沙 Sha, 月 Yue); 宫本 Miyamoto | person | |
| realm list | Novice (1) ... Sage (16), names from eastern-era.md | realm | |
| 药人 | Drug Thrall | creature | 万毒门药人 Wandu Sect Drug Thrall |
| 僵尸 / 毛僵 / 飞僵 | Jiangshi / Hairy Jiangshi / Flying Jiangshi | creature | |
| 机关玄刃 | Mechanical Black Blade | creature | |
| 獬豸 | Xiezhi | creature | |
| 黑风寨 | Heifeng Stronghold | place | 大当家 Chief, 二当家 Second Chief |
| 易筋经 / 葵花宝典 / 辟邪剑谱 / 斗转星移 / 降龙 | Sinew-Changing Sutra / Sunflower Manual / Evil-Warding Sword Manual / Shifting the Stars / Dragon-Subduing | art | |
| 丹 / 丸 | Pill | item suffix | 小还丹 Lesser Restoration Pill |
| 眩晕 / 冻结 | Stun / Frozen | status | |
| traits | names in plain English; internet memes kept as the same joke in English (金坷垃 Jinkela, 菜就多练 Bad? Practice More, 练习生 Trainee + Iron Mountain Lean) | trait | |
| hall (branch) effects | 诏令该堂弟子... = Orders this hall's disciples to ... | trait | |
| 斤 / 钧 | jin / jun | unit | |
| 谪仙 | banished immortal | lore | |
| 药王 | Medicine King | title | |
| 心情 (in buff lines) | Happiness | stat | "{I1}{T1} Name: Happiness {0} {/T}" pattern |
| buff effect lines | "{I1}{T1} Name {/T}: {T2}Stat +{0} {/T}" | style | full-width colon becomes ": " |
| 凌波微步 | Lingbo Steps | art | |
| 庖丁 | Master Butcher Ding | room buff | |
| 福神 | God of Fortune | deity | |
| consumables | 熊胆丸 Bear Gall Pill, 寒锋散 Cold Edge Powder, 安息香 Benzoin Incense, 七星海棠膏 Seven-Star Begonia Salve, 续断膏 Xuduan Salve, 断金散 Gold-Cutting Powder, 贯山丸 Mountain-Piercing Pill, 养元丹 Origin-Nurturing Pill, 踏雪丸 Snow-Treading Pill, 八珍酒 Eight Treasures Wine, 黑玉断续膏 Black Jade Bone-Mending Salve, 天王保命丹 Heavenly King Life-Saving Pill, 田家乐 Farmhouse Joy, 罡气丹 Qi Shield Pill, 匠作酒 Craftsman's Wine, 通玄丸 Mystery-Piercing Pill, 金刚护体丹 Vajra Body-Guarding Pill, 易筋经拓本 Rubbing of the Sinew-Changing Sutra, 大力金刚丸 Mighty Vajra Pill | item | |
| consumable bonus traits | 铁布 Iron Cloth, 百毒不侵 Immune to All Poisons, 霜锋 Frost Edge, 贯山 Mountain-Piercing, 玄铁锋 Black Iron Edge, 踏雪 Snow Treading, 砗磲护体 Giant Clam Guard, 凝玉 Condensed Jade | trait | |
| 天机门 halls | 南斗堂 Nandou Hall, 天市堂 Tianshi Hall, 北斗堂 Beidou Hall, 紫薇堂 Ziwei Hall, 太微堂 Taiwei Hall | org | |
| 望月峰 | Wangyue Peak | place | |
| 尉迟骁 | Yuchi Xiao | person | male |
| 总捕头 | Chief Constable | rank | |
| 拂晓神剑 | Divine Sword of Dawn | title | Arthur |
| 闪电五连鞭 | Lightning Five-Whip Combo | art | meme |
| 秦阎王 / 鬼面鸿 | King Yama Qin / Ghost-Faced Hong | epithet | |
| 惊鸿 / 冷月 (weapons) | Startled Swan / Cold Moon | weapon | |
| 柳茹是 | Liu Rushi | person | female; 是 is part of the name |
| 赤努 | Chi Nu | person | male |
| 墨千机 | Mo Qianji | person | male; Mohist heir |
| 东瀛 | Dongying | place | Japan in wuxia |
| 汴河 / 州桥 / 相国寺 | Bian River / Zhou Bridge / Xiangguo Temple | place | Kaifeng |
| 把头 / 牙侩 | Foreman / Broker | role | |
| 雷爷 | Master Lei | person | |
| 大人 (said to the player) | Sect Master | address | user 2026-11-19 |
| 云鹤真人 / 玄空大师 / 龙姑娘 (name fields) | Daoist Master Yunhe / Master Xuankong / Maiden Long | person | user 2026-11-19; title units hold the given name (真人=Yunhe, 大师=Xuankong, 姑娘=Long), first-name field overridden per row: row_overrides.json |
| 苏茹是 | Su Rushi | person | female; her line says 我叫苏茹 (source drops 是), kept as Su Rushi for consistency |
| 魔教 | Demonic Cult | org | |
| 无极门 | Wuji Sect | sect | fake sect in a joke backstory |
| 苏妲月 / 苏媚儿 | Su Dayue / Su Meier | person | sisters, female |
| 玄狐 / 月狐 (outfits) | Dark Fox / Moon Fox | clothing | |
| 雄狮帮 | Xiongshi Gang | sect | |
| 节气 | 惊蛰 Waking of Insects, 谷雨 Grain Rain | calendar | |
| 衡山派 / 雪山派 | Hengshan Sect / Xueshan Sect | sect | |
| 全真教 | Quanzhen Sect | sect | famous Daoist school; "Sect" not "Cult" (exception to 教 = Cult) |
| 趟子手 | path-crier | role | escort agency |
| 城隍庙 | City God Temple | place | |
| 铁剑门 / 漕帮 | Tiejian Sect / Cao Gang | sect | |
| 六袋弟子 / 帮主 | six-pouch disciple / Chief | rank | Beggar Sect |
| 莫愁 | Mochou | person | female |
| 丈 | zhang | unit | |
| life skills | 务农 Farming, 建造/修建 Construction, 挖掘/采矿 Mining, 烹饪 Cooking, 动物 Taming, 制作/制造 Crafting, 艺术 Art, 治疗 Healing, 纵横 Diplomacy, 智力 Intelligence, 战斗 Combat | skill | X技能 = X Skill |
| 雅娱 | Refined Recreation | stat | |
| 生育 (organ) | Reproductive Organs | body | |
| 少主 (to the player) | Young Sect Master | address | gender-neutral, matches 少掌门 |
| 识位诀 | Position-Sensing Formula | art | tutorial |
| quality colors in text | 绿/蓝/紫/橙/金 色 = green/blue/purple/orange/golden | UI | N阶 = Lv N |
| 营造法式 | building methods | item | tutorial |
| 藏兵阁 / 奇珍阁 | Armory Pavilion / Treasure Pavilion | building | old sect |
| 青云心法 | Qingyun Method | art | |
| 烩饼 | Braised Flatbread | food | |
| shichen in dialogue | plain times of day (dawn, morning, noon, dusk, late evening) | style | |
| 血影教 | Xueying Cult | sect | |
| 内门堂主 | Inner Hall Master | rank | |
| player Sect Master in 3rd person | they/them (他 is generic) | rule | player gender unknown |
| 五连鞭 meme (Ma Baoguo) | "I was careless, I didn't dodge!", "young people have no martial ethics", 耗子尾汁 pun → "behave yourself" (pun lost) | meme | |
| 小翠 / 李财主 | Xiaocui / Squire Li | person | |
| 阴婚 | ghost marriage | lore | |
| 兵器谱 / 英才榜 | Weapon Rankings / Talent Rankings | UI | |
| 门主 (to the player) | Sect Master | address | |
| 灵粟 | spirit millet | item | |
| 麒麟臂 / 麒麟酒 | Qilin Arm / Qilin Wine | item | |
| 老夫 / 老朽 | this old man (when the speaker stresses age), else I | self | |
| 洪七 | Hong Qi | person | male, Beggar Sect elder |
| 叫花鸡 | beggar's chicken | food | |
| 宗主 (to the player) | Sect Master | address | |
| 鸠摩志 / 大轮寺 / 吐蕃 | Jiumo Zhi / Dalun Temple / Tubo | person/place | 小僧 = this humble monk (kept, it is his voice) |
| 蓉儿 | Rong'er | person | |
| 鸳鸯五珍脍 | Mandarin Duck Five Delicacies | food | |
| 精致级 | Exquisite | food grade | |
| 机关铜人 | mechanical bronze man | creature | |
| 鎏纹铜锈甲片 / 鎏金旋纹箔片 | Gilded Patina Armor Plate / Gilded Swirl Foil | item | |
| 施主 | benefactor | address | monks to lay people |
| 贫僧 / 小僧 | this humble monk | self | |
| 还施水阁 | Huanshi Water Pavilion | place | Murong library |
| dice | 大 Big, 小 Small, 豹子 Triples | game | |
| 潜龙帮 | Qianlong Gang | sect | |
| 郝雄 | Hao Xiong | person | male, old Tianji Sect member |
| 少门主 | Young Sect Master | address | |
| 郝叔 | Uncle Hao | address | |
| 廖贾 | Liao Jia | person | male |
| 老门主 | the old Sect Master | person | player's father |
| 廖堂主 | Hall Master Liao | address | Liao Jia |
| 路条 / 货牌 | travel permit / cargo tag | item | Kaifeng quests |
| 蜀山异矿砂 | Shushan exotic ore sand | item | |
| 卢临风 | Lu Linfeng | person | grain store owner |
| 碧螺灵茶 | Biluo Spirit Tea | item | |
| 丰裕粮行 | Fengyu Grain Store | place | |
| [援助] quests | [Aid] | quest | |
| 悬空寺 / 雪隐寺 | Hanging Temple / Snow Hermit Temple | place | |
| 中州 | Zhongzhou | place | quest tag |
| 洪老前辈 | Elder Hong | address | Hong Qi |
| 论剑大会 | Sword Discussion Assembly | event | |
| 门派时装N阶 | Sect Fashion Tier N | tech | |
| clothing sets | 江湖款 Jianghu, 绣花 Embroidered, 重装纹 Heavy Patterned, 深色质 Dark, 考究款 Refined, 华贵 Luxurious + Clothes/Trousers/Shoes | item | |
| clothing modifiers | 款 -Cut (only where a plain name exists, else dropped), 式 -Style, 面 -Faced, 质 fabric (dropped), 纹 Patterned; 干练 Smart, 紧身 Tight, 锦缎 Brocade, 名门 Noble House, 灰布 Gray Cloth/Gray-Faced, 考究 Refined, 天蚕 Heavenly Silkworm, 精铁 Fine Iron, 蓝绸 Blue Silk, 华贵 Luxurious, 短打 Short Work, 利落 Neat, 青棉 Blue Cotton, 粗麻 Coarse Hemp, 素色 Plain, 布衣 Commoner, 深色 Dark, 寻常 Ordinary, 沉香 Agarwood, 上等 Fine | item | from b066 on |
| recipe template | 制作{Numeber}{Function}{Quality}{Item} = "Make {Numeber} {Quality} {Item}, {Function}."; Function fragments = "used to ..."; Quality = lowercase adjective | UI | |
| tech books | 营造法式 Building Methods, 天工开物 Exploitation of the Works of Nature, 鲁班书 Book of Lu Ban | item | |
| 幽冥草 | Netherweed | plant | |
| 墨云环 / 火云环 / 璃龙环 | Blackcloud Ring / Firecloud Ring / Glass Dragon Ring | accessory | |
| art level suffix | "-XX功N层" = " - <Art> Lv N"; "N层XX" = "<Art> Lv N" | style | |
| 降龙十八掌 | Eighteen Dragon-Subduing Palms | art | |
| 智慧 | Wisdom | stat | |
| status names | [破甲] Sunder, [中毒] Poison, [流血] Bleeding, [灼烧] Burn, [沉默] Silence, 冻结 freeze | combat | |
| 【进攻】/【撤退】 | [Attack] / [Retreat] | UI | |
| 踏月留香 / 天罗步 | Treading the Moon, Leaving Fragrance / Heaven's Net Steps | art | |
| 武学基础: X | Martial Basics: X | UI | |
| skill prefixes | 枪戟- Spear -, 拳掌- Fist -, 刀剑- Sword -, 暗器- Hidden Weapon - | UI | |
| statuses with tiers | [减速Ⅰ] Slow I, [破甲Ⅰ] Sunder I, [流血Ⅰ] Bleeding I, [剧毒Ⅲ] Deadly Poison III, [缴械Ⅰ] Disarm I, [弹射] Bounce | combat | ASCII numerals |
| more statuses | [致盲] Blind, [霸体] Unstoppable, [冰冻] Frozen | combat | |
| more statuses | [定身] Root, 吸血 lifesteal, [狂暴] Frenzy | combat | |
| 传承- | Legacy - | UI | |
| 词条：X | Affix: X | UI | |
| 混元功 | Hunyuan Skill | art | |
| 龟息功 | Turtle Breath Skill | art | |
| 草上飞 | Flying Over Grass | art | |
| 养气诀 | Qi Nurturing Formula | art | |
| 寸劲功 | Inch Force Skill | art | |
| 袖箭功 | Sleeve Arrow Skill | art | |
| 舍身功 | Self-Sacrifice Skill | art | |
| 连环桥手 | Chained Bridge Hands | art | |
| 凝气诀 | Qi Condensing Formula | art | |
| 先天功 | Innate Skill | art | |
| 吸星大法 | Star-Absorbing Great Method | art | |
| 摄魂经 | Soul-Seizing Sutra | art | |
| 饮血魔功 | Blood-Drinking Demonic Art | art | |
| 穿云破空诀 | Cloud-Piercing Sky-Breaking Formula | art | |
| 神机火龙诀 | Divine Mechanism Fire Dragon Formula | art | |
| 不死印法 | Undying Seal Method | art | |
| 道心种魔 | Dao Heart Demon Seed | art | |
| 太清神焰 | Taiqing Divine Flame | art | |
| 换日大法 | Sun-Swapping Great Method | art | |
| X窗 | X window | UI | timed buff window |
| 虚弱 | Weakness | status | |
| crops | 麦 Wheat, 粟 Millet, 水稻 Rice, 玉米 Corn, 莲子 Lotus Seed, 棉 Cotton, 菇 Mushroom, 南瓜 Pumpkin, 茶丛 Tea Bush, 果丛 Berry Bush, 葛丛 Kudzu Bush, 毛蕨 Fern, 野草 Wild Grass, 绿荆条 Green Vitex, 杨树 Poplar, 桦树 Birch, 松树 Pine, 杏树 Apricot Tree, 椰树 Coconut Palm, 芭蕉树 Plantain Tree | plant | |
| X产出 | X Yield | UI | 砍伐 Felling, 采摘 Picking, 割除 Cutting, 收割 Harvest, 开采 Mining |
| X派 / X门 (jianghu sects) | X Sect | sect | 华山 Huashan, 青城 Qingcheng, 崆峒 Kongtong, 峨眉 Emei, 伏虎门 Fuhu, 飞星门 Feixing; 达摩禅院 Damo Chan Monastery |
| 江湖小道消息 | Jianghu rumour has it | log | |
| skill template fragments | {Direction}/{Distance}/{Target} | UI | templates read "to {Target} {Distance} {Direction}"; 对前方 ahead, 对四周 around you, 小范围 in a small area, 大范围 in a large area, 直线 in a line |
| 招式 / 近战 / 拳脚 (tags) | Move / Melee / Fist | UI | skill tag lists |
| recipe-only items | 金疮药 Golden Wound Medicine, 铁打丸 Iron Strike Pill, 磨刀石 Whetstone, 透骨药 Bone-Piercing Medicine, 轻身丸 Lightness Pill, 茯苓汤 Poria Soup, 三七散 Notoginseng Powder, 入门拳谱 Beginner's Fist Manual, 山参丸 Wild Ginseng Pill, 护体散 Body-Guarding Powder, 避瘴丸 Miasma-Warding Pill, 接骨丹 Bone-Setting Pill | item | 配方:X = Recipe: X |
| 天机阁 / 侠客岛 / 青牛镇 | Tianji Pavilion / Xiake Island / Qingniu Town | place | |
| secret realms | 十万大山 Hundred Thousand Mountains, 群雄会猎 Gathering of Heroes' Hunt, 两仪争枢 Two Forms Contest for the Pivot | place | |
| 武林大会 | Martial Tournament | event | |
| tech | 农耕分析 Farming Analysis, 木工初解 Carpentry Basics, 夯土结构 Basic Building Foundation, 山门初立 Founding the Sect | tech | |
| 戈止 (tech) | Arms Halt | tech | 初级/中级/星能戈止 Basic/Intermediate/Star Energy Arms Halt |
| tech branches | 门派与修炼 Sect and Cultivation, 天工与机巧 Heavenly Works and Mechanisms, 江湖与天下 Jianghu and the World; 道家 Daoist Heritage, 奇门 Puppet Arts, 达摩 Buddhist Heritage, 天下会 Tianxia Society Heritage (tech lines only, Lv.1-4; user choice 2026-11-20) | tech | |
| 比武大会 | Martial Contest | event | 武林大会 is Martial Tournament |
| 旱魃 | Hanba | creature | |
| faction suffixes (world map) | 派/门 Sect, 帮 Gang, 世家 Clan, 盟 Alliance, 阁 Pavilion, 楼 Tower, 寺/观 Temple, 宫 Palace, 教 Order, 会 Society, 堂 Hall, 卫 Guard, 庄 Manor, 山庄 Villa, 镖局 Escort Agency, 堡 Fort, 洞 Cave, 谷 Valley | sect | names in pinyin (聚宝帮 Jubao Gang, 玄铁门 Xuantie Sect) |
| 地铺 / 动物地铺 | Hay Bed / Animal Hay Bed | furniture | user choice 2026-11-20 (was Floor Bedding, then Hay Pallet) |
| 黄金/白银/玄铁/星棱矿坑 | Gold / Silver / Black Iron / Star Crystal Mine | building | user choice 2026-11-20: no "Pit" |
| 种植技艺 | Farming Techniques | tech | user choice 2026-11-20 (was Planting Craft) |
| 园丁技艺 | Landscaping (Lv.N) | tech | user choice 2026-11-20 (was Gardening Craft); decorative flowerbeds/trees, not farming |
| 车马驿站 | Courier Station | tech | user choice 2026-11-20 (was Carriage Post Station); unlocks Pigeon Coop + Stable. 驿站 the trading hub stays "post station" |
| 百打千锤 / 静心凝神 | Training Equipment / Meditation | tech | user choice 2026-11-20 (were A Hundred Blows, a Thousand Hammers / Calm the Mind, Focus the Spirit) |
| building renames 2026-11-20 | 清庚居/青衍居/玄渊室/丹曜居/厚德居 Metal/Wood/Water/Fire/Earth Breakthrough Room; 石锁 Stone Weight; 水车桩 Waterwheel Kick Trainer; 坛子功 Jar Grip Trainer; 琴台 Guqin Stand; 禅心映莲 Lotus Meditation Pond; 藏锋屏 Sword Dance Screen; 恒剑玉璧 Sword Jade Tablet; 天演殿 Group Training Hall; 码货区 Selling Area; 交易区 Purchase Area; 杂物柜 Storage Cabinet; 戈矛置架 Spear Rack; 大火炉 Decorative Stove; 南烟墙 Jiangnan Wall; 青砖长屋 Bluestone Brick Longhouse; 真武镇魔 Zhenwu Demon-Subduing Statue; 霸下负碑 Tortoise Stele; 舆架 Sedan Frame; 蟠螭小屏 Coiled Dragon Screen; 龙泉 Longquan Sword; 碎拼石/宝相花纹/团寿纹地基 Flagstone/Floral Pattern/Longevity Pattern Foundation | building | user approved (functional names) |

## 2026-11-20 terms checked against the Immortal Mountain glossary (user choices)
| Chinese | English | Type | Notes |
|---|---|---|---|
| 星棱 / 星棱石 | Star Crystal | term | was Star Prism; Star Crystal Mine |
| 星能 | Star Energy | term | was Star Energy; Star Energy Stove, Max Star Energy |
| 暗器 | Hidden Weapon(s) | weapon class | was mixed Projectile / hidden weapon; skill prefix "Hidden Weapon - X"; 弹道 (a move's projectile) stays "projectile" |
| 丹田 | Dantian | term | was Qi Source; Open Dantian, Dantian Exp, Max Dantian Health. 气源有术 (trait) still "Mastery of the Qi Source" |
| 轻功 | Lightness Skill | art type | was Acrobatic Arts; "lightness skill move", Lightness Skill Exp. 凌云阁 renamed Lightness Skill Training Hall (user OK 2026-11-20) |
| already matching | Jianghu, Sect Master, Core/Inner/Outer Disciple, Cultivation, Breakthrough, Meridians, Acupoints, Qi Deviation, Inner Demon, Manual, Sword Qi, Sword Intent, Taiji, Wuji, Elixirs, Realm, Innate | | no change |
| 阎罗 (as the underworld king) | King Yama | person | user choice 2026-11-20; matches 阎王令 King Yama's Order; Chief Constable Yan Luo is a different person |
| misc-terms page check 2026-11-20 | everything else on immortalmountain other-miscellaneous-terms already matches | | Big Dipper, Luohan Bed, Stone Weight, Pagoda Tree kept |
| status names 2026-11-20 | 中毒 Poison, 冰冻 Frozen, 冻结 Freeze, 流血 Bleeding, 灼烧 Burn, 蓄力 Charge Up | status | standalone names now match the [brackets] in move text |
| stats in text 2026-11-20 | 心情 = Happiness when it is the stat (numbers, tutorial headings, highlighted); plain "mood" fine in prose. 娱乐值 = Relaxation (the stat); 娱乐 schedule slot = Recreation | stat | |
| 罡气护体 | Qi Shield Guard | buff | was Qi Shield Body Guard |
| 饱腹度 / 饱食度 | Fullness | stat | 2026-11-20: 20 lines that said Satiety changed to Fullness |

## 2026-11-20 patch (new Fmodel export, C:\Dev\Fmodel\Output\Exports)
Units re-extracted from the new patch with export_by_folder.py (19,946 strings; 572 dev-only left out: comment keys, AI behavior-tree labels, debug/test panels, GOAP labels; list in newpatch_skipped.json). Old ids are gone: everything is keyed by the new ids. Old files: batches\before-patch-2026-11-20\. 16,883 lines carried over by matching Chinese, 181 reused where only a line break changed, the rest translated in batches p001-p013.

| Chinese | English | Type | Notes |
|---|---|---|---|
| 好感 / 好感度 | Affinity | diplomacy | |
| 宗旨 | creed | diplomacy | 激进 Aggressive |
| 血仇 / 灭门仇人 / 救命恩人 / 恩情在身 | Blood Feud / Destroyer of Our Sect / Savior / Owes Us a Debt | relation tag | |
| 至交 / 信赖 / 亲密 / 友好 / 中立 / 冷漠 / 冷淡 / 敌对 / 死敌 | Close Friends / Trusted / Close / Friendly / Neutral / Cold / Cold / Hostile / Sworn Enemy | affinity tier | |
| 协议 / 同盟 / 休战 / 进贡 / 臣服 / 附庸 / 宗主 | Agreement / Alliance / Truce / Tribute / Vassalage / Vassal / overlord | diplomacy | |
| 委托 | Commission | diplomacy | 斡旋 Mediate, 剿匪 Suppress Bandits, 营救 Rescue, 护送 Escort, 猎杀魔头 Hunt a Demon, 协防 Joint Defense |
| 求学 / 镇派绝学 / 弟子客座 | Study / Signature Art / Guest Disciples | diplomacy | |
| 要人 / 人质 / 勒索 / 招降 | Notable / Hostage / Ransom / Recruit | captives | |
| 正邪 | Alignment | | 偏正 Shifts Righteous, 偏邪 Shifts Unorthodox, 纯恶 Pure Evil |
| 旬 | ten-day | time | "This ten-day 0/1" |
| 名义好感 | Listed Affinity | | |
| 图谱:X | Blueprint: X | item | |
| new buildings | 美人靠 Railing Bench, 花罩 Carved Arch, 连廊 Covered Walkway, 飞廊 Sky Bridge, 隔断 Partition, 门派山门 Grand Sect Gate, 垂花门 Inner Courtyard Gate, 月洞门 Moon Gate, 影壁 Screen Wall, 华表 Huabiao Column, 攒尖顶 Pyramid Roof, 高夯土墙 Tall Basic Wall | building | functional names |
| 当前为{0}层视图，X | Floor {0} view: X | build error | |
| character creator colors | traditional color names turned into plain English color names (朱红 Vermilion, 月白 Moon White, 藏蓝 Navy Blue...) | UI | |
| techs 203/205/705/706/502/602/703/802/909 | unlock lists updated in row_overrides.json | tech | the patch added new parts to them |

## 2026-11-20 trait effect line fixes (user OK)
- Shared trait templates reworded so every buff using them reads cleanly: "...for {N}s (max stacks {N}). Cooldown {N}s." (no more "up to 1 stacks"); "Fires a Hidden Weapon forward, dealing X of Min Attack as Y".
- Per-row literal lines in row_overrides.json (DT_CommonBuff FormatDescribe.TextMain): Training_Blue_016 Frenzied Assault, Purple_010 Rend, Purple_016 A Drifting Duckweed, Purple_020 Hunter-Killer, Orange_004 Thought Flash, Orange_014 Baleful, Orange_027 Kongtong Seal (their params don't fit the shared template).
- Practice rooms Room_NeiGongExp/LightSkillExp/SpearExp_1-3: {Exp} param overridden to Internal Art Exp / Lightness Skill Exp / Spear Art Exp (game bug said Ranged Art Exp).
- 讨厌家务 Hates Housework: "...Won't haul or do chores."; 怕火 Afraid of Fire: "...Won't cook or fight fires."

## 2026-11-20 WUXIA pass (user: the game is 100% Wuxia, not Xianxia)
| Chinese | English | Notes |
|---|---|---|
| 星棱 / 星能 | Star Crystal / Star Energy | user choice (was Spirit Crystal / Spirit Energy) |
| 修炼 / 修行 | Training (Training Exp, Training Room, Training Speed) | was Cultivation; 修仙 jokes keep "cultivating immortality" |
| 修为 | Training Progress (stat); "martial attainment" in prose | was Cultivation |
| 魔头 / 猎魔 / 伐魔 | Fiend (Hunt a Fiend, Fiend Hunts) | was Demon; art names (Heavenly Demon Skill), 魔教 Demonic Cult and Demon Seed stay |
| 灵气 | qi | was spiritual/spirit qi; 灵气微溢 Qi Overflow |
| 灵粟 / 碧螺灵茶 / 灵草 / 灵酒 / 灵物 / 灵灯 / 灵视镜 | Fine Millet / Biluo Tea / rare herbs / fine wine / rare materials / Memorial Lamp / Keen-Sight Lens | no "Spirit" |
| 秘境 | Secret Realm | user: keep |
| 星石养功桩 / 吐纳法 (tech) / 内修 | Star Stone Training Post / Internal Arts Training / Inner Training | |
| attribute pairs with one Chinese name | Base X Damage vs X Damage, Max Health, Max Insight, Max Relaxation, Base Injury Recovery Speed, Max X Health Loss % | row_overrides DT_CharacterAttributeInfo, so nothing reads doubled |
Also 2026-11-20: tutorial task lines got how-to steps (menus Build/Tech/Work/Schedule, info-panel actions); the 33 training items list their real effects (row_overrides DT_InventoryItem); Ginseng/Astragalus/Coconut/wines state their effect; 受气包 trait text = what it gives (Piercing Resistance +8, Happiness -5); debug/test panel text translated too.

## 2026-11-20 in-game round 1 (user's screenshots)

Plain ASCII only (the user: the game doesn't take special characters): · → " - ", … → "...", × → x, ≤/≥ → at most/at least, → → to, dashes → -, ℃ → " degrees", ü → u, circled digits → "1." Only the language picker keeps its own script.

| Chinese | English | Notes |
|---|---|---|
| 设置 | Settings | main menu |
| 主角形象 / 选择难度 / 选择地点 / 选择资源 | Character Appearance / Difficulty / Location / Starting Resources | new-game tabs |
| 人物体型 | Body | only height, skin tone and age change |
| 瞳孔 / 睫毛 / 眉毛 / 眉眼 | Pupil Color / Eyelashes / Eyebrows / Eyes | creator; eyebrow styles drop "Brows" (Bushy, Crescent...) |
| 背景故事 / 故事背景 / 剧本 / 剧本积分 / 剧本选择 | Perks / Perk Points / Choose Perks | user |
| 福神转世 / 凌波微步 (perk only) / 天机泄露 / 父慈子孝 / 古墓派 / 呼朋引伴 / 孤僻一时 / 苦力强 | Lucky Star / Light-Footed / Heaven's Bargain / Happy Family / Master and Apprentice / Natural Leader / Loner / Strong Back | perk text states each effect; the martial art 凌波微步 stays Lingbo Steps (locres key override) |
| 技能详情 | Skills | no "Skill" after life-skill names: Farming, Mining, Cooking... (Farming Exp Bonus) |
| 拳脚/刀剑/远程/枪戟招式经验 | Fist / Sword / Ranged / Spear Exp | |
| 开山裂石 | Rock Splitter | trait and saber move |
| 炉火纯青 (5) / 出神入化 (8) | Refined (5) / Sublime (8) | realm levels, short for the trait button |
| 镇守 / 城市镇守 | Warden / City Warden | |
| 难度 初涉江湖 / 名门正派 / 武林盟主 | Newcomer / Righteous Sect / Alliance Leader | |

Trait names now fit the button (about 15 characters): list in trait_short_names.json. 313 UI labels much longer than the space the official English used were shortened (ui_short_labels.json). Location tooltips name pros and cons (temperature and weather from game data); Luoxia Hollow's new-game copy is an object override because its text key also feeds the world map.

## 2026-11-20 in-game round 2 (user: punchy not literal, Wuxia but instantly clear, no Chinese jokes, gaming abbreviations in tight menus, ONE term everywhere)

| Chinese | English | Notes |
|---|---|---|
| 主角 | your character / Your Character | never "protagonist" |
| 娱乐值 / 娱乐+N | Relaxation | the stat; 娱乐 the menu/activity stays Recreation |
| 心情 (stat) | Happiness | rules, status and trait text; flavor/dialogue may say mood |
| 疲劳值 | Rest | the bar drops as fatigue builds; tea = Rest Recovery Speed |
| 硬功 | Iron Body | was Iron Chi |
| 内劲 | Inner Force | was Inner Strength |
| X招式经验 / X招式伤害系数 | X Move EXP / X Move DMG Mult | X武学经验 stays X Art EXP |
| 经验 | EXP | |
| 健康 (stats) / 攻击 / 防御 / 伤害 (stat names) / 增幅 | HP / ATK / DEF / DMG / Boost | Max HP, Head HP, Min ATK, ATK Speed, Slashing DMG, Piercing Boost; prose keeps "damage" |
| 生育 (organ) | Groin | Groin HP |
| 健康 (trait) | Healthy | row override |
| 基础造型 / 主角形象 / 标准棚光 | Avatar & Portrait / Appearance / Lighting | |
| 开源丹 | Dantian Pill | its text says it opens the Dantian |
| 大锅烩菜 / 家常四喜烩 / 酱烧头道 | One-Pot Stew / Four Joys Stew / Braised Roast (user pick; "Braised Meat" would clash with Soy-Braised Meat) | dish lines now from the real recipe (row overrides) |
| 小还丹 | Lesser Return Pill | pairs with Great Return Pill |
| 龙涎茶 | Ambergris Tea | |
| 青灵竹 / 武当灵泉水 | Green Jade Bamboo / Wudang Spring Water | no "Spirit" |
| perks 凌波微步 / 苦力强 | Light-Footed Sect / Strong-Backed Sect | whole-sect buffs; perk text says "You:" or "Whole sect:" from DT_StoryBackgroundData |

Traits: 85 renamed (jokes/memes replaced by names from each trait's real effect, e.g. 身材好 hips joke -> Deft Hands; 金坷垃 -> Seed Sower; 牛马圣体 tiers -> Diligent / Workhorse / Born to Toil / Workaholic). Trait names fit about 12 characters.

Dishes with a real Chinese dish behind them use its usual English name (user, 2026-11-20): 粥 Congee, 家常四喜烩 Four Joy Meatballs (recipe is raw meat), 宫保禽丁 Kung Pao Chicken, 香蕉饼 Banana Pancake, 桂圆莲子汤 Longan Lotus Seed Soup, 枣泥糕 Red Date Cake, 鱼脍 Sliced Raw Fish, 松子百合酥 Lily Pastry, 甲鱼八珍汤 Softshell Turtle Soup, 烩饼 Braised Flatbread, 酱烧头道 Braised Roast. Made-up or regional names stay descriptive: One-Pot Stew, Soy-Braised Meat, Five-Veg Meat, Six Treasures Stew, Nine-Sauce Pot, Eight Treasures Stew, Netherweed Cake/Pastry, Spring Dew Cake.
幽冥草 = Mugwort (user, 2026-11-20; was Netherweed). User's dish names (2026-11-20, from icon + original description): 大锅烩菜 Big Pot Stew, 炒酱油水 Soy-Braised Meat (any raw meat, not just fish), 五菜香肉 Braised Meat, 山灵八珍烩 Eight-Treasure Rice, 幽草饼 Mugwort Cake, 幽光酥 Savory Pastry, 枣泥糕 Red Date Cake. Kept: 静味六宝烩 Six Treasures Stew, 九汁焖锅 Nine-Sauce Pot, 春露幽光糕 Spring Dew Cake.

## 2026-11-20 in-game round 3
- Skill/manual names fit the tooltip banner (limit about "Wind Sweeps the Fallen Plum"): 76 shortened, e.g. 踏月留香 Moon-Treading Step, 神行百变 Myriad Divine Steps, 五虎断门刀 Five Tigers Saber, 绝学·X = "Ultimate - X" with X short.
- Names: given names start with a space at key level and CharacterNameFormat = {lastname}{firstname}, so names read surname first everywhere ("Tang Yi"). Random given names are pinyin (一 Yi, 火 Huo, 大 Da...); surname 山 Shan.
- 弟子 as the green tag after a speaker = Disciple (singular; key RoleConnectionsConfig_ConnectionsName_28).
- 矮菇 = Mushroom (not Short Mushroom); its text has no colour (the plant's cap is white, the Chinese said yellow).
- Intro buttons: "Rebuild with my disciples' help (start the tutorial)" / "I'll plan the rebuilding myself (skip the tutorial)".
- 2026-11-21: recipe/blueprint books fit the banner; the items themselves got the short names everywhere: Ancient Iron Blade, Warm Core Armor, Whirlblade Greaves, Wind-Riding Boots, Golden Wound Salve, Bone-Deep Salve, Basic Fist Manual, Seven-Star Salve, Piercing Pill, Black Jade Salve, Heavenly King Pill, Guarding Powder, Vajra Pill, Sinew Sutra Rubbing, Cloud Plaque, Hanging Lantern (宫灯 is Palace Lantern), Bell-Drum Tower, Stone Lions, Five-Tier Pagoda, Dragon Plaque, Dragon Pillars.
- 2026-11-21: CharacterNameFormat = {lastname} {firstname}: characters made before the name fix saved their names as plain text without a space.

## 2026-11-21 in-game round 4
- Crop field title = crop + " Field" (key /Farmland; the game joins them in code): Mushroom Field.
- 演武台 Stone Arena, 疗养床 Hospital Bed, 石锅灶台 Stone Stove (stone + logs, no bricks).
- Tech tabs: Sect & Training, Crafts & Mechanisms, Jianghu & World. Tech tree item 安葬 = Graves (row override; the work task stays Burying).
- Decor named for what the icon shows, no "Ornament:/Censer:/Wall Hanging:" prefixes: Galloping/Leaping Horse Scroll, Tiger Head Mount, Swallow Kite, Crane Incense Holder/Stand, Inkstone, Brush Rack, Stack of Books, Brush Rest, Framed Painting, Root Carving, Painting Stand, Longquan Sword Rack, Tableware Set, Plum Porcelain Table Vase, Celadon Vase, Bamboo Porcelain Jar, Leaf Pattern Vase, Celadon Bud Vase, Scroll Jar, Ember Brazier (火盆 stays Brazier), Large Screen, Chu Pattern Screen, Dragon-Phoenix Screen, Silk/Leather Screen Stand, Clay Stove, Crane Skeleton, War Drum, Scholar's Rock, Bamboo Vase, Bonsai, Costume Rack, Curio Cabinet.
- Build menu names drawn at 80%, building tooltip titles at 85% (Lua LAYOUT scale).
