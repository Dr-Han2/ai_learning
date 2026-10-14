"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 定义一个函数计算长方形的面积
def get_rectangle_area():
    # 在函数中定义了变量, 只能在函数内部使用，不能在外部使用
    # 函数内部定义的变量，是局部变量
    width = 5
    height = 10
    return width * height

# 在函数外部访问函数内部定义的变量
#print(width)
#NameError: name 'width' is not defined