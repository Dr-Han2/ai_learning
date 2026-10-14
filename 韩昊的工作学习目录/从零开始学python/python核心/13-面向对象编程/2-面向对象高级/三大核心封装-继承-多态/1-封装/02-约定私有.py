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
        self._score =score

#创建对象,修改
student1 =Student("张三",18,99)
print(student1._score)
student1._score = 1000
print(student1._score)