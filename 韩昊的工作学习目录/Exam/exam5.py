"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import functools


def count_calls(func):
    """
    统计函数执行次数的装饰器
    """

    count = 0


    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        wrapper.count = count

        print(f"{func.__name__}第 {count} 次被调用")

        return func(*args, **kwargs)


    wrapper.count = 0
    return wrapper




@count_calls
def add(a, b):
    """求和函数"""
    return a + b


@count_calls
def is_even(n):
    """判断奇偶函数"""
    return n % 2 == 0


add(10,20)
add(20,30)
add(30,40)

is_even(1)
is_even(2)
is_even(3)

print(f"\nadd函数被总共调用{add.count}次")
print(f"is_even函数被总共调用{is_even.count}次")