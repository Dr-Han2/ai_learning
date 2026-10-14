"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 定义函数，接收用户输入的姓名，年龄，性别并打印
def print_info(name, age, gender):
    print(f"姓名：{name}, 年龄：{age}, 性别：{gender}")

# 调用函数：以正确的顺序进行传参
print_info("张三", 18, "男")
# 调用函数：以错误的顺序进行传参
print_info("张三", "男", 18)

# 多传一个参数
# print_info("张三", 18, "男", "202609班")

# 少传一个参数
#print_info("张三", 18)
#传参数一定要传全 少传和多传都会报错