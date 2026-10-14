"""
@Author  : 韩昊
@Company : *********
@Date    :
@Desc    :
@Version : 1.0
"""
#先定义一个列表
goods = ["电脑", "手机", "平板"]
# in / notin
if "手机" in goods:
    print("手机在goods中")
else:
    print("手机不在goods中")

print(f"手机在列表中:{"手机" in goods}")
#下标 \
print(f"手机的下标是{goods.index("手机")}")  #1