"""
@Author  : 韩昊
@Company : *********
@Date    :
@Desc    :
@Version : 1.0
"""
#分析:
#1.我们需要输入学生的各科成绩 故 需要 input函数
#2. 每次输入一科成绩 用不同变量接收
#3. 计算结果 用加法
#4. 在控制台上打印结果
chinese = float(input("请输入你的语文成绩:"))
math = input("请输入你的数学成绩:")
math = float(math)

english = input("请输入你的英语成绩")
english =float(english)

#计算总分
total = chinese + math + english
print(f"总分为 = {total}")

#这部分内容我会在循环和IF语句中进行拓展讨论