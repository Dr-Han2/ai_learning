"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#定义字典的key
ID = "id"
NAME = "name"
DEPT = "dept"
SALARY = "salary"

#定义一个员工字典 CTRL+ALT+L 自动格式化
emp_dict = {
    ID: 1001,
    NAME: "张三",
    DEPT: "技术部",
    SALARY: "20000"
}
#通过KEY访问字典的元素 最常用[KEY]
print(f"员工的ID是:{emp_dict[ID]}")
print(f"员工的姓名是:{emp_dict[NAME]}")
print(f"员工的部门是:{emp_dict[DEPT]}")
print(f"员工的薪水:{emp_dict[SALARY]}")
print(emp_dict["id"])

#print(emp_dict["age"])
#通过get(key)访问
print(f"员工的id:{emp_dict.get(ID)}")
#访问一个不存在的KEY
print(f"员工的年龄:{emp_dict.get("AGE")}")
# 访问一个不存在的KEY时，返回一个默认值
print(f"员工的性别是：{emp_dict.get("gender", "保密")}")
print(f"员工的年龄是：{emp_dict.get('age', 18)}")
