"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from exception.exceptions import ParamError, ServiceError, AppException

#系统页面显示
#接收用户输入指令 来进行操作 增删改查退出
while True:
    print("学生管理系统".center(30,"="))
    print("1. 添加学生")
    print("2. 查询学生")
    print("3. 更改学生信息")
    print("4. 删除学生信息")
    print("q. 退出系统")

    choice = input("请输入选项")

    if choice == "q":
        print("退出系统".center(30,"="))
        break
    elif choice == "1":
        try:
            print("添加学生".center(30,"="))
            # 1. 接收用户的输入
            stu_id = input("请输入学生ID：")
            stu_name = input("请输入学生姓名：")
            stu_phone = input("请输入学生电话：")
            # 2. 调用添加学生函数
            result, message = ss.add_student(stu_id, stu_name, stu_pho
        except ParamError as e:
            print(e)
        except ServiceError as e:
            print(e)
        except AppException as e:
            print(e)
        except Exception as e:
            print(e)


