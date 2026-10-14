"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#定义一个函数 参数是可变关键字参数
def print_info(**kwargs):
    print(f"参数类型:{type(kwargs)}")
    print(kwargs)
#调用
print_info(name="张三",age=18,gender="man",height=180)
print_info(name="张三", age=18, weigth=80, height=180)
print_info()
#都是在字典中
