"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#使用super().__init__()给子类添加属性
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #定义方法
    def eat(self):
        print(f"{self.name}正在吃法")

    def play(self):
        print(f"{self.name}正在玩耍")

    def sleep(self):
        print(f"{self.name}正在睡觉")

#假如Cat有颜色 Dog无
class Cat(Animal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color

    def mew(self):
        print(f"{self.name}正在o(=•ェ•=)m")

class Dog(Animal):
    def Wow(self):
        print(f"{self.name}正在Wow叫")


#实例化Cat Dog
Cat1 = Cat("Mini",5,"yellow")
Cat1.mew()
