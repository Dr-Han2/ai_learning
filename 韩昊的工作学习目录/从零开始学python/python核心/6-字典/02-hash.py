"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#int的hash值
print(f"int型的hash值{hash(1)}")
print(f"int型的hash值{hash(100)}")
print(f"int型的hash值{hash(1000)}")

# 字符串的HASH值
print(f"字符串的HASH值 {hash("hello")}")
print(f"字符串的HASH值 {hash("hello")}")
print(f"字符串的HASH值 {hash("world")}")
print(f"字符串的HASH值 {hash("python")}")

# 不可变类型的HASH值
print(f"不可变类型的HASH值 {hash((1, 2, 3))}")
#可变类型的HASH值 列表 字典 集合 bytearray
#print(f"可变类型的HASH值{hash([1,2,3])}") 可变类型Python不允许计算它的hash值

print("=" * 30)
print(f"8所在的HASH桶位置:{hash(8) % 8}") # 8/8 =0
print(f"HELLO所在的HASH桶位置:{hash("HELLO") % 8}")
print(f"HELLO所在的HASH桶位置:{hash("HELLO") % 16}")
