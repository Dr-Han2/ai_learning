"""
@Author  : 韩昊
@Company : *********
@Date    :
@Desc    :
@Version : 1.0
"""

# 1. 接收用户的输入年龄和是否有身份证
age = int(input("请输入你的年龄："))
# 接收到的是字符串，不论输入的是0还是1转成bool时都是True
has_id = input("请输入是否有身份证：0：没有，1：有")
# 先把输入的0或1转成整型，再转到bool： 1 -> True  0 -> False
has_id = bool(int(has_id))

# 2. 进行条件判断
if age >= 18 and has_id:
    print("可以进入网吧")
else:
    if age < 18 and not has_id:
        print("年龄不满足要求也没有身份证")
    elif age < 18:
        print("年龄不满足要求")
    elif not has_id:
        print("没有身份证")