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
    def __str__(self):
        return f"学生信息 姓名:{self.name},分数:{self.score}"
#打印对象
zhang_san = Student("张三",90)
print(zhang_san) #对象在内存中地址的字符串表示
#字符串转换
str_obj=str(zhang_san)
print(str_obj)
#当打印对象 或把对象转成字符串时 会自动调用__str__()

