"""
@Author  : 韩昊
@Company : *********
@Date    :
@Desc    :
@Version : 1.0
"""

# 每循环一次问一下用户是否需要退出
# 定义一个退出条件
flag = True
count = 1
# 开始循环
while flag:
    print(f"这是第{count}次循环..")
    # 接收用户的输入，如果输入y，继续循环，否则退出
    user_input = input("是否继续：y(继续)")
    if user_input == "y":
        # 更新退出条件
        # flag = False
        break    # 后面的语句都不执行, 退出整个循环体，整个循环结束
        # continue # 后面的语句都不执行, 重新开始新一轮的循环，并不会退出整个循环体
    # 更新记数
    count += 1

print(f"一共执行了{count}次循环")