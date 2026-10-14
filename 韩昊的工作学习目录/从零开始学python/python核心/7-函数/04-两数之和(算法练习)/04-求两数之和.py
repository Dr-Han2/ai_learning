"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
def add_num(num1,num2):
    """
    对两数求和
    :param num1:第一个运算数
    :param num2:第二个运算数
    :return:两个数的和
    """
    result = num1 + num2
    return result

#result1 = add_num(1,2)
#print(result1)
#也可接收用户输入
num1 = int(input("请输入第一个数"))
num2 = int(input("请输入第二个数"))

result2 =add_num(num1,num2)
print(result2)