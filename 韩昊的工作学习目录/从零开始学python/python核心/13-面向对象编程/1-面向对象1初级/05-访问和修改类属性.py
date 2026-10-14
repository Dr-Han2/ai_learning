"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from student1 import Student
#通过类名来访问
#创建两个对象
zhang_san = Student("张三",18)
li_si     = Student("李四",19)
#1 通过类名访问属性
print(f"所有学生的学校是:{Student.school_name}")

#2 通过对象修改类属性
print("=" * 30)
zhang_san.school_name = "中国中学"
print(f"所有学生的学校是:{Student.school_name}")
print(f"张三的学校是{zhang_san.school_name}")
print(f"李四的学校是{li_si.school_name}")
#只有张三修改成功

#3
print("=" * 30)
#对象中所有定义的属性,如果对象中有同名属性, 则优先访问对象中的属性