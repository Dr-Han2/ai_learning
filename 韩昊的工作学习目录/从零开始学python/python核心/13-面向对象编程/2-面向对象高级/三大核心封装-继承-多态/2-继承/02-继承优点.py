"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#首先定义一个父类 Cat和Dog属于Animal 所以可以先定义父类Animal
class Animal:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    #定义方法
    def eat(self):
        print(f"{self.__name}正在吃法")

    def play(self):
        print(f"{self.__name}正在玩耍")

    def sleep(self):
        print(f"{self.__name}正在睡觉")

#现在定义子类继承父类 格式class 子类名(父类名)
class Dog(Animal):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def Wow(self):
        print(f"{self.__name}正在Wow叫")

class Cat(Animal):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def mew(self):
        print(f"{self.__name}正在o(=•ェ•=)m")

cat1 = Cat("Mini",5)
cat1.mew()

dog1 = Dog("Steven",10)
dog1.Wow()
#子类中没有的方法被调用时 首先会看父类中有无 若无则报错
#dog1.mew()
#AttributeError: 'Dog' object has no attribute 'mew'
#可以看到 使用继承之和 我们把Cat Dog的共同属性全部打包在一个父类Animal中
#使代码变得少而简洁 对程序员后期的维护有帮助
#子类中特有的方法我们直接写在子类里即可


