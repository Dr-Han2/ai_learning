"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#1.定义一个函数 可实现两个数的加减乘除
#2.接收用户的输入(两个运算数)
#3.函数体中根据用户输入的运算符号,进行运算

def calculator(num1, opt, num2):
    """
    实现两个数的运算 加、减、乘、除
    :param num1: 数1
    :param opt: 符号
    :param num2: 数2
    :return:
    """
    if opt == "+":
        return num1 + num2
    elif opt == "-":
        return num1 - num2
    elif opt == "*":
        return num1 * num2
    elif opt == "/":
        return
    elif opt == "%":
        return num1 % num2
    else:
        return ("运算符错误")

result =calculator(10,"*", 5)
print(result)