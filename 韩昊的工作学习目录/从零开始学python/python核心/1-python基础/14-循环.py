"""
@Author  : 韩昊
@Company : *********
@Date    :
@Desc    :
@Version : 1.0
"""

#在循环中不停的累加初始条件，直到大于等于100则退出
#定义一个初始条件,后面在循环体中更新
condition = 0
#定义一个循环
while condition < 100:
    print(condition)
    #必须要更新退出条件
    condition += 1

print(f"循环结束,当前的conditon={condition}")