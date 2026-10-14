"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from sys import set_coroutine_origin_tracking_depth

#目标:字典的所有操作, 模拟企业用户信息管理系统
#1 定义一个包含多个员工的字典
users ={
    "user1001": {"name": "张三", "age": 25, "dept": "技术部", "phone": "13800138000"},
    "user1002": {"name": "李四", "age": 23, "dept": "市场部", "phone": "13800138001"},
    "user1003": {"name": "王五", "age": 27, "dept": "财务部", "phone": "13800138002"}
}
# ============================================================
# 1. 查：遍历所有用户  .items()
# ============================================================
def show_all():
    print("\n" + "全部用户" .center(50,"="))
    if not users:
        print("暂无用户")
        return
    for emp_id , info in users.items():
        print(f"工号:{emp_id},姓名:{info['name']},年龄:{info['age']},"
              f"部门:{info['dept']},电话:{info['phone']}")
        print("=" * 53)
show_all()
# ============================================================
# 2. 增：添加用户  setdefault() 防止覆盖已有工号
# ============================================================

def add_user(emp_id,name,age,dept,phone):
    if emp_id in users:
        print(f"工号{emp_id}存在,不能重复添加")
        return False
#setdefault()不存在才添加
    users.setdefault(emp_id,{
        "name":name,
        "age":age,
        "dept":dept,
        "phone":phone
    })
    print(f"已添加用户{name}(工号:{emp_id})")
    return True

# ============================================================
#3 . 查：针对单个用户的查找 get()
# ============================================================
def find_user(emp_id):
    user = users.get(emp_id)
    if user is None:
        print(f"工号为:{emp_id}的用户不存在")
        return None
    print(f"\n工号:{emp_id}")
    for key,value in user.items():
        print(f"{key}:{value}")
    return user

# ============================================================
#4 . 删除：pop
# ============================================================
def update_user(emp_id,**kwargs):
    user = users.pop(emp_id,None)
    if user in None:
        print(f"工号为{emp_id}的用户不存在")
        return False
    print(f"已删除{user['name']}({emp_id})")
    return True
# ============================================================
# 5. 统计：按部门分组（字典嵌套 + setdefault）
# ============================================================
def group_by_dept():
    dept_map={}
    for emp_id, info in users.items():
        dept = info["dept"]
        # setdefault：部门第一次出现时建一个空列表，再 append
        dept_map.setdefault(dept,[]).append(info["name"])

    print("\n" + " 按部门分组 ".center(50, "="))
    for dept, names in dept_map.items():
        print(f"{dept}（{len(names)}人）：{', '.join(names)}")
    return dept_map

# ============================================================
# 6. 排序：sorted() + 字典推导式
# ============================================================
def sort_by_age():
    #sorted 返回列表,再用字典推导式重建字典
    sorted_users ={
        emp_id: info
        for emp_id , info in sorted(users.items(), key=lambda item: item[1]["age"])
    }
    print("\n" + "按年龄升序 ".center(50, "="))
    for emp_id, info in sorted_users.items():
        print(f"{info['age']:>} 岁  {info['name']:<10} [{emp_id}]")
    return sorted_users

sort_by_age()














