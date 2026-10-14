"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 定义一个元组（星期几）
week = ("周一", "周二", "周三", "周四", "周五", "周六", "周日")
#1 下标访问 与列表一致
print(f"下标访问,:{week[0]},{week[-1]}")
print("=" * 30)

#查找元素 in week?
print(f"查找星期一是否在元组中:{"周一" in week}")
print(f"查找星期五是否在元组中:{"周五" in week}")
print(f"查找星期五是否不在元组中:{"周一" not in week}")
print(f"统计周一在元组中出现的次数:{week.count("周一")}")
print("=" * 30)

#获取切片
#与列表一致
print(f"切片:{week[0:3]}") #左闭右开
#反向切片
print(f"反向切片:{week[::-1]}")
#取到周四
print(f"正向:周四到周日:{week[3:]}")
print(f"反向:周四到周日:{week[-4:]}")
print("=" * 30)

#遍历
for weekday in week:
    print(f"遍历:{weekday}")
print("=" * 30)

#遍历 同时取下标
for index, weekday in enumerate(week):
    print(f"遍历:{index}-{weekday}")
print("=" * 30)
