"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#1. 方法中必须第一个参数self
#2_单下划线开头的方法是约定私有
#3 __双下划线开头的方法强制私有
class Student:
    """
    学生类
    """
    #定义一个属性
    school_name = "中国大学"
    #构造方法
    def __init__(self,name,age,score):
        #为对象添加一个实例属性
        self.name = name
        self.age =age
        self.score = score

        print(f"创建一个学生对象,姓名是:{self.name},年龄是:{self.age}")
    #定义一个方法
    def study(self):

        print("正在学习...")

    #定义考试方法
    def take_exam(self,subject ):
        print(f"正在参加{subject}考试...")

    #约定私有实例方法
    def _update_score(self,score):
        print(f"更新分数={score}")
        self.score = score

    def __update_score(self,score):
        print(f"更新分数={score}")
        self.score = score

#创建一个对象
student = Student("张三",18,90)
#调用公开的实例方法
student.study()
student.take_exam("数学")
#调用约定私有的实例方法
student._update_score(100)

#1约定私有可以被调用
#2强制私有不能被调用


