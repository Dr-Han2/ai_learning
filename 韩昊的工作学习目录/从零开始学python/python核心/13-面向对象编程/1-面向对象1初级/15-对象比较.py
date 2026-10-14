"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
class Student:
    def __init__(self,name,score,age,stu_no):
        self.name = name
        self.age =age
        self.stu_no =stu_no
        self.score=score



student1 = Student("张三",90,18,1001)
student2 = Student("张三",90,18,1001)
print(student1 == student2)