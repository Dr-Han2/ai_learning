"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""

# 函数1：煮米饭（小功能）
def cook_rice():
    print("1. 洗米→加水→开火煮米饭")
    return "米饭煮好啦"

# 函数2：炒青菜（小功能）
def fry_vegetable():
    print("2. 洗青菜→切青菜→倒油翻炒")
    return "青菜炒好啦"

# 函数3：做一顿饭（主函数，嵌套调用上面两个小函数）
def make_meal():
    print("开始做一顿饭：")
    # 嵌套调用：在make_meal内部调用cook_rice和fry_vegetable
    rice_result = cook_rice()  # 煮米饭
    veg_result = fry_vegetable()  # 炒青菜
    # 执行完内层函数，继续执行外层函数
    print(f"{rice_result}，{veg_result}，一顿饭做好了")

# 调用主函数
make_meal()