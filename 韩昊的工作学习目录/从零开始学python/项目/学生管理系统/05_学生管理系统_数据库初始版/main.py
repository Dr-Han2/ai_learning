"""
@Author  : hanhao
@Company : 未来元启
@Date    : 2026/10/9 10:16
@Desc    : 命令行的用户界面
@Version : 1.0
"""
from service.user_service import UserService
from service.clazz_service import ClazzService
from service.student_service import StudentService
from service.course_service import CourseService
from service.score_service import ScoreService

from model.clazz import Clazz
from model.student import Student
from model.course import Course
from model.score import Score

from core.exceptions import AppException
from core import logger

log = logger.get_logger()


# ============================================================
#                      输入辅助函数
# ============================================================

def input_str(prompt: str) -> str:
    """读取字符串，去除首尾空格"""
    return input(prompt).strip()


def input_int(prompt: str, allow_empty: bool = False):
    """
    读取整数
    :param prompt: 提示语
    :param allow_empty: 是否允许空输入（空则返回 None）
    """
    raw = input(prompt).strip()
    if raw == "":
        if allow_empty:
            return None
        raise ValueError("输入不能为空，需要整数")
    return int(raw)


def input_float(prompt: str, allow_empty: bool = False):
    """读取浮点数"""
    raw = input(prompt).strip()
    if raw == "":
        if allow_empty:
            return None
        raise ValueError("输入不能为空，需要数字")
    return float(raw)


def pause():
    """暂停，等待用户回车"""
    input("\n按回车键继续...")


def print_line():
    """分隔线"""
    print("-" * 70)


# ============================================================
#                      显示辅助函数
# ============================================================

def show_clazz(clazz: Clazz):
    """打印单个班级"""
    if clazz is None:
        print("(未找到)")
        return
    print(f"  ID={clazz.id:<4} 名称={clazz.name:<20} 班主任={clazz.teacher_name}")


def show_clazz_list(clazz_list):
    """打印班级列表"""
    if not clazz_list:
        print("(无数据)")
        return
    print(f"共 {len(clazz_list)} 条：")
    for c in clazz_list:
        show_clazz(c)


def show_student(student: Student):
    """打印单个学生"""
    if student is None:
        print("(未找到)")
        return
    print(f"  ID={student.id:<4} 学号={student.stu_num:<12} 姓名={student.name:<10} "
          f"性别={student.gender or '-':<3} 年龄={student.age or '-':<4} "
          f"班级ID={student.class_id or '-':<4} 电话={student.phone or '-'}")


def show_student_list(student_list):
    """打印学生列表"""
    if not student_list:
        print("(无数据)")
        return
    print(f"共 {len(student_list)} 人：")
    for s in student_list:
        show_student(s)


def show_course(course: Course):
    """打印单个课程"""
    if course is None:
        print("(未找到)")
        return
    print(f"  ID={course.id:<4} 名称={course.name:<20} 学时={course.hour}")


def show_course_list(course_list):
    """打印课程列表"""
    if not course_list:
        print("(无数据)")
        return
    print(f"共 {len(course_list)} 条：")
    for c in course_list:
        show_course(c)


def show_score(score: Score):
    """打印单条成绩"""
    if score is None:
        print("(未找到)")
        return
    print(f"  ID={score.id:<4} 学生ID={score.stu_id:<4} 课程ID={score.course_id:<4} "
          f"分数={score.score:<6} 考试日期={score.exam_time}")


def show_score_list(score_list):
    """打印成绩列表"""
    if not score_list:
        print("(无数据)")
        return
    print(f"共 {len(score_list)} 条：")
    for s in score_list:
        show_score(s)


# ============================================================
#                      登录
# ============================================================

def login():
    """用户登录，成功返回 User，失败返回 None"""
    print("=" * 50)
    print("学生管理系统 - 登录")
    print("=" * 50)
    username = input_str("用户名: ")
    password = input_str("密  码: ")

    try:
        user = UserService.check_login(username, password)
        if user:
            print(f"登录成功，欢迎 {user.real_name}")
            return user
        else:
            print("登录失败：用户名或密码错误")
            return None
    except AppException as e:
        print(f"[业务错误] {e.message}")
        return None
    except Exception as e:
        print(f"[系统错误] {e}")
        return None


