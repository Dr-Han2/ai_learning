"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
def print_info(name,age=18,gender="未知",*args,**kwargs):
    print(f"姓名:{name}, 年龄: {age}, 性别: {gender}")
    print(f"可变位置参数:{args}")
    print(f"可变关键字参数{kwargs}")
    print(f"可变位置参数的类型是{type(args)}")
    print(f"可变关键字参数的类型是{type(kwargs)}")

print_info("张三",18)
#传入多个参数
print_info("张三", 18, "man", 80, 90 , 100, height=175, weight=70)

#多种参数型混合定义函数
def print_info1(name,age=18,gender="man",*, height=180,weight=70):
    print(f"姓名：{name}， 年龄：{age}，性别：{gender}")
    #print(f"可变位置参数：{args}")
    #print(f"可变关键字参数：{kwargs}")


print_info1("张三", 18, "男", height=190, weight=60)
