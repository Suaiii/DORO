

# -- 节点 S1｜通话与碎响 --
label s1_call:
    scene bg living room dim
    narrator "我掰开啤酒拉环，铝片发出轻微的嘶声，仿佛为这一天的疲惫画上句点。"
    show ui phone call at center with dissolve
    narrator "手机屏幕亮起，拨号的嘟嘟声让我有些恍惚。似乎，但凡需要多费口舌解释的事情，最后都难免变成一场误会。"
    "妈" "到家了？"
    p "到了。最近换了工作节奏，自己出来做事……会更忙些，但，是我自己选的。"
    narrator "我说到“自己选的”时稍微停顿，像把一枚硬币按死在桌上，生怕它再次摇摆不定。"
    narrator "电视屏幕底部滚过两条白色的促销信息：“上层区夜间促销｜Gene-Pet 限量”。那些文字像针一样，把遥远城市的浮华刺在这面墙壁上。"
    "爸" "忙点好，但也别累着。你妈晒了橘子干，说让你舅带过去。"
    p "别麻烦了，你们留着吃。"
    narrator "我把拉环摆正，下意识地在桌上找了个直角对齐。"
    p "家里橘子田今年怎么样？雨水还多么？收果子的贩子有没有压价？"
    "妈" "果子结得多，就是包装箱涨价了。"
    p "那就不急着卖，别亏本。等我这边稳定点，接到大项目，年底就回去多住几天。"
    narrator "电话那头沉默了一会儿，那短暂的空白柔软得像一堵墙。我只好又补了一句："
    p "我这儿真的挺好。"
    hide ui phone call with dissolve
    play sound "sfx/glass_break.ogg"
    narrator "——就在这时，走廊传来一声脆响，像是厚玻璃被瞬间拧爆的声音。"
    narrator "紧接着，蓝红交错的光从门缝底下渗进来，在地板上飞快地扫过。谈话戛然而止，现实闯了进来。"
    jump s2_peephole

# -- 节点 S2｜猫眼初看＋总计时 --
label s2_peephole:
    scene bg corridor peephole
    narrator "透过猫眼，外面的世界被压缩成一个扭曲的鱼眼镜头。玻璃碎片像炸开的鳞片散落一地，一道明显的金属刮痕从中心延伸，最终消失在阴影里。"
    narrator "最近的一块碎片边缘，挂着一滴浅蓝色的液体，圆润得有些不真实。"
    narrator "我屏住呼吸，心跳声清晰地将恐惧分割成一段一段。"
    
    menu:
        "〔S2-A｜寻源靠近〕开门，沿着刮痕走向阴影处":
            $ openness += 1
            $ closedness -= 1
            $ respect += 1
            jump s3b_close_encounter
        "〔S2-B｜警惕守候〕不开门，留在门后观察":
            $ suspicion += 1
            $ control += 1
            jump s2_event_trigger
        "〔S2-C｜装作不见〕关灯退回卧室，不介入":
            $ closedness += 1
            $ egoism += 1
            jump s3c_prime_knocking

# S2 事件触发：王阿姨喝斥
label s2_event_trigger:
    scene bg corridor normal
    show wang ayi impatient at center
    a "哎！谁家的——快走！别在这儿待着！"
    narrator "钥匙串在她手里叮当作响。她的脚步声逼近，停在碎玻璃旁边；又是一声呵斥，风从半开的窗户灌进来，吹动了几粒碎屑。"
    hide wang ayi impatient
    narrator "我贴在门后，掌心能感觉到门板冰冷的木纹——这触感提醒着我一个事实：我的犹豫，本身就是一种参与。"
    narrator "片刻后，脚步声远去，回声在楼梯井里渐渐消散。"
    menu:
        "〔S2-R1｜趁静开门〕":
            jump s3b_close_encounter
        "〔S2-R2｜仍不开门〕":
            jump s3c_knocking