# ============================================================
#                      班级管理
# ============================================================

def clazz_add():
    """新增班级"""
    clazz = Clazz()
    clazz.name = input_str("班级名称: ")
    clazz.teacher_name = input_str("班主任: ")
    ClazzService.add(clazz)
    print(f"新增班级成功，ID={clazz.id}")


def clazz_query_by_id():
    """按ID查询班级"""
    id = input_int("班级ID: ")
    clazz = ClazzService.get_by_id(id)
    show_clazz(clazz)


def clazz_query_all():
    """查询全部班级"""
    show_clazz_list(ClazzService.list_all())


def clazz_update():
    """更新班级"""
    id = input_int("要修改的班级ID: ")
    exist = ClazzService.get_by_id(id)
    if exist is None:
        print(f"班级 ID={id} 不存在")
        return

    print("原数据：")
    show_clazz(exist)
    print("(不需要修改的字段直接回车跳过)")

    clazz = Clazz()
    clazz.id = id

    name = input_str(f"新班级名称[{exist.name}]: ")
    clazz.name = name if name else None

    teacher_name = input_str(f"新班主任[{exist.teacher_name}]: ")
    clazz.teacher_name = teacher_name if teacher_name else None

    ClazzService.update(clazz)
    print("更新成功")


def clazz_delete():
    """删除班级"""
    id = input_int("要删除的班级ID: ")
    exist = ClazzService.get_by_id(id)
    if exist is None:
        print(f"班级 ID={id} 不存在")
        return

    print("即将删除：")
    show_clazz(exist)
    confirm = input_str("确认删除？(y/N): ").lower()
    if confirm != "y":
        print("已取消")
        return

    ClazzService.delete(id)
    print("删除成功")


def clazz_menu():
    """班级管理子菜单"""
    while True:
        print("\n" + "=" * 50)
        print("班级管理")
        print("=" * 50)
        print("1. 新增班级")
        print("2. 按ID查询")
        print("3. 查询全部")
        print("4. 更新班级")
        print("5. 删除班级")
        print("0. 返回上级")
        choice = input_str("请选择: ")

        try:
            if choice == "1":
                clazz_add()
            elif choice == "2":
                clazz_query_by_id()
            elif choice == "3":
                clazz_query_all()
            elif choice == "4":
                clazz_update()
            elif choice == "5":
                clazz_delete()
            elif choice == "0":
                return
            else:
                print("无效选项")
        except AppException as e:
            print(f"[业务错误] {e.message}")
        except ValueError as e:
            print(f"[输入错误] {e}")
        except Exception as e:
            print(f"[系统错误] {e}")

        pause()


# ============================================================
#                      学生管理
# ============================================================

def student_add():
    """新增学生"""
    student = Student()
    student.stu_num = input_str("学号: ")
    student.name = input_str("姓名: ")
    student.gender = input_str("性别: ")
    student.age = input_int("年龄(可空): ", allow_empty=True)
    student.class_id = input_int("班级ID(可空): ", allow_empty=True)
    student.phone = input_str("手机号: ")
    StudentService.add(student)
    print(f"新增学生成功，ID={student.id}")


def student_query_by_id():
    """按ID查询学生"""
    id = input_int("学生ID: ")
    show_student(StudentService.get_by_id(id))


def student_query_by_stu_num():
    """按学号查询学生"""
    stu_num = input_str("学号: ")
    show_student(StudentService.get_by_stu_num(stu_num))


def student_query_by_class():
    """按班级查询学生"""
    class_id = input_int("班级ID: ")
    show_student_list(StudentService.list_by_class(class_id))


def student_query_all():
    """查询全部学生"""
    show_student_list(StudentService.list_all())


