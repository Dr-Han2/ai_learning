"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
def flo(i):
    if i == 1:
        return 1
    elif i ==0:
        return 0
    else:
        return flo(i-1)+flo(i-2)

