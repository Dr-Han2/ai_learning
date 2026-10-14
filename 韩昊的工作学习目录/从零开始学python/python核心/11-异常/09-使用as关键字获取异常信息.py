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
    # ...后续代码中可能出现未知的异常

except ZeroDivisionError as e:
    print(f"异常类型:{type(e)}")
    print(e)
    print("出现异常：除数不能为零")
except ValueError as e:
    print(f"异常类型:{type(e)}")
    print(e)
    print("出现异常,请输入一个数字")
except Exception as e:
    print(f"异常类型:{type(e)}")
    print(e)
    print(f"出现未知异常{e}")
