"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
class Student:
    def __init__(self, name, age, score):
        #私有属性全部强制私有，外部不能直接访问
        self.__name = name
        self.__age = age
        self.__score =score

    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age

    @property
    def score(self):
        return self.__score


    @name.setter

    def set_name(self,name):
        if not isinstance(name,str) or name.strip() == "":
            raise TypeError("姓名必须为字符串且不能为空")
        self.__name = name

    @age.setter
    def age(self,age):
        if not isinstance(age,int) or age <= 0:
            raise TypeError("年龄必须为正整数")
        self.__age = age

    @score.setter
    def score(self,score):
        if not isinstance(score,int) or score <= 0:
            raise TypeError("成绩必须为正整数")
        self.__score = score






