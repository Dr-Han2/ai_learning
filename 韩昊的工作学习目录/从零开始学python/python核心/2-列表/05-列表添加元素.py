"""
@Author  : 韩昊
@Company : *********
@Date    :
@Desc    :
@Version : 1.0
"""

#定义空列表
fruit = []
print(f"fruit列表: {fruit}")
#使用append()向列表尾加入一个元素
fruit.append("apple")
print(f"fruit列表:{fruit}")

fruit.append("banana")
print(f"fruit列表:{fruit}")

#使用insert()在列表指定元素添加一个元素
fruit.insert(1,"mango")
print(f"fruit列表:{fruit}")

#在有效的位置插入一个元素，超出列表下标最大值，会插入到表尾
fruit.insert(30,"Grapes")
print(f"fruit列表:{fruit}")
#extend(2-列表,序列)
list0 = ["1","2"]
fruit.extend(list0)
print(f"fruit列表:{fruit}")