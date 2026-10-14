"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#定义两个类 和属性
#例 Cat Dog
class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def play(self):
        print(f"{self.__name}正在玩耍")

    def eat(self):
        print(f"{self.__name}正在吃饭")

    def sleep(self):
        print(f"{self.__name}正在吃法")

    def mew(self):
        print(f" {self.__name}正在o(=•ェ•=)m")

class Dog:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def play(self):
        print(f"{self.__name}正在玩耍")

    def eat(self):
        print(f"{self.__name}正在吃饭")

    def sleep(self):
        print(f"{self.__name}正在吃法")

    def Wow(self):
        print(f"{self.__name}正在汪汪叫")

#实例化
cat1 =Cat("Mimi",18)
dog1 = Dog("Steven",18)
cat1.play()
dog1.eat()
#不同的类有相同的属性 不使用继承 代码会变多 不方便后期维护与查错
