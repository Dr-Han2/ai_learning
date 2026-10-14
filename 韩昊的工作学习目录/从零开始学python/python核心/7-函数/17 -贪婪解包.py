"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 定义一个元素比较多的列表
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#用一个变量接收第一个元素，再用一个变量接收最后一个元素
first , *other , last = list1
print(f"第一个元素:{first}")
print(f"最后一个元素:{last}")
print(f"其他元素:{other}")
#other是一个列表
print(type(other))

# 只取第一个元素，其他的存在一个数据容器中
first, *_ = list1
print(f"第一个元素：{first}")
# _ 表示一个变量，可以忽略，在程序中不使用
print(f"其他元素：{_}")
print(type(_))

