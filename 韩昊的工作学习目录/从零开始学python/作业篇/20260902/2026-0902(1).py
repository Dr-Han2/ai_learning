"""
@Author  : 韩昊
@Company : *******
@Date    :
@Desc    :
@Version : 1.0
"""
#判断闰年
year =int(input("请输入一个年份:"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")