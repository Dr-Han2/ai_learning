"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 打印用户信息，年龄默认 18 岁
def print_info(name, age=18, gender="未知"):
    print(f"姓名：{name}，年龄：{age}，性别：{gender}")

# 调用函数
# 不传年龄时，使用默认值
print_info("张三")
# 传入年龄时，使用传入的值
print_info("张三", 19)
print_info("张三", 19, "男")
# 不传age 的值，但是要传gender的值
print_info("张三", gender="男")