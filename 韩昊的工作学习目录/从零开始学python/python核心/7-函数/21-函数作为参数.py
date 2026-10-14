"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 函数1：计算两个数的和
def add(num1, num2):
    return num1 + num2

print(type(add))

# 函数2：计算两个数的差
def subtract(num1, num2):
    return num1 - num2

print(type(subtract))

# 定义一个数据处理函数，接收三个参数
# 1. 数据处理函数
# 2. 3. 运算数
def data_process(func, num1, num2):
    print(f"当前执行的函数是：{func.__name__}")
    result = func(num1, num2)
    return result

# 调用
result1 = data_process(add, 10, 5)
print(result1)

result2 = data_process(subtract, 10, 5)
print(result2)