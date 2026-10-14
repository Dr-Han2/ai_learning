"""
@Author  : 刘光尘
@Company : 未来元启
@Date    : 2026/9/11 09:54
@Desc    : 
@Version : 1.0
"""
# 导入工具包
from utils import validation as v
# 导入数据源, 直接导入变量students
from db.database import students
# 导入KEY
from config.kyes import STU_ID, STU_NAME, STU_PHONE
# 导入异常包
from exception.exceptions import ParamError, ServiceError


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
        raise ParamError("学号不能为空")
    # 校验姓名是否为空
    if not stu_name:
        raise ParamError("姓名不能为空")
    # 校验手机号是否为空
    checked_phone_num = v.check_phone_num(stu_phone)
    if not checked_phone_num:
        raise ParamError("手机号格式错误")

    # 把学号转成大写
    stu_id = stu_id.upper()
    # 检查学号是否重复
    if stu_id in students:
        raise ServiceError("学号已存在")

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
        raise ParamError("学号不能为空")

    # 学号转大写
    stu_id = stu_id.upper()
    # 检查学号是否存在
    if stu_id not in students:
        raise ServiceError("学号不存在")

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
        raise ParamError("学号不能为空")
    # 学号转大写
    stu_id = stu_id.upper()
    # 检查学号是否存在
    if stu_id not in students:
        raise ServiceError("学号不存在")
    # 校验姓名是否为空
    if not stu_name:
        raise ParamError("姓名不能为空")
    # 校验手机号是否为空
    checked_phone_num = v.check_phone_num(stu_phone)
    if not checked_phone_num:
        raise ParamError("手机号格式错误")


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
        raise ParamError("学号不能为空")
    # 学号转大写
    stu_id = stu_id.upper()
    # 检查学号是否存在
    if stu_id not in students:
        raise ServiceError("学号不存在")


    # 返回学生信息
    return students[stu_id], "查询成功"

# 查询所有学生信息
def query_all_students():

    """
    查询所有学生信息
    :return: 所有学生信息
    """
    return students, "查询成功"