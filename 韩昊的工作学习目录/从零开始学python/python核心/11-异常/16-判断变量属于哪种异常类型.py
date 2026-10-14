
"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 定义一个除法函数
def div(a, b):
    # 判断a和b 是不是整型
    if not isinstance(a, int): # 返回bool类型
        raise TypeError("a必须是整型")
    if not isinstance(b, (int, float)):
        raise TypeError("b必须是浮点型")
    if b == 0:
        raise ZeroDivisionError("除数不能为0")
    return a / b

#
print(div(10,2))
#print(div(10,0))