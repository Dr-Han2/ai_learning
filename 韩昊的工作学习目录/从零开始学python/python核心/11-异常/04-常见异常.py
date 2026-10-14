"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 语法异常
# SyntaxError: unterminated string literal (detected at line 9)
# print("hello world)

# 除零错误
# ZeroDivisionError: division by zero
# print(10 / 0)

# 引用一个不存在的变量
# NameError: name 'name' is not defined
# print(name)
# div(a, b)

# 下标引用异常
list1 = [1, 2, 3, 4, 5, 6]
# IndexError: list index out of range
# print(list1[100])  # 访问了一个不存在的下标

# 类型异常
# TypeError: can only concatenate str (not "int") to str
# print("hello" + 18)

# 值异常
# ValueError: invalid literal for int() with base 10: 'abc'
# int("abc")

# KYE不存在的异常
# dict1 = {"name": "张三"}
# KeyError: 'age'
# print(dict1["age"])

# KeyboardInterrupt用户手动中断程序
# 等同于命令行中用户按  ctrl + c

while True:
    pass