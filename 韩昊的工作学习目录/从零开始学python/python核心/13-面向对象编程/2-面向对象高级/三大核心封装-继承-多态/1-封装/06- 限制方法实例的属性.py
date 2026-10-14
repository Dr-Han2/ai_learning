"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""



class Student:

    """学生类"""
    #在这里定义属性才能被外部访问,也可以防止对象动态更新
    __slots__ = ('__name','__age','__score')
    #通过__slots__解决外部动态添加变量的问题



    def __init__(self, name, age, score):
        #私有属性全部强制私有，外部不能直接访问
        self.__name = name
        self.__age = age
        self.__score =score


    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age

    @property
    def score(self):
        return self.__score


    @name.setter
    def name(self,name):
        if not isinstance(name,str) or name.strip() == "":
            raise TypeError("姓名必须为字符串且不能为空")
        self.__name = name

    @age.setter
    def age(self,age):
        if not isinstance(age,int) or age <= 0:
            raise TypeError("年龄必须为正整数")
        self.__age = age

    @score.setter
    def score(self,score):
        if not 0 <= score <= 100 and isinstance(score,int):
            raise ValueError or TypeError("成绩必须为0-100之间正整数且不能为字符串")
        self.__score = score

#实例化一个对象
student1 = Student("张三","18","99")
print(student1._Student__score)
student1._Student__score=1000
#依旧可修改属性(不建议这么做)
print(student1._Student__score)



