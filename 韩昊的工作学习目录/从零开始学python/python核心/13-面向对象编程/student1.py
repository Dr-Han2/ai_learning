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
    #构造方法
    def __init__(self,name,age):
        #为对象添加一个实例属性
        self.name = name
        self.age =age

        print(f"创建一个学生对象,姓名是:{self.name},年龄是:{self.age}")
    #定义一个方法
    def study(self):

        print("正在学习...")

    #定义考试方法
    def take_exam(self,subject ):
        print(f"正在参加{subject}考试...")