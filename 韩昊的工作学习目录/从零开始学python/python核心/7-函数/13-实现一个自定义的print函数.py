"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
print("hello", "world", "!")
import sys

def my_print(*args):
    for arg in args:
        sys.stdout.write(str(arg))
        sys.stdout.write(" ")
    sys.stdout.write("\n")
my_print("hello", "world", "!")
my_print("hello world", 123, 3.14, True)
