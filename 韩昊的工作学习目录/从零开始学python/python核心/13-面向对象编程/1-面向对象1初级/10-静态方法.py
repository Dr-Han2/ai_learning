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
    def __init__(self,name,score):
        #为对象添加一个实例属性
        self.name = name
        self.score =score

    #
    @staticmethod
    def check_score(score):
        return 0 <= score <= 100
#
print(Student.check_score(100))
print(Student.check_score(-1))

#通过对象来调用
student = Student("张三",50)
print(student.check_score(student.score))
