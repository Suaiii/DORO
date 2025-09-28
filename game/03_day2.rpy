

# -- 节点 T5-A｜事件室·橘与腐香（接纳线 Day2） --
label t5a_oranges_indoors:
    scene bg living room dim
    narrator "我睡醒时觉得喉咙很干。门口不知何时放了一个瓦楞纸箱，上面用粗记号笔写着“别太累”。"
    narrator "打开箱子，一股甜中带酸的热气扑面而来——有几个橘子已经从脐部裂开，白色的橘络像没理干净的线头。"
    narrator "我把橘子分成三堆：好的、发软的、腐烂的。分拣时手指被果汁粘住，空气里弥漫开一股淡淡的腐败气味。"
    narrator "我踩开脚踏式垃圾桶，盖子啪一声弹起，扔进烂橘后，那点腐臭味被暂时盖住了。"
    show doro calm indoors at center
    narrator "Dora 在房间里。当她靠近那堆烂橘子时，肩膀极其轻微地起伏了一下，仿佛屏住了呼吸。"
    narrator "等我再转过身时，地上多了一个橘子，它看起来非常干净，像是刚洗过，表皮上的油脂腺点在光下微微发亮。"
    narrator "我剥开它，一股清新的香气驱散了屋里的陈腐味——好像有人悄悄给这个房间换了口气。"
    narrator "我愣了一下，打开电脑，在搜索框里输入：“基因突变 宠物 腐烂 食物 可以 吃 吗”。"
    narrator "网页弹出一些模板化的答案和广告。"
    narrator "身后，垃圾桶的盖子被轻轻碰了一下，金属轴心发出轻微的叮声。"
    narrator "我看向桌面，又看向她。她并没有看我，只是把前爪边的一小片橘皮朝我这边推了推，像是在提交某种证明。"
    narrator "而另一只完好的橘子，已经静静地放在我的手边。"
    
    # 可重复选项循环
    label t5a_orange_request_loop:
        menu:
            "再给我一个橘子。":
                $ orange_request_count += 1
                narrator "Dora的肩膀再次轻微起伏，又一个崭新的橘子出现在你面前。"
                jump t5a_orange_request_loop # 跳回循环

            "〔看向垃圾桶〕" if orange_request_count >= 3:
                narrator " 这太不寻常了，似乎是，“食物复写”"
    
    # 跳出循环后的汇聚选项
    menu:
        "我们做个小试验，好吗？你继续——我数数。":
            $ respect += 1; 
            $ trust += 1; 
            $ openness += 1
            jump t6_replication_experiment
        "先等等。我需要知道这东西真的安全。":
            $ suspicion += 1; 
            $ control += 1; 
            $ respect -= 1
            jump t6_replication_experiment
        "这也许能帮我们活下去。":
            $ altruism += 1; 
            $ openness += 1; 
            $ control += 1
            jump t6_replication_experiment

# -- 节点 T5-B｜楼下垃圾桶·清香反转（逃离线 Day2） --
label t5b_oranges_outdoors:
    scene bg downstairs trash area # 需要新的背景图：楼下垃圾桶区域
    narrator "我捏着鼻子，把几袋烂橘子丢进楼道尽头的公共分类垃圾桶。果皮撞在桶壁上，发出沉闷湿润的声音。"
    narrator "刚走出几步，就听到背后传来一阵轻微而密集的咀嚼声，像是有小剪刀在剪纸。"
    narrator "我停下脚步，回头看去。"
    narrator "垃圾桶盖子内侧的编号“B-07”在灯光下显得有些陈旧。咀嚼声停了，随即又响起来。"
    narrator "我走近，手指搭在桶盖边缘，甚至能听到橘皮油脂腺点被压破时细微的嘶嘶声。"
    narrator "我掀开了桶盖。"
    show doro hiding at center # Dora在垃圾桶里
    narrator "Dora 在里面。她没有看我，专注得像个在暗处啃书的孩子。"
    narrator "那堆烂橘子在她口鼻周围似乎正褪去腐败的气息，空气中升起一股新鲜橘皮的清凉香气。"
    narrator "几瓣橘子在她爪边慢慢“更新”：软烂的表皮被一种细微的光泽抚平，油脂腺点重新变得饱满，如同被熨平的皱纸。"
    narrator "我扶着半开的桶盖，眼睛有些发酸。"
    narrator "旁边的广告灯箱正循环播放着“周末市集·现剥橘子 9.9”的促销信息，那画面甜得有些虚假。"

    menu:
        "跟我回去。我不会说出去，也不会让你待在这里。":
            $ altruism += 1; 
            $ respect += 1; 
            $ trust += 1; 
            $ suspicion -= 1
            jump s4_acceptance
        "等一下——这里有摄像头。我们得避开它。":
            $ control += 1; 
            $ suspicion += 1; 
            $ openness += 1
            narrator "你拉着Dora，小心翼翼地避开了监控探头，回到了公寓。"
            jump s4_acceptance
        "如果你能看着图做出味道，我们或许真的能…试点卖卖？":
            $ openness += 1; 
            $ control += 1; 
            $ altruism += 1
            narrator "一个大胆的想法在你脑中成形。你决定把Dora带回去，这不仅仅是收留，更像是一场赌博的开始。"
            jump s4_acceptance

