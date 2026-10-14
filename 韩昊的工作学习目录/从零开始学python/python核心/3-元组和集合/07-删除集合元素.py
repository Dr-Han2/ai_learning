"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""

set1 = {"苹果", "香蕉", "橙子", "葡萄", "芒果"}
print(f"原集合：{set1}")

# 1. 使用remove()删除元素
set1.remove("香蕉")
print(f"删除元素后的集合：{set1}")

# 使用remove()删除集合中不存在的元素，当元素不存在是会报错
# KeyError: '香蕉'
# set1.remove("香蕉")

# 2. 使用discard()删除元素
set1.discard("苹果")
print(f"使用discard()删除元素后的集合：{set1}")

# 使用discard()删除不存在的元素，不会报错【推荐】
set1.discard("苹果")
print(f"使用discard()删除不存在元素后的集合：{set1}")

# 3. 使用pop()删除元素，随机删除元素并返回被删除的元素
delete_item = set1.pop()
print(f"使用pop()删除元素后的集合：{set1}")
print(f"删除的元素是：{delete_item}")

# 4. 清空集合
set1.clear()
print(f"清空集合后的集合：{set1}")
