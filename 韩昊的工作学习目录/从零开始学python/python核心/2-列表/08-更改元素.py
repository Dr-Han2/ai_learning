"""
@Author  : 韩昊
@Company : *********
@Date    :
@Desc    :
@Version : 1.0
"""
#定义一个包含所有学生的列表
students = ["张三", "李四", "王五"]
print(students)

#通过有效下标找到元素并赋值
#先看指定下标的元素值
print(students[1])
#修改元素的值
students[1] = ("赵六")
print(students[1])
print("修改成功")

#注  修改不要出现下标越界
#students[100] = "钱七"
#IndexError: list assignment index out of range