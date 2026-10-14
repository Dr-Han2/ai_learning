"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#模仿方法一般不直接调用 而是由Python在特定语法
#或内置操作时自动触发
# ,用来让自定义对象支持内置行为
#、运算符、容器协议等等
#模仿方法通常以双下划线开头和结尾
#例如 __init__ 、__str__、__add__
#python
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __len__(self):
        return 2

    def __getitem__(self, index):
        return (self.x, self.y)[index]

v1 = Vector(1,2)
v2 =Vector(3,4)

v3 = v1 + v2
print(v3) #(4,6)
print(len(v3))    # 自动调用 __len__ -> 2
print(v3[0])      # 自动调用 __getitem__ -> 4