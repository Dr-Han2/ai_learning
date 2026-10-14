"""
@Author  : 韩昊
@Company : *********
@Date    :
@Desc    :
@Version : 1.0
"""

#定义一个列表
students = ["zhangsan","lisi","wangwu","zhaoliu"]
print(f"students:{students}")

#访问元素
print(f"列表中第一个元素:{students[0]}")
print(f"列表中最后一个元素:{students[-1]}")
print(f"列表中最后一个元素:{students[3]}")
print(f"列表中最后一个元素:{students[len(students)-1]}")
#print(f"列表中最后一个元素:{students[4]}") 常见错误
print(f"列表中包含 {len(students)} 个元素")