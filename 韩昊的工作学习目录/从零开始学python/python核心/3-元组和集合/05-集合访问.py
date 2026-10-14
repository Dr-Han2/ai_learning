"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 定义一个集合
week_set = {"周一", "周二", "周三", "周四", "周五", "周六", "周日"}

# 集合是无序的，不能通过下标访问元素
# TypeError: 'set' object is not subscriptable
#print(week_set[0])

# 判断元素是否在集合中
print(f"周一是否在集合中：{'周一' in week_set}")  # True
print(f"周一是否不在集合中：{'周一' not in week_set}")  # False

# 遍历集合
for week in week_set:
    print(f"遍历集合：{week}")

