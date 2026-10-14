"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 1. 返回单个值，定义一个加法运算函数
def add_num(num1, num2):
    result = num1 + num2
    return result

# 调用
result = add_num(10, 20)
print(result)

# 1. 返回单个值，定义一个加法运算函数
def add_num1(num1, num2):
    result = num1 + num2
    print(result)
    # 返回None
    return

result = add_num1(10, 20)
print(result)

################################
# 2. 返回多个值，定义函数，接收两个参数，姓名和分数，返回姓名和分数评级
def get_grade(name, score):
    if score >= 90:
        grade = "A"
        return name, grade
    elif score >= 80:
        grade = "B"
        return name, grade
    elif score >= 70:
        grade = "C"
        return name, grade
    elif score >= 60:
        grade = "D"
        return name, grade
    else:
        grade = "F"
        return name, grade

# 调用
result = get_grade("张三", 80)
print(f"result的类型 {type(result)}")  # 元组
# 自动解包
name, grade = result
print(f"{name}的评级为：{grade}")

