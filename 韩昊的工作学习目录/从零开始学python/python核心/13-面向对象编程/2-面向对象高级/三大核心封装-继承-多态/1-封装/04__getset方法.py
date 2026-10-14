"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
class Student:
    """
    学生类
    """
    #构造方法
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.__score =score

    def get_score(self):
        return self.__score