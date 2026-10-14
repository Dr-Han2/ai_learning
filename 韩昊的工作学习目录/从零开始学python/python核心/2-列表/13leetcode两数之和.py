"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，
#并返回它们的数组下标。
#分析 可以用两个循环来完成这个问题
#外循环 控制一个数
#内循环控制另一个数
#外循环从0开始，内循环从外循环的下一个元素开始 例 for i in len: for j in range(i+1 len)
#定义一个列表
nums =[3,3]
#定义一个目标值
target =6
#获取列表的长度
lenght=len(nums)
print(lenght)
for i in range(lenght):
    for j in range(i+1,lenght):
        if nums[i] + nums[j] == target:

            print(f"两数的下标为{i},{j}")#
#时间复杂度O(N^2)