"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#__repr__：给开发者看，用于调试、日志、交互式环境，目标是明确、无歧义，最好能重建对象。
#__str__：给用户看，用于 print() 等，目标是可读、友好

class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"User({self.name!r})" #开发者表示

    def __str__(self):
        return f"User({self.name})"

u = User("Alice")
print(u)
print(str(u))
print(repr(u))
print([u]) # [User('Alice')]   <- 这里用的是 __repr__
