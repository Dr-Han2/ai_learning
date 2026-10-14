"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""

# 字典存放所有学生（学生信息在子字典中）
# 学生字典中的内容：学号、姓名、手机号

# 1. 视图层：用于和用户交互、接收用户输入、展示运行结果
# 2. 业务层：校验视图层传来的参数、实现具体业务逻辑、把学生数据保存在字典中、返回视图层需要的结果

# 定义一个字典来保存学生数据(字典)
students = {}

# 定义KEY
STU_ID = "stu_id"
STU_NAME = "name"
STU_PHONE = "phone"


# 定义一个电话号码校验函数
def check_phone_num(phone_num: str):
    """
    电话号码校验
    :param phone_num: 电话号码
    :return: True/False
    """
    # 不能为空
    if not phone_num.strip():
        return False
    # 长度必须为11位
    if len(phone_num) != 11:
        return False
    # 是否全是数字
    if not phone_num.isdigit():
        return False
    # 校验通过
    return True

# 定义一个添加学生函数
def add_student(stu_id: str, stu_name: str, stu_phone: str):
    """
    添加学生
    :param stu_id: 学号
    :param stu_name: 姓名
    :param stu_phone: 电话号码
    :return: 添加结果
    """
    # 校验学号是否为空
    if not stu_id:
        return False, "学号不能为空"
    # 校验姓名是否为空
    if not stu_name:
        return False, "姓名不能为空"
    # 校验手机号是否为空
    checked_phone_num = check_phone_num(stu_phone)
    if not checked_phone_num:
        return False, "手机号格式错误"

    # 把学号转成大写
    stu_id = stu_id.upper()
    # 检查学号是否重复
    if stu_id in students:
        return False, "学号已存在"

    # 构造一个学生字典
    student = {
        STU_ID: stu_id,
        STU_NAME: stu_name,
        STU_PHONE: stu_phone
    }
    # 保存学生信息
    students[stu_id] = student
    # 返回正确的结果
    return True, "添加成功"

# 删除学生
def delete_student(stu_id: str):
    """
    删除学生
    :param stu_id: 学号
    :return: 删除结果
    """
    # 校验学号是否为空
    if not stu_id:
        return False, "学号不能为空"

    # 学号转大写
    stu_id = stu_id.upper()
    # 检查学号是否存在
    if stu_id not in students:
        return False, "学号不存在"

    # 删除学生信息
    del students[stu_id]
    # 返回正确的结果
    return True, "删除成功"

# 修改学生信息
def modify_student(stu_id: str, stu_name: str, stu_phone: str):

    """
    修改学生信息
    :param stu_id: 学号
    :param stu_name: 姓名
    :param stu_phone: 电话号码
    :return: 修改结果
    """

    # 校验学号是否为空
    if not stu_id:
        return False, "学号不能为空"
    # 学号转大写
    stu_id = stu_id.upper()
    # 检查学号是否存在
    if stu_id not in students:
        return False, "学号不存在"
    # 校验姓名是否为空
    if not stu_name:
        return False, "姓名不能为空"
    # 校验手机号是否为空
    checked_phone_num = check_phone_num(stu_phone)
    if not checked_phone_num:
        return False, "手机号格式错误"


    # 修改学生信息
    student = students[stu_id]
    student[STU_NAME] = stu_name
    student[STU_PHONE] = stu_phone

    # students[stu_id][STU_NAME] = stu_name
    # students[stu_id][STU_PHONE] = stu_phone
    # 返回正确的结果
    return True, "修改成功"

# 按学号查询学生信息
def query_student_by_id(stu_id: str):
    """
    按学号查询学生信息
    :param stu_id: 学号
    :return: 学生信息
    """
    # 校验学号是否为空
    if not stu_id:
        return None, "学号不能为空"
    # 学号转大写
    stu_id = stu_id.upper()
    # 检查学号是否存在
    if stu_id not in students:
        return None, "学号不存在"


    # 返回学生信息
    return students[stu_id], "查询成功"

# 查询所有学生信息
def query_all_students():

    """
    查询所有学生信息
    :return: 所有学生信息
    """
    return students, "查询成功"

# 循环
while True:
    print(" 学生管理系统 ".center(30, "="))
    print("1. 新增学生")
    print("2. 查询学生")
    print("3. 删除学生")
    print("4. 更新学生")
    print("5. 查看所有")
    print("q. 退出系统")

    # 接收用户输入的选项
    choice = input("请输入选项：")

    # 根据用户的选项进入同的分支
    if choice == "1":
        print(" 新增学生 ".center(30, "="))

        # 1. 接收用户的输入
        stu_id = input("请输入学生ID：")
        stu_name = input("请输入学生姓名：")
        stu_phone = input("请输入学生电话：")
        # 2. 调用添加学生函数
        result, message = add_student(stu_id, stu_name, stu_phone)
        # 3. 展示结果
        print(message)
    elif choice == "2":
        print(" 查询学生 ".center(30, "="))
        # 1. 接收用户的输入
        stu_id = input("请输入学生ID：")
        # 2. 调用查询学生函数
        result, message = query_student_by_id(stu_id)
        # 3. 展示结果
        if result is None:
            print(message)  # 错误提示
        else:
            print(result)  # 学生信息字典

    elif choice == "3":
        print(" 删除学生 ".center(30, "="))
        # 1. 接收用户的输入
        stu_id = input("请输入学生ID：")
        # 2. 调用删除学生函数
        result, message = delete_student(stu_id)
        # 3. 展示结果
        print(message)
    elif choice == "4":
        print(" 更新学生 ".center(30, "="))
        # 1. 接收用户的输入
        stu_id = input("请输入学生ID：")
        stu_name = input("请输入学生姓名：")
        stu_phone = input("请输入学生电话：")
        # 2. 调用修改学生函数
        result, message = modify_student(stu_id, stu_name, stu_phone)
        # 3. 展示结果
        print(message)
    elif choice == "5":
        print(" 查看所有 ".center(30, "="))
        # 1. 调用查询所有学生函数
        result, message = query_all_students()
        # 2. 展示结果，遍历字典，打印每个学生的信息
        for student in result.values():
            print(student)

    elif choice == "q":
        print(" 退出系统 ".center(30, "="))
        break
    else:
        print(" 输入错误 ".center(30, "="))
