"""
@Author  : hanhao
@Company : 未来元启
@Date    : 2026/10/9 10:19
@Desc    : 
@Version : 1.0
"""
from datetime import datetime

from model.student import Student
from dao.student_dao import StudentDao
from dao.clazz_dao import ClazzDao
from core.exceptions import ValidationError, AlreadyExistsError, NotFoundError, BusinessException
from core import logger

# 日志对象
log = logger.get_logger()


class StudentService:
    """学生业务逻辑层"""

    @staticmethod
    def _validate_age(age):
        """年龄范围校验"""
        if age is not None and not (1 <= age <= 150):
            raise ValidationError("年龄必须在 1-150 之间", field="age", value=age)

    @staticmethod
    def _validate_class_id(class_id):
        """班级ID校验：不能为0，且必须存在"""
        if class_id is None:
            return
        if class_id <= 0:
            raise ValidationError("班级 ID 必须为正整数", field="class_id", value=class_id)
        if ClazzDao.select_by_id(class_id) is None:
            raise NotFoundError("班级", class_id)

    @staticmethod
    def _validate_phone(phone):
        """手机号校验：11 位数字"""
        if phone is None or phone.strip() == "":
            return
        if not phone.isdigit() or len(phone) != 11:
            raise ValidationError("手机号必须为 11 位数字", field="phone", value=phone)

    @staticmethod
    def add(student: Student) -> int:
        """新增学生"""
        # 1. 必填校验
        if student is None:
            raise ValidationError("学生信息不能为空")
        if not student.name or not student.name.strip():
            raise ValidationError("学生姓名不能为空", field="name")
        if not student.stu_num or not student.stu_num.strip():
            raise ValidationError("学号不能为空", field="stu_num")

        # 2. 学号唯一性校验
        if StudentDao.select_by_stu_num(student.stu_num) is not None:
            raise AlreadyExistsError("学生", field="stu_num", value=student.stu_num)

        # 3. 班级、年龄、手机号校验
        StudentService._validate_class_id(student.class_id)
        StudentService._validate_age(student.age)
        StudentService._validate_phone(student.phone)

        # 4. 时间字段
        now = datetime.now()
        student.create_time = now
        student.update_time = now

        # 5. 调用 DAO
        row = StudentDao.insert(student)
        if row <= 0:
            raise BusinessException("新增学生记录失败")
        log.info("新增学生成功 id=%s stu_num=%s", student.id, student.stu_num)
        return row

    @staticmethod
    def update(student: Student) -> int:
        """更新学生"""
        if student is None or student.id is None:
            raise ValidationError("更新时必须传入学生 ID", field="id")

        # 学生存在性校验
        exist = StudentDao.select_by_id(student.id)
        if exist is None:
            raise NotFoundError("学生", student.id)

        # 如果传入了新学号，校验它不能和其他学生冲突
        if student.stu_num is not None and student.stu_num.strip() != "":
            conflict = StudentDao.select_by_stu_num(student.stu_num)
            if conflict is not None and conflict.id != student.id:
                raise AlreadyExistsError("学生", field="stu_num", value=student.stu_num)

        # 班级、年龄、手机号校验
        StudentService._validate_class_id(student.class_id)
        StudentService._validate_age(student.age)
        StudentService._validate_phone(student.phone)

        student.update_time = datetime.now()
        row = StudentDao.update(student)
        if row == 0:
            log.warning("更新学生失败，未找到 id=%s", student.id)
        return row

    @staticmethod
    def delete(id: int) -> int:
        """删除学生"""
        if id is None:
            raise ValidationError("删除时必须传入学生 ID", field="id")
        row = StudentDao.delete(id)
        if row == 0:
            log.warning("删除学生失败，未找到 id=%s", id)
        return row

    @staticmethod
    def get_by_id(id: int) -> Student:
        """按主键查询学生"""
        return StudentDao.select_by_id(id)

    @staticmethod
    def get_by_stu_num(stu_num: str) -> Student:
        """按学号查询学生"""
        return StudentDao.select_by_stu_num(stu_num)

    @staticmethod
    def list_by_class(class_id: int) -> list[Student]:
        """查询某个班级的学生列表"""
        if class_id is None:
            raise ValidationError("班级 ID 不能为空", field="class_id")
        return StudentDao.select_by_class_id(class_id)

    @staticmethod
    def list_all() -> list[Student]:
        """查询所有学生"""
        return StudentDao.select_all()


if __name__ == '__main__':
    student = Student()
    student.stu_num = "S2025001"
    student.name = "测试学生"
    student.gender = "男"
    student.age = 20
    student.class_id = 1
    student.phone = "13800000000"
    StudentService.add(student)
    print("新增学生ID:", student.id)