# -- 节点 S3b｜近距初遇·伤口 --
label s3b_close_encounter:
    scene bg corridor normal
    show doro injured curled at center
    narrator "它蜷缩在阴影里，那圈浅蓝色的痕迹在体温下微微发亮。它没有后退，只是把自己缩得更紧，仿佛这样就能把疼痛攥在手里。"
    narrator "我蹲下身，啤酒瓶口在指间有些打滑。"
    p "别动……我看看。"
    narrator "允许靠近，本身就是一种冒险。因为它会逼着我，更真实地面对自己。"
    narrator "楼道里的时间被各种声音切碎：远处一扇门关上，楼梯扶手轻微震动，风穿过走廊。如果我再不做决定，世界就会替我决定。"
    $ s3b_choices = [
        ("先进来，我给你处理一下。", "accept"),
        ("抱歉，我帮不了你。", "reject")
    ]
    show expression Solid("#c276c7", xsize=400, ysize=50) as test_block at top, test_shrinking_transform(5.0)
    call screen multi_choice_timed_screen(choices=s3b_choices, timeout_seconds=5.0)


    # 使用我们刚刚定义的标签 "test_block" 来隐藏它
    hide test_block
    $ result = _return
    if result == "accept":
        $ altruism += 1; 
        $ openness += 1; 
        $ respect += 1; 
        $ trust += 1; 
        $ suspicion -= 1
        jump s4_acceptance
    elif result == "reject":
        $ closedness += 1; 
        $ egoism += 1; 
        $ trust -= 1
        jump s3e_escape
    elif result == "timeout":
        jump s3x_box_hideout

# -- 节点 S3x｜纸箱潜伏 (已更新返回值判断逻辑) --
label s3x_box_hideout:
    scene bg corridor normal
    narrator "思考得太久了。"
    narrator "脚步声正在靠近，我不知道一个欠着房贷、浑身酒气的男人，和一个来路不明的生物一起被发现，会是什么后果。"
    narrator "但我知道，我承担不起。"
    p "有了。"
    narrator "我把门口的快递纸箱拖到脚边，用指甲划开封口胶带，撕啦一声，一个藏身之处出现了。"
    narrator "纸板带着潮气，像一块可以折叠的黑暗。我在上面抠出两个洞，刚好够眼睛往外看。"
    narrator "箱内的空气带着纸浆的酸甜味，让我想起小时候躲在衣柜里的那次，心跳得像在敲鼓。"
    
    show bg corridor normal
    show wang ayi impatient at approach_from_distance
    show fg box lo
    narrator "透过孔洞，王阿姨的影子先出现，钥匙串叮当作响。她压低声音，连连挥手，像在驱赶一只误入“公共秩序”的小动物。"
    narrator "“它”紧贴着墙，轻轻缩了一下，呼吸的末尾带着微不可查的颤抖。"
    
    p "（躲起来，是因为害怕被看见；偷偷地看，又是渴望被接纳。人心，真是矛盾的深渊。）"
    narrator "你很清楚，至少不能让“它”被发现。"
    show expression Solid("#c276c7", xsize=400, ysize=50) as test_block at top, test_shrinking_transform(7.0)
    call screen box_excuses_screen
    
    $ excuse_choice = _return

    # 【核心改动】现在我们判断 'observe' 和 'timeout_observe' 两种情况
    if excuse_choice == "observe" or excuse_choice == "timeout_observe":
        

        # 在这里用一个简单的 if 判断来显示不同的文本
        if excuse_choice == "timeout_observe":
            # 这是超时的情况
            narrator "面对众多荒唐的借口，你最终选择了沉默。时间在流逝，王阿姨也渐渐远去。"
        else:
            # 这是手动点击的情况
            narrator "你决定保持静默，等待王阿姨声音渐远。"
        
        narrator "环顾四周，我失去了“它”的踪迹"
        menu:
            "回屋":
                jump s3e_escape


    elif excuse_choice == "drunk":
        # 【核心改动】这是现在唯一正确的选项
        hide fg box lo
        narrator "我让箱子倒下，木地板发出咚的一声闷响。"
        narrator "我用带着酒气的声音拖长语调：“哎……我这……掉……掉箱子里了。”让脚步显得虚浮，手扶着墙，直线走回屋里。"
        $ openness += 1; 
        $ suspicion -= 1; 
        $ control += 1
        narrator "王阿姨狐疑地看了我一眼，但最终还是因为嫌弃酒气而转身离开。"
        jump search_for_doro_after_excuse # 跳转到脱险后寻找Doro的新剧情
    elif excuse_choice == "camouflage":
        jump bad_end_eviction
    elif excuse_choice == "acoustic":
        jump bad_end_misunderstanding
    elif excuse_choice == "art":
        jump bad_end_exile
    elif excuse_choice == "cat":
        jump bad_end_trauma


