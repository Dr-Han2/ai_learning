"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
try:
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))
    print(f"{num1} / {num2} = {num1 / num2}")
except (ZeroDivisionError, ValueError):  # 使用元组进行多个异常的指定
    print("出现异常：除数不能为零或输入不合法，请检查")