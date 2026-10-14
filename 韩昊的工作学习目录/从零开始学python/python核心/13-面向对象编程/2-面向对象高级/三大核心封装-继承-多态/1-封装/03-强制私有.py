"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.__score =score


#创建对象,修改
student1 =Student("张三",18,99)
# __3
student1.__score=1000
print(student1.__score)
#
print(student1.__dict__)
#访问
print(student1._Student__score)
#
student1._Student__score=1000
print(f"student1._Student__score:{student1._Student__score}")