def student_update():
    """更新学生"""
    id = input_int("要修改的学生ID: ")
    exist = StudentService.get_by_id(id)
    if exist is None:
        print(f"学生 ID={id} 不存在")
        return

    print("原数据：")
    show_student(exist)
    print("(不需要修改的字段直接回车跳过)")

    student = Student()
    student.id = id

    stu_num = input_str(f"新学号[{exist.stu_num}]: ")
    student.stu_num = stu_num if stu_num else None

    name = input_str(f"新姓名[{exist.name}]: ")
    student.name = name if name else None

    gender = input_str(f"新性别[{exist.gender}]: ")
    student.gender = gender if gender else None

    age = input_int(f"新年龄[{exist.age}](可空): ", allow_empty=True)
    student.age = age

    class_id = input_int(f"新班级ID[{exist.class_id}](可空): ", allow_empty=True)
    student.class_id = class_id

    phone = input_str(f"新手机号[{exist.phone}]: ")
    student.phone = phone if phone else None

    StudentService.update(student)
    print("更新成功")


def student_delete():
    """删除学生"""
    id = input_int("要删除的学生ID: ")
    exist = StudentService.get_by_id(id)
    if exist is None:
        print(f"学生 ID={id} 不存在")
        return

    print("即将删除：")
    show_student(exist)
    confirm = input_str("确认删除？(y/N): ").lower()
    if confirm != "y":
        print("已取消")
        return

    StudentService.delete(id)
    print("删除成功")


def student_menu():
    """学生管理子菜单"""
    while True:
        print("\n" + "=" * 50)
        print("学生管理")
        print("=" * 50)
        print("1. 新增学生")
        print("2. 按ID查询")
        print("3. 按学号查询")
        print("4. 按班级查询")
        print("5. 查询全部")
        print("6. 更新学生")
        print("7. 删除学生")
        print("0. 返回上级")
        choice = input_str("请选择: ")

        try:
            if choice == "1":
                student_add()
            elif choice == "2":
                student_query_by_id()
            elif choice == "3":
                student_query_by_stu_num()
            elif choice == "4":
                student_query_by_class()
            elif choice == "5":
                student_query_all()
            elif choice == "6":
                student_update()
            elif choice == "7":
                student_delete()
            elif choice == "0":
                return
            else:
                print("无效选项")
        except AppException as e:
            print(f"[业务错误] {e.message}")
        except ValueError as e:
            print(f"[输入错误] {e}")
        except Exception as e:
            print(f"[系统错误] {e}")

        pause()


# ============================================================
#                      课程管理
# ============================================================

def course_add():
    """新增课程"""
    course = Course()
    course.name = input_str("课程名称: ")
    hour = input_int("学时(默认40): ", allow_empty=True)
    course.hour = hour if hour is not None else 40
    CourseService.add(course)
    print(f"新增课程成功，ID={course.id}")


def course_query_by_id():
    """按ID查询课程"""
    id = input_int("课程ID: ")
    show_course(CourseService.get_by_id(id))


def course_query_all():
    """查询全部课程"""
    show_course_list(CourseService.list_all())


def course_update():
    """更新课程"""
    id = input_int("要修改的课程ID: ")
    exist = CourseService.get_by_id(id)
    if exist is None:
        print(f"课程 ID={id} 不存在")
        return

    print("原数据：")
    show_course(exist)
    print("(不需要修改的字段直接回车跳过)")

    course = Course()
    course.id = id

    name = input_str(f"新课程名称[{exist.name}]: ")
    course.name = name if name else None

    hour = input_int(f"新学时[{exist.hour}](可空): ", allow_empty=True)
    course.hour = hour

    CourseService.update(course)
    print("更新成功")


def course_delete():
    """删除课程"""
    id = input_int("要删除的课程ID: ")
    exist = CourseService.get_by_id(id)
    if exist is None:
        print(f"课程 ID={id} 不存在")
        return

    print("即将删除：")
    show_course(exist)
    confirm = input_str("确认删除？(y/N): ").lower()
    if confirm != "y":
        print("已取消")
        return

    CourseService.delete(id)
    print("删除成功")


def course_menu():
    """课程管理子菜单"""
    while True:
        print("\n" + "=" * 50)
        print("课程管理")
        print("=" * 50)
        print("1. 新增课程")
        print("2. 按ID查询")
        print("3. 查询全部")
        print("4. 更新课程")
        print("5. 删除课程")
        print("0. 返回上级")
        choice = input_str("请选择: ")

        try:
            if choice == "1":
                course_add()
            elif choice == "2":
                course_query_by_id()
            elif choice == "3":
                course_query_all()
            elif choice == "4":
                course_update()
            elif choice == "5":
                course_delete()
            elif choice == "0":
                return
            else:
                print("无效选项")
        except AppException as e:
            print(f"[业务错误] {e.message}")
        except ValueError as e:
            print(f"[输入错误] {e}")
        except Exception as e:
            print(f"[系统错误] {e}")

        pause()


