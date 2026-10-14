"""
@Author  : 韩昊
@Company : *********
@Date    :
@Desc    :
@Version : 1.0
"""

#列表中的元素不限制数据类型
list1 = [1, "hello", True , 3.14, "张三"]
print(f"list1 = {list1}")
print(f"list1 的类型:{type(list1)}")

#用list()函数创建列表,相当于类型转化
list2 =list("hello")
print(f"list2 = {list2}")

#序列来创建
list3 =list(range(1,10,2))
print(f"list3 = {list3}")

s = "hello"
for i in s:
    print(i)
list4 = list(s)
print(f"list4 = {list4}")