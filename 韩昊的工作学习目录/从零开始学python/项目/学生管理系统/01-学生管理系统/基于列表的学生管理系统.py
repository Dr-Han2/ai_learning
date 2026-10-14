"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 作业: 1.实现一个基于列表的学生管理系统
                2.通过用户的输入完成：增删改查遍历
                3.要求新用户时，接收学号、姓名、电话(组成一个子列表加入到学生列表中)
@Version : 1.0
"""
#1 . 新增学生: 按列表的格式组织数据
#2 . 查询学生: 接收用户输入的学号,遍历列表,比较学生信息子列表中的第一个元素
#3 . 删除学生: 先查询，如果存在则删除
#4 . 更新学生: 先查询, 如果存在则赋新值
#5 . 遍历列表: 取出每一个学生元素进行打印
#定义一个列表 用来存储学生信息
#学号、姓名、手机号
students = []

while True:
    print("========== 学生管理系统 ============")
    print("1. 新增学生")
    print("2. 查询学生")
    print("3. 删除学生")
    print("4. 更新学生信息")
    print("5. 查看所有")
    print("q. 退出系统")

    #1. 接收指令
    choice = input("请输入你的选择:")
    #根据用户指令选择分支
    if choice == "1":
        #.append
        print("========= 添加学生信息 ============")
        stu_no = input("请输入学生学号:")
        stu_name = input("请输入学生姓名:")
        stu_phone = input("请输入学生电话号:")
        #创建一个学生信息子列表
        stu=[stu_no, stu_name, stu_phone]
        #加入到学生列表中
        students.append(stu)
        #
        print(f"添加成功，学号:{stu_no}, 姓名:{stu_name}, 电话号:{stu_phone}")
    elif choice == "2":
        print("========== 查询学生信息 ============")
        #接收学生学号
        stu_no = input("请输入学号")
        #遍历列表 比较学号
        found = False
        for stu in students:
            if stu[0] == stu_no:
                print(f"查询到学生, 学号:{stu_no}, 姓名:{stu_name}, 手机号:{stu_phone}")
                #找到学生
                found = True
                break
        #没有找到
        if not found:
            print(f"没有找到学号为{stu_no}的学生")

    elif choice == "3":
        #删除.remove
        print("========== 删除学生  ============")
        #接收学生学号
        stu_no = input("请输入学生学号")
        #先查找再删除
        found = False
        #遍历列表,找到匹配元素
        for stu in students:
            if stu[0] == stu_no:
                students.remove(stu)
                print("删除成功")
                found =True
                break
        #没有找到学号对应的学生
        if not found:
            print(f"删除失败,没有找到学号为:{stu_no}的学生")

    elif choice == "4":
        print("==========  更新学生信息 ============")
        #接收学生信息
        stu_no = input("请输入学号")
        stu_name = input("请输入姓名")
        stu_phone = input("请输入手机号")

        #先查找再修改
        found = False
        for stu in students:
            if stu[0] == stu_no:
                #更新学生信息
                stu[1] = stu_name
                stu[2] = stu_phone
                print(f"更新学生信息成功，学号:{stu_no}, 姓名:{stu_name}, 手机号:{stu_phone}")
                found =True
                break
        #没有找到学号对应的学生
        if not found:
            print(f"更新失败,没有找到学号为:{stu_no}的学生")

    elif choice == "5":
        print("==========  遍历列表 ============")
        #学生总数
        total_student = len(students)
        print(f"当前学生总数为:{total_student}人")
        #打印每个学生信息
        for stu in students:
            print(f"学号:{stu[0]},姓名:{stu[1]}, 电话号:{stu[2]}")

    elif choice == "q":
        print("退出系统")
        break
    else:
        print("无效输入,请重新输入")









