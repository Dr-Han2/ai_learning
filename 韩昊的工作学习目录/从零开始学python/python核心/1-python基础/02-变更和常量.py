"""
@Author  : 韩昊
@Company : 天津电子信息职业技术学院
@Date    :   2026/9/5 14:00
@Desc    :
@Version : 1.0
"""

#重复使用相同的字符串
print("hello python")
print("我正在学习python")
print("python是一门主流的编程语言")
print("=" * 30)

#定义一个变量 让变量指向"python"
name = "python"
#使用变量
print("hello", name)
#字符串拼接
print("我正在学习" + name) # 字符串之间可以用 + 进行连接
print(f"{name}是一门主流的编程语言")  # f-string方式进行字符串的格式化

#==========
print("=" * 30)
name="C++"
print(name)
print("我正在学习" + name)
print(f"{name}是一门主流的编程语言")

#======常量======
print("=" * 30)
PI=3.1415926
SCHOOL_NAME = "未来元启"

print(PI)
print(SCHOOL_NAME)

# Python中大小写是敏感
print("=" * 30)
name = "Java"
Name = "张三"

print(name)
print(Name)
print(name)

#==================