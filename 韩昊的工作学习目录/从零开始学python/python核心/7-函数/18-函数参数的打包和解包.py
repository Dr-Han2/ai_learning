"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#把多个参数打包成元组
def func(*args):
    print(args)
    print(type(args))
func(1,2,3)
print("=" * 30)

def add(a,b,c):
    result = a+b+c
    return result
print(add(1,2,3))
list = [1,2,3]
print(add(*list))

def func(name, age, gender):
    print(f"姓名：{name}，年龄：{age}，性别：{gender}")

dict1={"name":"张三","age":18,"gender":"mam"}
func(**dict1)