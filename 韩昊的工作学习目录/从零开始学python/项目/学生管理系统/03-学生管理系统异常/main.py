"""
@Author  : 刘光尘
@Company : 未来元启
@Date    : 2026/9/11 09:50
@Desc    : 
@Version : 1.0
"""
# 导入学生模块
from service import student_service as ss
# 导入异常模块
from exception.exceptions import ParamError, ServiceError, AppException
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
        try:
            print(" 新增学生 ".center(30, "="))

            # 1. 接收用户的输入
            stu_id = input("请输入学生ID：")
            stu_name = input("请输入学生姓名：")
            stu_phone = input("请输入学生电话：")
            # 2. 调用添加学生函数
            result, message = ss.add_student(stu_id, stu_name, stu_phone)
            # 3. 展示结果
            print(message)
        except ParamError as e:
            print(e)
        except ServiceError as e:
            print(e)
        except AppException as e:
            print(e)
        except Exception as e :
            print(e)
    elif choice == "2":
        try:
            print(" 查询学生 ".center(30, "="))
            # 1. 接收用户的输入
            stu_id = input("请输入学生ID：")
            # 2. 调用查询学生函数
            result, message = ss.query_student_by_id(stu_id)
            # 3. 展示结果
            if result is None:
                print(message)  # 错误提示
            else:
                print(result)  # 学生信息字典
        except AppException as e:
            print(e)
        except Exception as e:
            print(e)

    elif choice == "3":
        print(" 删除学生 ".center(30, "="))
        # 1. 接收用户的输入
        stu_id = input("请输入学生ID：")
        # 2. 调用删除学生函数
        try:
            result, message = ss.delete_student(stu_id)
            # 3. 展示结果
            print(message)
        except AppException as e:
            print(e)
        except Exception as e:
            print(e)

    elif choice == "4":
        print(" 更新学生 ".center(30, "="))
        # 1. 接收用户的输入
        stu_id = input("请输入学生ID：")
        stu_name = input("请输入学生姓名：")
        stu_phone = input("请输入学生电话：")
        try:
            # 2. 调用修改学生函数
            result, message = ss.modify_student(stu_id, stu_name, stu_phone)
            # 3. 展示结果
            print(message)
        except AppException as e:
            print(e)
        except Exception as e:
            print(e)
    elif choice == "5":
        print(" 查看所有 ".center(30, "="))
        # 1. 调用查询所有学生函数
        result, message = ss.query_all_students()
        # 2. 展示结果，遍历字典，打印每个学生的信息
        for student in result.values():
            print(student)

    elif choice == "q":
        print(" 退出系统 ".center(30, "="))
        break
    else:
        print(" 输入错误 ".center(30, "="))