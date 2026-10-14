"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
while True:
    try:
        num1 = float(input("请输入第一个数字："))
        num2 = float(input("请输入第二个数字："))
        print(f"{num1} / {num2} = {num1 / num2}")
    except ZeroDivisionError:
        print("出现异常：除数不能为零")