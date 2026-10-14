"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
def func1(x):
    return x * x

print(func1(10))
#
func2 = lambda x: x * x
print(func2(10))

def func3(x,y):
    return x * y
print(func3(10,20))

func4 = lambda x,y: x * y
print(func4(10,20))