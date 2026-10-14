"""
@Author  : 韩昊
@Company : *********
@Date    :
@Desc    :
@Version : 1.0
"""
#定义列表
fruits = ["苹果", "梨", "香蕉", "橙子", "芒果", "香蕉"]
print(fruits)
#统计某个元素是列表中出现的次数
count = fruits.count("香蕉")
print(f"香蕉出现{count}次")

#方式一: 使用pop删除
fruits.pop() #删除尾元素
print(fruits)
#删除第一个元素pop(0)
del_item = fruits.pop(0)
print(f"删除的元素是{del_item}")
print(fruits)

#方式二:删除指定的元素remove(值)
fruits.remove("香蕉")
print(fruits)

#方式三 使用del删除元素
del fruits[0]
print(fruits)

#方式四: 清空列表
fruits.clear()
print(fruits)