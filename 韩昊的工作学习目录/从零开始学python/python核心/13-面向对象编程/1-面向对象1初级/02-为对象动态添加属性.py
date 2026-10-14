"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#创建一个类
class Student:
    """
    学生类
    """
    #定义一个属性
    school_name = "中国大学"
    #定义一个方法
    def study(self):
        print("正在学习...")

    #定义考试方法
    def take_exam(self,subject ):
        print(f"正在参加{subject}考试...")

#创建一个学生对象 张三 18
zhang_san = Student()
zhang_san.name = "张三"
zhang_san.age = 18
print(f"张三的学校是:{zhang_san.school_name}")
print(f"张三的年龄是:{zhang_san.age}")
