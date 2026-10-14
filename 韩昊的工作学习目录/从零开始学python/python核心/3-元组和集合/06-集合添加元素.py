"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#创建一个集合
set1 =set()
#向集合中添加元素
set1.add("苹果")
print(f"set1: {set1}")
print(f"set1的长度是:{len(set1)}")
#向集合中添加一个列表
set1.update(["橙子", "葡萄", "香蕉"])
print(f"set1: {set1}")
print(f"set1的长度是:{len(set1)}")