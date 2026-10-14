"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#对学生分数进行评级 需要一个参数 score
def get_score(score):
    """
    根据分数返回评级
    :param score:
    :return:
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
#调用 给参数赋值即可
score1 =88
print(get_score(score1))