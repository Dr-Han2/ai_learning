"""
@Author  : 韩昊
@Company : *********
@Date    :
@Desc    :
@Version : 1.0
"""

# 需求场景
#
#输入考试分数,判断是否及格
# (60分及以上为及格,否则为不及格)

#1.从控制台接收用户的输入
score = input("请输入分数")
#2换成float类型
score = float(score)
#3判断是否及格
if score >= 60:
    print("考试及格")
else:
    print("考试不及格")
