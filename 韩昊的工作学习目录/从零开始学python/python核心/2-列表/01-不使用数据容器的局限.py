"""
@Author  : 韩昊
@Company : *********
@Date    :
@Desc    :
@Version : 1.0
"""

# 问题：存储3个学生的名字
student1 = "张三"
student2 = "李四"
student3 = "王五"

# 如果想找有没有"李四"这个学生，该怎么办？
# 需要写很长的判断：
if student1 == "李四":
    print("找到了")
elif student2 == "李四":
    print("找到了")
elif student3 == "李四":
    print("找到了")
else:
    print("没找到")

# 如果想计算平均分，也很麻烦：
score1 = 90
score2 = 85
score3 = 92
average = (score1 + score2 + score3) / 3
print(f"平均分是：{average}")