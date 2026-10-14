"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from abc import ABC,abstractmethod
import math
from math import radians


class Shape(ABC):
    def __init__(self,color):
        self.__color = color #触发setter校验

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if not isinstance(color,str) or not color.strip():
            raise TypeError('颜色必须为字符串')

        self.__color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class  Rectangle(Shape):
    def __init__(self,color,length,width):
        super().__init__(color)
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if not isinstance(length,(int,float)) or length <= 0:
            raise TypeError("长必须是大于0的数字")
        self.__length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width,(int,float)) or width <= 0:
            raise TypeError("宽必须是大于0的数字")
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return (self.__length + self.__width) * 2

class Circle(Shape):
    def __init__(self,color,radius):
        super().__init__(color)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self,radius):
        if not isinstance(radius,(int,float)) or radius <= 0:
            raise TypeError("半径必须是大于0的数字")
        self.__radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Rectangle):
    def __init__(self,color,side):
        super().__init__(color,side,side)

    @property
    def side(self):
        return self.__length

    @side.setter
    def side(self,side):
        self.__length = side
        self.__width = side

    # @Rectangle.length.setter
    # def length(self, length):
    #     if not (isinstance(length,(int,float)) or length <= 0):
    #         raise ValueError("side必须是大于0的数字")
    #     self.__length = length
    #     self.__width = length






