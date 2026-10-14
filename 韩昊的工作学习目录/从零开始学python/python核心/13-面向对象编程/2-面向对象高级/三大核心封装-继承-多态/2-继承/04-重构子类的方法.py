"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
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

#现在定义子类继承父类 格式class 子类名(父类名)
class Dog(Animal):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def Wow(self):
        print(f"{self.name}正在Wow叫")

    def eat(self):
        print(f"{self.name}正在吃骨头")

class Cat(Animal):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def mew(self):
        print(f"{self.name}正在o(=•ェ•=)m")

    def eat(self):
        print(f"{self.name}正在吃鱼")

cat1 =Cat("Mini",5)
cat1.eat()
