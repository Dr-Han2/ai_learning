"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#求两数之和 如果等于给定的target 则返回下标 否则无

def get_index_sum(nums,targer):
    """

    :param nums: 给定列表
    :param targer: 给定目标值
    :return: index的列表
    """
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == targer:
               return [i,j]


nums1=get_index_sum([1,2,3,4],6)
print(nums1)
#O(n^2)时间复杂度较高 可以用简单方法进行优化