# ============================================================
#                      成绩管理
# ============================================================

def score_add():
    """录入成绩"""
    score = Score()
    score.stu_id = input_int("学生ID: ")
    score.course_id = input_int("课程ID: ")
    score.score = input_float("分数: ")
    ScoreService.add(score)
    print(f"新增成绩成功，ID={score.id}")


def score_query_by_id():
    """按ID查询成绩"""
    id = input_int("成绩ID: ")
    show_score(ScoreService.get_by_id(id))


def score_query_by_student():
    """按学生查询成绩"""
    stu_id = input_int("学生ID: ")
    show_score_list(ScoreService.list_by_student(stu_id))


def score_query_by_course():
    """按课程查询成绩"""
    course_id = input_int("课程ID: ")
    show_score_list(ScoreService.list_by_course(course_id))


def score_query_all():
    """查询全部成绩"""
    show_score_list(ScoreService.list_all())


def score_update():
    """更新成绩"""
    id = input_int("要修改的成绩ID: ")
    exist = ScoreService.get_by_id(id)
    if exist is None:
        print(f"成绩 ID={id} 不存在")
        return

    print("原数据：")
    show_score(exist)
    print("(不需要修改的字段直接回车跳过)")

    score = Score()
    score.id = id

    stu_id = input_int(f"新学生ID[{exist.stu_id}](可空): ", allow_empty=True)
    score.stu_id = stu_id

    course_id = input_int(f"新课程ID[{exist.course_id}](可空): ", allow_empty=True)
    score.course_id = course_id

    new_score = input_float(f"新分数[{exist.score}](可空): ", allow_empty=True)
    score.score = new_score

    ScoreService.update(score)
    print("更新成功")


def score_delete():
    """删除成绩"""
    id = input_int("要删除的成绩ID: ")
    exist = ScoreService.get_by_id(id)
    if exist is None:
        print(f"成绩 ID={id} 不存在")
        return

    print("即将删除：")
    show_score(exist)
    confirm = input_str("确认删除？(y/N): ").lower()
    if confirm != "y":
        print("已取消")
        return

    ScoreService.delete(id)
    print("删除成功")


def score_menu():
    """成绩管理子菜单"""
    while True:
        print("\n" + "=" * 50)
        print("成绩管理")
        print("=" * 50)
        print("1. 录入成绩")
        print("2. 按ID查询")
        print("3. 按学生查询")
        print("4. 按课程查询")
        print("5. 查询全部")
        print("6. 更新成绩")
        print("7. 删除成绩")
        print("0. 返回上级")
        choice = input_str("请选择: ")

        try:
            if choice == "1":
                score_add()
            elif choice == "2":
                score_query_by_id()
            elif choice == "3":
                score_query_by_student()
            elif choice == "4":
                score_query_by_course()
            elif choice == "5":
                score_query_all()
            elif choice == "6":
                score_update()
            elif choice == "7":
                score_delete()
            elif choice == "0":
                return
            else:
                print("无效选项")
        except AppException as e:
            print(f"[业务错误] {e.message}")
        except ValueError as e:
            print(f"[输入错误] {e}")
        except Exception as e:
            print(f"[系统错误] {e}")

        pause()


# ============================================================
#                      主菜单
# ============================================================

def main_menu():
    """主菜单"""
    while True:
        print("\n" + "=" * 50)
        print("学生管理系统")
        print("=" * 50)
        print("1. 班级管理")
        print("2. 学生管理")
        print("3. 课程管理")
        print("4. 成绩管理")
        print("0. 退出系统")
        choice = input_str("请选择: ")

        if choice == "1":
            clazz_menu()
        elif choice == "2":
            student_menu()
        elif choice == "3":
            course_menu()
        elif choice == "4":
            score_menu()
        elif choice == "0":
            print("再见")
            break
        else:
            print("无效选项，请重新输入")


if __name__ == '__main__':
    user = login()
    if user:
        main_menu()
    else:
        print("登录失败，程序退出")