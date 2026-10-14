"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 定义一个列表保存所有的学生信息
students = []

# 定义KEY
STU_ID = "stu_id"       # 学生ID
STU_NAME = "name"       # 学生姓名
STU_PHONE = "phone_num" # 电话号码

# 提供一个用于用户操作的界面，使用控制台实现
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
        # 进行校验，分两个条件判断，防止stu_id为None时，调用strip()而产生异常
        # 因为None没有strip()
        if not stu_id or stu_id.strip() == "":
            print("学生ID不能为空")
            continue

        # 接收姓名
        stu_name = input("请输入学生姓名：")
        if not stu_name or stu_name.strip() == "":
            print("学生姓名不能为空")
            continue

        # 接收电话号码
        stu_phone = input("请输入学生电话号码：")
        if not stu_phone or stu_phone.strip() == "":
            print("电话号码不能为空")
            continue
        # 电话号必须是11位，且是纯数字
        if len(stu_phone) != 11 or not stu_phone.isdigit():
            print("电话号码必须是11位纯数字")
            continue

        # 2. 把用户输入转换成标准格式, 学号中的字母必须是大写
        stu_id = stu_id.upper()
        # 关于去空格，上面的校验已经完成了
        # 到此，用户输入的三个信息已经完成接收和校验

        # 判断学生ID是否已经存在
        exists = False
        for student in students:
            if student[STU_ID] == stu_id:
                # 修改标识位
                exists = True
                # 退出循环
                break
        if exists:
            print("学生ID已存在")
            # 终止添加操作
            continue

        # 通过所有校验之后，创建一个学生字典
        student = {
            STU_ID: stu_id,
            STU_NAME: stu_name,
            STU_PHONE: stu_phone
        }
        # 把学生追加到列表中
        students.append(student)
        print(f"---> 学生添加成功. {student}")

    elif choice == "2":
        print(" 查询学生 ".center(30, "="))
        # 接收用户输入的学号
        stu_id = input("请输入学生ID：")
        # 校验非空
        if not stu_id or stu_id.strip() == "":
            print("学生ID不能为空")
            continue
        # 转成大写，因为我们添加时的格式要求是字母必须大写
        stu_id = stu_id.upper()

        # 遍历列表，查找学生ID
        for student in students:
            if student[STU_ID] == stu_id:
                print(f"---> 学生信息. {student}")
                break
        else:  # 当循环正常结束，会执行else代码块
            print("学生ID不存在")

    elif choice == "3":
        print(" 删除学生 ".center(30, "="))
        # 接收用户输入的学号
        stu_id = input("请输入学生ID：")
        # 校验非空
        if not stu_id or stu_id.strip() == "":
            print("学生ID不能为空")
            continue
        # 转成大写
        stu_id = stu_id.upper()

        # 遍历列表，找到学生ID对应的字典，然后删除
        flag = False
        for student in students:
            if student[STU_ID] == stu_id:
                # 执行删除
                students.remove(student)
                # 标识符设置为已删除
                flag = True
                break

        # 打印提示
        if flag:
            print("---> 学生删除成功")
        else:
            print("---> 学生ID不存在")

    elif choice == "4":
        print(" 更新学生 ".center(30, "="))
        # 1. 接收用户的输入
        stu_id = input("请输入学生ID：")
        # 进行校验，分两个条件判断，防止stu_id为None时，调用strip()而产生异常
        # 因为None没有strip()
        if not stu_id or stu_id.strip() == "":
            print("学生ID不能为空")
            continue

        # 接收姓名
        stu_name = input("请输入学生姓名：")
        if not stu_name or stu_name.strip() == "":
            print("学生姓名不能为空")
            continue

        # 接收电话号码
        stu_phone = input("请输入学生电话号码：")
        if not stu_phone or stu_phone.strip() == "":
            print("电话号码不能为空")
            continue
        # 电话号必须是11位，且是纯数字
        if len(stu_phone) != 11 or not stu_phone.isdigit():
            print("电话号码必须是11位纯数字")
            continue

        # 2. 把用户输入转换成标准格式, 学号中的字母必须是大写
        stu_id = stu_id.upper()
        # 关于去空格，上面的校验已经完成了

        # 遍历列表，找到学号对应的学生信息，进行修改
        flag = False
        for student in students:
            if student[STU_ID] == stu_id:
                # 修改学生信息
                student[STU_NAME] = stu_name
                student[STU_PHONE] = stu_phone
                # 标识符设置为已修改
                flag = True
                break
        # 打印提示
        if flag:
            print(f"---> 学生信息修改成功, 学号 {STU_ID}, 姓名 {STU_NAME}, 电话 {STU_PHONE}")
        else:
            print("---> 学生ID不存在")

    elif choice == "5":
        print(" 查看所有 ".center(30, "="))
        # 学生总数
        total_students = len(students)
        print(f"当前学生总数为：{total_students} 人")

        # 遍历列表，打印每个学生的信息
        for student in students:
            print(f"学号: {student[STU_ID]}, 姓名: {student[STU_NAME]}, 电话: {student[STU_PHONE]}")
            print("-" * 30)

    elif choice == "q":
        print("退出系统")
        break
    else:
        print("输入错误，请重新选择.")