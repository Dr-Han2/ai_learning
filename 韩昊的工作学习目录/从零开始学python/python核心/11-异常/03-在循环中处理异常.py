"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""

# 直接处理整个循环
#try:
#    while True:
#        num1 = float(input("请输入第一个数字："))
#        num2 = float(input("请输入第二个数字："))
#        print(f"{num1} / {num2} = {num1 / num2}")
#except:
#    print("输入有误，出现异常")
#print("程序运行结束")

# 在循环内部处理异常
# 出现异常后只是结束了当前的一次循环，不会异常退出循环
while True:
    try:
        num1 = float(input("请输入第一个数字："))
        num2 = float(input("请输入第二个数字："))
        print(f"{num1} / {num2} = {num1 / num2}")
    except:
        print("输入有误，出现异常")
        print("除数不能为零")
