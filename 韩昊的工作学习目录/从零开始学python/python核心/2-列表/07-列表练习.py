"""
@Author  : 韩昊
@Company : *********
@Date    :
@Desc    :
@Version : 1.0
"""
import random
#
people = ["小明", "小红", "班主任", "校长", "大黄狗", "外卖小哥", "二哈", "胖虎"]
place = ["操场", "垃圾桶旁"]
tool = ["拖鞋", "铅笔"]
action = ["跳科目三", "肚皮舞"]

peole_item = random.choice(people)
place_item = random.choice(place)
tool_item = random.choice(tool)
action_item = random.choice(action)

print(f"{peole_item}在{place_item}用{tool_item}{action_item}")