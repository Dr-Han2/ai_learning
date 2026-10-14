"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import math

class Shape:
    def __init__(self,color):
        self.color = color

    def area(self):
        return 0

    def perimeter(self):
        return 0

#创建Rectangle类 增加属性 并重构area方法
class Rectangle(Shape):
    def __init__(self,color,length,width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width)*2


class Circle(Shape):
    def __init__(self,color,radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi*self.radius **2

    def perimeter(self):
        return 2* math.pi *self.radius


class Square(Rectangle):
    def __init__(self,color,side):
        super().__init__(color,side,side)


