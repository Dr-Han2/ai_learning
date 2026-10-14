"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#元组不支持推导式(不可变)
#因此可以先生成列表 再转化为元组
list1 =[i for i in range(1,11)]
print(f"list1: {list1}")
print(f"list1的类型:{type(list1)}")
#转化类型
a =tuple(list1)
print(f"a:{a}")
print(f"a的类型为:{type(a)}")

#集合推导式
set1 ={i for i in range(1,11)}
print(set1)
print(f"set1的类型:{type(set1)}")