# 【新增标签】用于连接装醉脱险和最终接纳
label search_for_doro_after_excuse:
    scene bg living room dim
    narrator "我关上门，背靠在门板上，长出了一口气。酒味和谎言的味道混杂在空气里，但总算是把王阿姨应付过去了。"
    p "（刚才……我保护了它？）"
    narrator "这个念头一闪而过，我立刻走到门口，小心翼翼地再次打开门缝向外望去。"
    
    scene bg corridor normal
    narrator "走廊里空荡荡的，只有风声和远处传来的电视声。刚才那个小家伙已经不见了。"
    p "（走了吗……也好，这里对它来说太危险了。）"
    narrator "我正准备关门，却看到阴影的尽头，有一小团轮廓动了一下。"
    
    show doro hiding at center with dissolve
    narrator "是它。它没有离开，只是躲在了更远的地方，似乎在等我。"
    narrator "我们的目光在昏暗的走廊里相遇。这一次，它的眼神里少了一丝恐惧，多了一些别的东西——或许是……确认？"
    
    # 在这里，玩家的主动保护行为最终导向了“接纳”的真结局
    jump s4_acceptance




# -- 节点 S3c｜敲门序列 --
label s3c_knocking:
    scene bg living room dim
    narrator "不开门，世界就会用自己的方式开始敲门。"
    narrator "“咚……咚。”声音先是从走廊尽头响起，停顿片刻，又移到更近的门前，像是在练习礼貌。最后，它停在了我的门外。“咚。”，这一声，像是把我的名字轻轻敲在了门板背面。"
    p "又是这样。先是退缩，然后竖起耳朵倾听，心里默念着“快走吧，别来烦我”。我总渴望一个能让我独自清静的世界，但又隐隐害怕……如果这个世界真的不再需要我了，我又该去哪里呢？"
    menu:
        "〔此刻接纳〕解开门链，让它进来":
            $ trust += 1; 
            $ openness += 1; 
            $ respect += 1; 
            $ suspicion -= 1
            $ blue_dot_evidence = True
            jump s4_acceptance
        "〔仍不开门〕维持沉默，装作无人在家":
            $ closedness += 1; 
            $ egoism += 1
            jump s3e_escape

# -- 节点 S3c’｜敲门序列·我装作不见 --
label s3c_prime_knocking:
    scene bg living room dim
    narrator "黑暗让屋子变得更小，仿佛把我塞回了某个更久远的沉默里。"
    narrator "“咚……咚。”声音先是从走廊尽头响起，停顿片刻，又移到更近的门前，像是在练习礼貌。最后，它停在了我的门外。“咚。”，这一声，像是把我的名字轻轻敲在了门板背面。"
    p "又是这样。先是退缩，然后竖起耳朵倾听，心里默念着“快走吧，别来烦我”。我总渴望一个能让我独自清静的世界，但又隐隐害怕……如果这个世界真的不再需要我了，我又该去哪里呢？"
    menu:
        "〔起身接纳〕我最终起身开门":
            $ trust += 1; 
            $ openness += 1; 
            $ respect += 1; 
            $ suspicion -= 1
            $ blue_dot_evidence = True
            jump s4_acceptance
        "〔装作不见到底〕不应声，不开门":
            $ closedness += 1; 
            $ egoism += 1
            jump s3e_escape

# -- 节点 S3e｜逃离 --
label s3e_escape:
    scene bg corridor normal
    narrator "更冷的风卷起碎屑。一小团影子跃上窗台，一缩一纵，隐入外侧铁梯，留下一声金属轻响。"
    narrator "夜色恢复平静，仿佛什么都不曾发生。"
    p "（只有我心里留下了一张空椅子，它不断邀请我坐下，却让我穿透椅背。）"
    if blue_dot_evidence:
        narrator "（门口的地面上，留下了一小点不该存在的蓝色。）"
    else:
        narrator "（地面干净，谁都没有来过。）"
    jump s3f_night_search

# -- 节点 S4｜接纳·入内 --
label s4_acceptance:
    scene bg living room dim
    show doro hiding at center
    narrator "我“们”回到了房间里"
    narrator "它先蹲在门边的影子里，耳尖微微颤动，对屋里的一切都保持警惕。"
    narrator "我打开电脑，搜索栏里输入最日常的词句：“基因宠物 受伤 处理 / 止血 消毒 / 伤口 护理”。"
    narrator "页面返回了标准答案、门店广告和用户心得。“新品外形特征”的光泽，与眼前这个沉默的小家伙重叠——认知闭合了：这是最新的Gene-Pet，可能走失了。这种结论带来了秩序，也带来了盲点。"
    p "我不会伤害你，先把伤口处理完。"
    narrator "我把声音放轻，像在调试一段音乐的音量。它的呼吸在纱布旁逐渐平稳，目光从警惕变为专注，落回到我手上。"
    p "（人真是奇怪的动物。一边抱怨着麻烦，一边又忍不住想把所有破碎的东西都拼凑起来。也许我害怕的不是失败，而是害怕这个世界上，再也没有什么东西需要我来修补。）"
    show ui computer search at center with dissolve
    p "..."
    p "这是..."
    narrator "侧栏广告反复强调“低致敏 / 到店护理”，一条问答写道：“少数型号体液呈蓝色，属正常参数范围，不必惊慌。”"
    hide ui computer search with dissolve
    if blue_dot_evidence:
        narrator "你本该想到的。门口的地面上，还留着那一点不该存在的蓝色。"
    else:
        narrator "你看着干净的门槛，那条信息只在你心里回响。"
    narrator "有时候，我们总是先认定了事实，然后才去寻找理解它的方式。"
    "（序幕结束）"
    jump t5a_oranges_indoors

