"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from functools import total_ordering
@total_ordering #自动更新方法

class Student:
    def __init__(self, name, age, stu_no):
        self.name = name
        self.age = age
        self.stu_no = stu_no

    #重写eq方法
    def __eq__(self,other):
        #判断other是否时当前类的实例
        if   not isinstance(other,Student):
            return False
        #比较属性,自定义规则
        result= (self.name == other.name and
                 self.age == other.age and
                 self.stu_no == other.stu_no)
        #返回一个布尔值True,False不相等
        return result

    def __gt__(self,other):
        if not isinstance(other,Student):
            raise TypeError("比较的对象必须是Student")
        result= (self.age > other.age)
        return self.name > other.name


#实例化
student1 = Student("张三",18 ,"S101")
student2 = Student("张三",18 ,"S101")
print(student1 == student2)

#创建一个李四对象
student3 = Student("李四",20 ,"S102")
print(student3 == student1)
#判断大小
print(student1 > student3)#false
print(student1 < student3)#true
print(student1 >= student3)#false
print(student1 <= student3)#true
print(student1 != student3)#true

