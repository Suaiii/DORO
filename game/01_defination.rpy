transform test_shrinking_transform(time):
    # 初始状态
    xsize 400
    # 动画，使用传入的 time 变量作为时长
    linear time xsize 0

# 2. 使用经过验证的“画中画”逻辑来构建你的选择屏幕
screen multi_choice_timed_screen(choices, timeout_seconds=5.0):
    modal True

    # 逻辑计时器 (不变)
    timer timeout_seconds action Return('timeout')

    # 选项按钮 (不变)
    # 将原来的 vbox 用一个 frame 包裹起来
    frame:
        xalign 0.5
        yalign 0.5

        # 1. 给整个背景框一个固定的宽度，让它看起来更像一个菜单窗口
        xsize 600
        background "#00000088"
        padding (30, 20)

        vbox:
            xalign 0.5
            # 2. 增大按钮之间的垂直间距
            spacing 25

            for text, value in choices:
                textbutton text:
                    # 3. 给按钮设置一个最小宽度，让它们看起来整齐划一
                    xminimum 350
                    
                    # 其他样式保持不变
                    text_color "#ffffff"
                    text_hover_color "#00ddff"
                    action Return(value)



# Screen 2: 你的第二个屏幕也可以用同样的方式添加进度条
# 这里为了简洁，仅作示意，你可以将上面 bar 的代码复制到你的 box_excuses_screen 中
screen box_excuses_screen(timeout_seconds=7.0):
    modal True
    timer timeout_seconds action Return('timeout_observe')

    # 将原来的 vbox 用一个 frame 包裹起来
    frame:
        xalign 0.5
        yalign 0.5

        # 1. 给整个背景框一个固定的宽度，让它看起来更像一个菜单窗口
        xsize 600
        background "#00000088"
        padding (30, 20)

        
    vbox:
        xalign 0.5 yalign 0.5 spacing 15
        textbutton "〔伺机观察〕" action Return("observe") text_color "#ffffff" text_hover_color "#00ddff"
        textbutton "（装醉）哎……我这……掉……掉箱子里了。" action Return("drunk") text_color "#ffffff" text_hover_color "#00ddff"
        textbutton "（严肃地）我在进行一项城市环境拟态适应性的社会学研究。" action Return("camouflage") text_color "#ffffff" text_hover_color "#00ddff"
        textbutton "（神秘地）我在测试走廊的声波共振特性，纸箱是最好的共鸣腔。" action Return("acoustic") text_color "#ffffff" text_hover_color "#00ddff"
        textbutton "（艺术地）这是我的行为艺术作品，主题是‘被投递的孤独’。" action Return("art") text_color "#ffffff" text_hover_color "#00ddff"
        textbutton "（无辜地）我在模仿猫的行为，试图从它们的视角理解这个世界。" action Return("cat") text_color "#ffffff" text_hover_color "#00ddff"

# -- 图像定义之后 --

# 定义一个名为 "approach_from_distance" 的可复用动画
transform approach_from_distance(start_zoom=0.4, start_y=0.6, duration=2.5):
    # 动画的初始状态
    zoom start_zoom
    yalign start_y
    xalign 0.5

    # 动画过程
    # linear duration zoom 1.0 yalign 1.0
    # 上面这句也可以，但 ease 会让效果更平滑
    ease duration zoom 1.0 yalign 1.0



define p = Character("我")
define narrator = Character(None, kind=p)
define a = Character("王阿姨", color="#f0e68c")

# -- 图像定义 (Art Assets Placeholders) --
image bg living room dim = "images/bg_living_room_dim.jpg"
image bg corridor peephole = "images/bg_corridor_peephole.jpg"
image bg corridor normal = "images/bg_corridor_normal.jpg"
image bg box pov = "images/bg_box_pov.jpg"
image doro injured curled = "images/doro_injured_curled.png"
image doro hiding = "images/doro_hiding.png"
image doro calm indoors = "images/doro_calm_indoors.png"
image wang ayi impatient = "images/wang_ayi_impatient.png"
image wang ayi angry = "images/wang_ayi_angry.png"
image ui phone call = "images/ui_phone_call.png"
image fx police light = "images/fx_police_light.jpg"
image ui computer search = "images/ui_computer_search.png"
image bg corridor empty = "images/corridor_1.jpg"
image fg box lo = "images/box.png"


# 一、 性格/态度参数 (Personality/Attitude Parameters)
default altruism = 0                # 利他性
default openness = 0                # 开放性
default suspicion = 0               # 怀疑度
default closedness = 0              # 封闭性
default control = 0                 # 控制欲
default egoism = 0                  # 利己性
default respect = 0                 # 尊重度
default trust = 0                   # 信任度

# 二、 关键剧情标记 (Key Plot Flags)
default blue_dot_evidence = False      # 蓝点证据
default clue_safe_startup = False      # 稳妥创业线索
default clue_high_risk_business = False  # 高风险商业线索

# 三、 机制与状态变量 (Mechanic & State Variables)
default player_initial_approach = "neutral"  # 初始接触方式 ("friendly", "hesitant", "cold")
default doro_initial_trust = "neutral"     # Dora初始信任度 ("neutral", "wary")
default orange_request_count = 0     # 橘子请求次数