# -- 节点 S3f｜夜半检索·未接纳 --
label s3f_night_search:
    scene bg living room dim
    narrator "我被若有似无的敲门声惊醒，仔细听却又消失不见。"
    narrator "但我想起了什么，起身开机，输入：“基因宠物 受伤 处理 / 止血 消毒 / 伤口 护理 方法 / 上门 兽医 / 蓝色 体液”"
    show ui computer search at center with dissolve
    narrator "侧栏广告反复强调“低致敏 / 到店护理”，一条问答写道：“少数型号体液呈蓝色，属正常参数范围，不必惊慌。”"
    hide ui computer search with dissolve
    narrator "我盯着这句话，再看向门口——如果那里有一小点蓝，是世界在回应我；如果什么也没有，那信息就只在我心里。认定，往往先于理解。"
    "（序幕结束）"
    jump t5b_oranges_outdoors

# -- 全新的坏结局 --
label bad_end_eviction:
    hide fg box lo
    narrator "我让箱子倒下，清了清嗓子，用一种学者的口吻对王阿姨说："
    p "（严肃地）我在进行一项城市环境拟态适应性的社会学研究。"
    narrator "王阿姨愣住了几秒，然后眼神从困惑变成了警惕和厌恶。"
    a "研究？我看你是在搞什么见不得人的偷窥勾当吧！神经病！"
    narrator "她掏出手机，直接拨通了物业保安的电话。半小时后，你因“行为异常，骚扰邻里”被要求立刻搬离。"
    narrator "你提着行李箱站在深夜的街头，成了自己研究的第一个失败样本。"
    "（结局：被驱逐的社会学家）"
    return

label bad_end_misunderstanding:
    hide fg box lo
    narrator "我让箱子倒下，故作高深地对她说："
    p "（神秘地）我在测试走廊的声波共振特性，纸箱是最好的共鸣腔。"
    narrator "王阿姨听到“共振”“腔”之类的词，脸色瞬间变得惨白。她想起新闻里那些用日常物品制造危险品的报道。"
    a "你...你离我远点！你要干什么！"
    narrator "她惊恐地尖叫着跑上楼，很快，整栋楼都被警灯的蓝红色光芒笼罩。"
    narrator "你因为“涉嫌制造不明危险装置，危害公共安全”的罪名被带走调查。尽管最后被澄清，但你再也无法在这里住下去了。"
    "（结局：被误解的科学家）"
    return

label bad_end_exile:
    hide fg box lo
    narrator "我让箱子倒下，摆出一个自认为充满艺术感的姿势。"
    p "（艺术地）这是我的行为艺术作品，主题是‘被投递的孤独’。"
    narrator "王阿姨沉默地看了你很久，眼神里没有愤怒，只有一种看透一切的疲惫。"
    a "小伙子，别跟我来这套。我不管你是孤独还是空虚，这是我的房子，不是你的舞台。"
    narrator "第二天，你的门上就贴了“租赁合同终止通知书”。"
    narrator "你的行为艺术以被房东“退货”而告终。"
    "（结局：被退货的艺术家）"
    return

label bad_end_trauma:
    hide fg box lo
    narrator "我让箱子倒下，然后用一种天真的语气说："
    p "（无辜地）我在模仿猫的行为，试图从它们的视角理解这个世界。"
    narrator "“猫”这个词像一把钥匙，瞬间打开了王阿姨最黑暗的记忆闸门。她想起了儿子小明，想起了那只“温顺”的基因宠物。"
    a "怪物...你们都是怪物！小明！我的小明！"
    narrator "她歇斯底里地尖叫起来，声音里充满了无法承受的痛苦和恐惧，引来了所有邻居的围观。"
    narrator "在众人的指指点点中，你被当成了一个引人发病的疯子。你试图解释，但没人想听一个在楼道里学猫叫的人说话。"
    "（结局：引爆创伤的模仿者）"
    return