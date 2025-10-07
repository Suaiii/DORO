# Doro (项目暂定名)

## 游戏简介

在一个科技高速发展但人情日益冷漠的未来都市，一位刚刚失业、对生活失去方向的主角，与一个拥有神秘能力的奇特生物“Doro”意外相遇。这不仅是一次简单的收留，更是一场在外界压力（如充满戒备的房东王阿姨）和内心挣扎（如对未来的迷茫和商业机会的诱惑）下的双向救赎。玩家的每一个选择都将影响主角的性格、与Doro的关系，并最终决定他们是找到新的生存之道，还是在现实的夹缝中彻底沉沦。

## 核心特色

* **深度分支叙事**: 故事拥有复杂的逻辑分支，玩家在序幕中的不同选择将导向截然不同的“第二天”体验（接纳线 vs 逃离线）。
* **性格参数系统**: 包含利他性、开放性、怀疑度、控制欲等8个维度的性格参数，您的选择会实时塑造主角的内心世界。
* **独特的犹豫/计时机制**: 游戏中的多个关键节点采用限时选择，玩家的“犹豫”本身也会被视为一种选择，触发特殊的剧情（如“纸箱潜伏”）。
* **模块化剧情结构**: 剧本被拆分为序幕（`01_prologue.rpy`）和第二天（`02_day2.rpy`），并拥有一个集中的定义文件（`00_definitions.rpy`），结构清晰，易于扩展。
* **潜在的模拟经营玩法**: 随着Doro能力的揭示，游戏引入了利用能力进行水果保鲜的商业线索，为后续章节的模拟经营玩法埋下伏笔。

## 当前状态

* 项目目前处于早期开发阶段。
* 已完成 **序幕 (Prologue)** 和 **第二天 (Day 2)** 的核心脚本，包含完整的剧情分支、数值系统和计时选择机制。
* 美术资源（背景、立绘、UI）目前使用占位符，待填充。

## 如何运行

1.  下载并安装最新版本的 [Ren'Py SDK](https://www.renpy.org/)。
2.  将本项目文件夹放置于Ren'Py SDK解压后生成的`projects`目录中。
3.  启动Ren'Py SDK，在项目列表中选择“Doro”。
4.  点击“Launch Project”即可运行。

## 项目文件结构

为了便于管理，项目脚本已拆分为以下文件：

* `game/00_definitions.rpy`: 包含所有的屏幕(screen)、角色(define)、图像(image)和变量(default)定义。是项目的“大脑”。
* `game/01_prologue.rpy`: 包含完整的序幕剧情（从S1到S4/S3e）。
* `game/02_day2.rpy`: 包含第二天（T5、T6节点）的剧情。

## 所需美术资源清单 (Checklist)

### 背景 (Backgrounds)
- [x] `bg_living_room_dim.jpg` (主角昏暗的客厅)
- [x] `bg_corridor_peephole.png` (猫眼视角下的走廊)
- [x] `bg_corridor_normal.jpg` (正常视角的走廊)
- [x] `bg_box_pov.png` (纸箱窥视视角的遮罩图层)
- [x] `bg_downstairs_trash_area.jpg` (楼下垃圾桶区域)

### 角色立绘 (Character Sprites)
- **Doro**
    - [x] `doro_injured_curled.png` (受伤蜷缩)
    - [x] `doro_hiding.png` (在阴影中躲藏)
    - [x] `doro_calm_indoors.png` (在室内安静的样子)
    - [x] `doro_in_trashcan.png` (在垃圾桶里的特殊差分)
- **王阿姨 (Wang Ayi)**
    - [x] `wang_ayi_impatient.png` (不耐烦的样子)
    - [x] `wang_ayi_angry.png` (愤怒的差分)

### UI与关键物象 (UI & Key Objects)
- [x] `ui_phone_call.png` (手机通话界面)
- [ ] `fx_police_light.png` (警灯光效图层)
- [x] `ui_computer_search.png` (电脑搜索结果界面)
- [x] `prop_oranges_sorted.png` (好、软、烂三堆橘子)
- [x] `prop_experiment_tray.png` (摆满实验品的托盘)
