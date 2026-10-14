"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#定义一个列表 (员工名单)
employees = ["张三", "李四", "王五", "赵六"]
# for循环
for emp in employees:
    print(f"员工:{emp}")
print("=" * 30)

#取出下标和元素
for index, emp in enumerate(employees):
    print(f"下标:{index}, 员工:{emp}")
print("=" * 30)

#使用while循环遍历
index = 0
while index < len(employees):
    print(f"下标:{index},员工:{employees[index]}")
    index += 1
print("=" * 30)

#反转列表
list1 = [2,1,56,36,10]
list1.reverse()
print(list1)
print("=" * 30)
#升序排列
list2 = [2,1,56,36,10]
list2.sort()
print(list2)
print("=" * 30)

list3 = [2, 1, 56, 36, 10]
list3.sort(reverse=True) # 降序排序
# [56, 36, 10, 2, 1]
print(list3)