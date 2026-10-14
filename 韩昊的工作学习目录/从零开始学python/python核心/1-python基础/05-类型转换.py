"""
@Author  : 韩昊
@Company : ********
@Date    :
@Desc    :
@Version : 1.0
"""

from traceback import print_tb
import math

age = "18" #str
print(f"age{type(age)}")
age = int(age)
print(f"age{type(age)}")

age = str(age)
print(age)
print(f"age{type(age)}")

print("=" * 30)

name = "张三"
#name = int(name)
#float(name) 报错

print("=" * 30)

# float
pi = 3.1415926
pi_str = str(pi)
print(pi)
print(f"pi type = {type(pi)}") # float
print(pi_str)
print(f"pi_str type = {type(pi_str)}") #str

print("=" * 30)
#float -> int 小数部分会全部丢弃
int_value = int(math.pi)
print(f"int_value = {int_value},type = {type(int_value)}")



# bool -> int True = 1 False = 0
print("=" * 30)
print(f"True + 1 = {True + 1},type = {type(True + 1)}")
# is_passed = True
is_passed = False
int_value = int(is_passed)
print(f"int_value = {is_passed},type = {type(is_passed)}")
print(f"True + 1 = {True + 1},type = {type(True + 1)}") #2 true

print("=" * 30)

#非0的数都是True
int_value = 100
bool_value = bool(int_value)
print(f"bool_value = {bool_value},type = {type(bool_value)}")

print("=" * 30)

#None类型转bool
none_value = None
bool_value = bool(none_value)
print(f"bool_value = {bool_value},type = {type(bool_value)}")

# 空字符
empty_str = ""
bool_value = bool(empty_str)
print(f"bool_value = {bool_value},type = {type(bool_value)}")
