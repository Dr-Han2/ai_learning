"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#{}创建集合 与字典区别 字典要有键和值 集合只需要有元素即可
#集合元素会自动去重
set1 = {"苹果", "香蕉", "梨子", "苹果"}
print(f"set1: {set1}")
print(f"set1的类型: {type(set1)}")
print("=" * 30)

#创建一个空集合
set2 = set()
print(f"set2: {set2}")
print(f"set2: {type(set2)}")
print("=" * 30)

set0 = {}#字典
print(f"set0:{type(set0)}")
print("=" * 30)

#set()方法创建
set3 = set(["张三", "李四", "王五", "张三"])
set4 = set(("pytho", "java", "pytho"))
print(f"set3: {set3}")
print(f"set4: {set4}")
set5 =set("hello")
print(f"set5: {set5}")

