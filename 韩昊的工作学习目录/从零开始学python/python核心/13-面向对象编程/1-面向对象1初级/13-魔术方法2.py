"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def __repr__(self):
        return f"Student(name={self.name},score={self.score})"
#打印
zhang_san = Student("张三",100)
print(zhang_san)

str_obj = str(zhang_san)
print(str_obj)


#__len__方法
