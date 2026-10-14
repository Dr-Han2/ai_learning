"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#场景目标:用列表存储原始数据,用集合去重,加前辍生成学号
#固定前缀:STU_1001

#1 .用列表存储原始数据(有重复)
original_ids = [1001,1002,1003,1002,1004,1001,1005,1003]
print(f"原始数据:{original_ids}")

#set去重
original_set = set(original_ids)
print(f"去重后的数据:{original_set}")

#去重后排序
new_ids = list(original_set)
print(new_ids)
new_ids.sort()
print(f"排序后的数据:{new_ids}")

# 4. 如查学号大于1001，则生成学号，并加入到列表中
student_nos = [f"STU_{i}" for i in new_ids if i > 1001]

#遍历并打印学号
for index, student_no in enumerate(student_nos):
    print(f"第{index+1}个学生的学号式{student_no}")