"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#定义一个字典(员工信息)
emp_dict={
    "id": 1001,
    "name": "张三",
    "dept": "技术部",
    "salary": "8000",
    "age": 25
}
#1获取字典所有的KEY
for key in emp_dict.keys():
    print(f"key={key}")
print("=" * 30)


#默认遍历字典的KEY
for key in emp_dict:
    print(f"key={key},value={emp_dict[key]}")
print("=" * 30)

#2 获取字典中的所有的VALUE
for value in emp_dict.values():
    print(f"value={value}")
print("=" * 30)

#3 遍历所有的KEY/VALUE
for key, value in emp_dict.items():
    print(f"keuy={key},value={value}")
print("=" * 30)