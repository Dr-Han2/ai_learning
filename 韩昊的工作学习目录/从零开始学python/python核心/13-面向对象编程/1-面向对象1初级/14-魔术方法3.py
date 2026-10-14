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
    def __len__(self):
        return len(self.name)

zhang_san = Student('张三',90)
print(len(zhang_san))