"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
nums=[] #创建一个空列表
print(f"添加元素前的列表:{nums}")
#for循环添加元素
for i in range(1,11):
    nums.append(i)
print(f"添加元素后的列表:{nums}")

#直接使用列表推导式
nums1 = [i for i in range(1,11)]
print(f"使用列表推导式构建的列表:{nums1}")

nums2 = [f"user_{i}" for i in range(1,11)]
print(nums2)