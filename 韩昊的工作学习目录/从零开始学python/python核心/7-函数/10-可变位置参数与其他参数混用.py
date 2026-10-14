"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
def print_info(name, age=18, gender="未知", *args):
    print(f"姓名：{name}， 年龄：{age}，性别：{gender}")
    # 计算总分
    total = sum(args)
    print(f"总分：{total}")

# 调用
print_info("张三", 18, "女", 80, 90, 100)
