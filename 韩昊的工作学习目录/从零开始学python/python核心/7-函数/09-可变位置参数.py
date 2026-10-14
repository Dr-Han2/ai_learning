"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 定义一个函数，参数是可变参数
def print_args(*args):
    # 打印参数类型
    print(f"参数类型是 {type(args)}")
    print(args)

print_args(1, 2, 3)

def sum_nums(*args):
    """
    遍历可变位置元组
    total = 0
    for num in args:
        total += num
    return total
    """
    total = 0
    for num in args:
        total += num
    return total
print(sum_nums(1, 2, 3,4,5))
print(sum_nums())