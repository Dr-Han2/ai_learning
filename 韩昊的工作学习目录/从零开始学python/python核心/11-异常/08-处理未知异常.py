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
except ZeroDivisionError:
    print("出现异常：除数不能为零")
except ValueError:
    print("出现异常：请输入一个数字")
except Exception:  # 所有的异常都是从Exception类中继承来的
    print("出现未知异常")
