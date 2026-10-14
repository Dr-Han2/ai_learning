"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#局部变量和全局变量
#1 局部变量
#只能在函数内部修改
def func(x):
    x += 100
    print(f"函数内部修改后的x={x}")
func(100)
#在外部定义一个变量
a = 100
func(a)
print(f"函数外部修改后的参数值:{a}") #未修改

def func1(lst):
    # 给列表追加元素
    lst.append(100)  # [1, 2, 3] -> [1, 2, 3, 100]
    print(f"函数内部修改后的列表：{lst}")

# 在外部定义一个列表
list1 = [1, 2, 3]
func1(list1)
print(f"函数外部修改后的列表：{list1}")

# 定义一个函数，在列表中追加元素
def func2(lst):
    # 给列表追加元素
    lst = [10, 20, 30]
    print(f"函数内部修改后的列表：{lst}")

list2 = [1, 2, 3]
func2(list2)
print(f"函数外部修改后的列表：{list2}")