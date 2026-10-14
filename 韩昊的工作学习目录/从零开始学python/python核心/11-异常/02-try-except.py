"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
try:
    num1 = float(input("请输入第一个数"))
    num2 = float(input("请输入第二个数"))
    print(f"{num1} / {num2}={num1/num2}")
except:
    print("输入有误,请重新输入")
    print("除数不能为0")

print("程序结束")

