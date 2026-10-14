"""
@Author  : 韩昊
@Company : 天津电子信息职业技术学院
@Date    :   2026/9/1 14:00
@Desc    :
@Version : 1.0
"""

#定义关于学生的信息(变量)
student_name = "张三"    #str
student_age = 18        #int
student_height = 1.75   #float
is_passed = True        #bool

#查看某个变量具体的类型
print(f"student_name 的类型是{type(student_name)}")
print(f"student_age 的类型是 {type(student_age)}")
print(f"student_height 的类型是 {type(student_height)}")
print(f"is_passed 的类型是 {type(is_passed)}")

print("=" * 30)

name = "李四"
print(name)
print(type(name))

name = 1000
print(name)
print(type(name)) #int

#=======
print("=" * 30)
#不同类数据类型无法进行加减乘除操作 要拼接  必须转类型
#print(student_name + student_age)

# 用一个变量接收转换后的字符串类型
student_age_str = str(student_age)
print(student_name + student_age_str)
#用一行代码进行简化操作
print(student_name + str(student_age))