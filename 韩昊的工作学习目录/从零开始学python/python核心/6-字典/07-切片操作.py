"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 定义一个字典
dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
#print(f"切片:{dict1[:2]}") #本质上是无序的 KeyError
#1 . 对键列表进行切片
keys =dict1.keys()
print(f"键列表:{keys}")
#键列表类型:<class,'dict_keys'>
print(type(keys))
#对Key进行类型转化
keys =list(keys)
#<class,'list'>
print(type(keys))
#前3个KEY
print(keys[0:3])

#2 . 对值切片
values = dict1.values()
print(f"值列表:{values}")
#值列表类型:<class,'dict_values'>
print(type(values))
values = list(values)
print(type(values))
#<class,'list'>
print(values[0:3])

#3  对键值对进行切片
items = dict1.items()
print(f"键值列表:{items}")
#值列表类型:<class,'dict_items'>
print(type(items))
items = list(items)
print(type(items))
#<class,'list'>
print(items[0:3])
