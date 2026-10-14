"""
@Company : *******
@Date    :
@Desc    :
@Version : 1.0
"""

#猜数字
import random

a=random.randint(0,100)
print(a)
num = int(input("请输入您要猜的数字"))
while True:
    if 0<=num<=100:
        if num == a:
            print("您答对了")
            break
        elif num > a:
            print("您要猜的数字大了")
            num = int(input("请输入你要猜的数字"))
        elif num < a:
            print("您要猜的数字小了")
            num = int(input("请输入您要猜的数字"))
    if num >100 or num <0:
        print("您猜的数字不在随机数生成的范围内，请重新输入")
        num = int(input("请输入您要猜的数字"))
