"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import functools
def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"开始执行[{func.__name__}]")

        result = func(*args, **kwargs)

        print(f"执行结束,返回结果为{result}")

        return result


    return wrapper
@log_decorator
def add(a,b):
    return a+b
@log_decorator
def is_even(n):
    return n % 2 == 0


print(f"测试add函数")
add(10,20)
print(f"测试is_even函数")
is_even(6)
is_even(7)