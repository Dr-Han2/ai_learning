"""
@Author  : 韩昊
@Company : *********
@Date    :
@Desc    :
@Version : 1.0
"""

#需求:对考试成绩进行评估
#1 90分及以上为优秀
#2 80 - 90 为良好
#3 60 - 80 为及格
#4 60以下为不及格

#1接收用户输入
score = float(input("请输入考试分数"))
if score >= 90:
    print("优秀")
elif 80<=score<=90:
    print("良好")
elif score >= 60 and score<= 80:
    print("及格")
else:
    print("不及格")