# -- 节点 T6-R2｜测试台·复写实验 --
label t6_replication_experiment:
    scene bg living room dim
    narrator "傍晚的光线为书桌镀上一层灰金色。我在电脑便签上草草写下几个目标：对比味道、尝试复写其他水果、看看网图能不能当模板。"
    narrator "方法很简单：看、闻、尝，必要时核对一下垃圾桶。"
    narrator "托盘里摆开了阵势：好橘子、烂橘子、柠檬片、面包块，还有一角青椒。Dora 沿着托盘边缘安静地移动。"
    p "（看着她，我心里盘算着该怎么开始。这里，我意识到自己的态度可能会影响整个过程…）"

    menu:
        "我们一起试，你随时可以停。":
            $ respect += 1; 
            $ trust += 1; 
            $ control -= 1
            p "我们一起试，你随时可以停。"
            narrator "我轻声对她说，打算根据她的反应来调整节奏。"
        "我们先按计划逐项完成。":
            $ control += 2; 
            $ suspicion += 1; 
            $ respect -= 1
            p "我们先按计划逐项完成。"
            narrator "我对自已说，试图让流程显得规范有序。"
        "我决定先不催促，只是观察记录，看她自己会怎么做。":
            $ respect += 1; 
            $ openness += 1
            p "..."
            narrator "我决定先不催促，只是观察记录。"

    narrator "Dora 在烂橘子旁停下，呼吸微微变化，那股腐败味随之淡化。一个看起来崭新的橘子出现在托盘上。"
    narrator "我剥开尝了尝，味道清甜圆润，和旁边那个甜得有点“冲”的正常橘子很不一样。"
    p "（接下来，是验证区别，还是直接探索新可能？）"

    menu:
        "我们再试一小瓣，我闭眼和好橘子交替尝，要是我猜错了，你可别笑话我。":
            $ trust += 1; 
            $ openness += 1
        "我们试试别的吧，比如葡萄？我会描述感觉，你按自己的理解来。":
            $ openness += 2; 
            $ respect += 1

    narrator "当我们进行到根据模糊网图复写蓝莓味时，出现了一点误差。Dora 先做出了一种带奶香的味道，不太对劲。"
    p "（面对误差，该如何反应？）"

    menu:
        "这个错误的味道挺有意思，我们顺着这个感觉走走看？":
            $ openness += 2;
            $ trust += 1
        "刚才这个不太对，我们再重新试试？":
            $ control += 1; 
            $ suspicion += 1

    narrator "实验一次次重复，当我第六次准备请求时，注意到 Dora 的动作明显慢了下来，甚至把头偏向一边。"
    p "（她是需要休息了。这时我该…）"

    menu:
        "先休息一下吧。我们都需要喘口气。":
            $ respect += 2; 
            $ trust += 1; 
            $ control -= 1
            p "先休息一下吧。"
            narrator "我放下笔，也感到有些疲惫。"
        "再坚持三次就好。":
            $ control += 2; 
            $ respect -= 1
            p "再坚持三次就好。"
            narrator "我的语气不自觉地带上了一点催促，说完自己也觉得有点过分。"

    narrator "在整个过程中，我始终记得不去拍摄她，只在便签上记录关键词。"
    p "（而对于这能力的潜在用途，一个念头冒了出来…）"
    
    menu:
        "也许以后可以先让朋友尝尝，听听反馈再想下一步。":
            $ trust += 1; 
            $ altruism += 1
            $ clue_safe_startup = True
        "如果能按接单，也许可以挣到快钱…":
            $ control += 1; 
            $ openness += 1
            $ clue_high_risk_business = True
            narrator "这个想法让我有些兴奋，但随即提醒自己细节必须透明。"

    narrator "最后，当一轮测试顺利结束时，我看着安静的 Dora。"

    
    menu:
        "〔轻触〕辛苦了。":
            $ trust += 1; 
            $ respect += 1
            p "辛苦了。"
            narrator "我伸出手，轻轻碰了碰她的肩膀，表示谢意。"
        "〔保持距离〕做得很好。":
            p "做得很好。"
            narrator "我站在原地，只是口头肯定，保持着一点距离。"

    narrator "实验便签的角落，我画下了一个简单的能量条。看来，要维持这种合作，换口味和适时休息与测试本身同样重要。"

    # 故事在此暂告一段落
    "（第二日 结束）"
    return