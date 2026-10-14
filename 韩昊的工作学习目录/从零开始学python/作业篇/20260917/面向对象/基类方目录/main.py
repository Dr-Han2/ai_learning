"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""

from classShapejileifangfa import Circle
from classShapejileifangfa import Rectangle
from classShapejileifangfa import Square

if __name__ == '__main__':
    #实例化 Circle Rectangle
    circle1 = Circle("Red",5)
    rectangle1 = Rectangle("Blue",5,6)
    square1 = Square("Green",5)

    #放入一个列表中 统一管理
    shapes = [circle1,rectangle1,square1]

    for shape in shapes:
        print(f"图形:{type(shape).__name__},颜色:{shape.color}")
        print(f"  面积: {shape.area():.2f}")
        print(f"  周长: {shape.perimeter():.2f}")
        print("=" * 30)

