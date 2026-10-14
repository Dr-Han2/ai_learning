"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
class A:
    def __add__(self, other):
        return NotImplemented

class B:
    def __radd__(self, other):
        return "B.__radd__ 被调用"

a, b=A(), B()
print(a.__add__(b))#这个操作我处理不了 试试别的办法
print(a+b)
