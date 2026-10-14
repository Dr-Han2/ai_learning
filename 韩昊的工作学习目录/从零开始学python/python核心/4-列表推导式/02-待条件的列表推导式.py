"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 创建一个1-20中的偶数的列表
even_nums = []
print(f"添加前的列表:{even_nums}")

for i in range(1,21):
    if i % 2 == 0:
        even_nums.append(i)
print(f"添加后的列表:{even_nums}")

#列表推导式
even_nums1 = [i for i in range(1,21) if i % 2 == 0]
print(even_nums1)

# 示例2：把列表中大于10的元素组成的新列表
old_list = [5, 12, 8, 15, 3, 20]
#
new_list = [i for i in old_list if i > 10 ]
print(new_list)
