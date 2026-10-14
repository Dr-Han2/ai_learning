"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/9 10:19
@Version : 1.0
"""
from core.page_request import PageRequest
from core.page_result import PageResult
from dao.student_dao import StudentDao
from model.student import Student
from core.exceptions import ValidationError, BusinessException
from core import logger
from datetime import datetime
from utils.db_util import DBUtil

log = logger.get_logger()


class StudentService:
    """学生业务类"""

    @staticmethod
    def add(student: Student) -> Student:
        """新增学生记录"""
        if student is None:
            log.warning("学生信息不能为空.")
            raise ValidationError("学生信息不能为空.")
        if student.stu_num is None or student.stu_num.strip() == "":
            log.warning("学生学号不能为空.")
            raise ValidationError("学生学号不能为空.")
        if student.name is None or student.name.strip() == "":
            log.warning("学生姓名不能为空.")
            raise ValidationError("学生姓名不能为空.")
        if student.gender not in ("男", "女"):
            log.warning("学生性别只能是 男 或 女.")
            raise ValidationError("学生性别只能是 男 或 女.")
        if student.age is None or student.age <= 0:
            log.warning("学生年龄不合法.")
            raise ValidationError("学生年龄不合法.")
        if student.class_id is None or student.class_id <= 0:
            log.warning("所属班级ID不能为空.")
            raise ValidationError("所属班级ID不能为空.")

        now = datetime.now()
        student.create_time = now
        student.update_time = now

        with DBUtil.session_dml() as _:
            row = StudentDao.insert(student)

        if row <= 0:
            log.warning("新增学生记录失败.")
            raise BusinessException("新增学生记录失败.")
        log.info(f"新增学生记录成功. 学生：{student}")
        return student

    @staticmethod
    def update(student: Student) -> Student:
        """更新学生记录"""
        if student is None:
            log.warning("学生信息不能为空.")
            raise ValidationError("学生信息不能为空.")
        if student.id is None:
            log.warning("学生ID不能为空.")
            raise ValidationError("学生ID不能为空.")

        student.update_time = datetime.now()

        with DBUtil.session_dml() as _:
            row = StudentDao.update(student)

        if row <= 0:
            log.warning("更新学生记录失败.")
            raise BusinessException("更新学生记录失败.")
        log.info(f"更新学生记录成功. 学生：{student}")
        return student

    @staticmethod
    def delete(id: int) -> bool:
        """删除学生记录"""
        if id is None:
            log.warning("学生ID不能为空.")
            raise ValidationError("学生ID不能为空.")

        with DBUtil.session_dml() as _:
            row = StudentDao.delete(id)

        if row <= 0:
            log.warning("删除学生记录失败.")
            raise BusinessException("删除学生记录失败.")
        log.info(f"删除学生记录成功. 学生ID：{id}")
        return True

    @staticmethod
    def select_by_id(id: int) -> Student:
        """根据ID查询学生记录"""
        if id is None:
            log.warning("学生ID不能为空.")
            raise ValidationError("学生ID不能为空.")

        with DBUtil.session_readonly() as _:
            student = StudentDao.select_by_id(id)

        return student

    @staticmethod
    def select_by_name(name: str) -> list[Student]:
        """根据姓名查询学生记录"""
        if name is None or name.strip() == "":
            log.warning("学生姓名不能为空.")
            raise ValidationError("学生姓名不能为空.")

        with DBUtil.session_readonly() as _:
            student_list = StudentDao.select_by_name(name)

        return student_list

    @staticmethod
    def select_by_stu_num(stu_num: str) -> Student:
        """根据学号查询学生记录"""
        if stu_num is None or stu_num.strip() == "":
            log.warning("学生学号不能为空.")
            raise ValidationError("学生学号不能为空.")

        with DBUtil.session_readonly() as _:
            student = StudentDao.select_by_stu_num(stu_num)

        return student

    @staticmethod
    def select_by_class_id(class_id: int) -> list[Student]:
        """根据班级ID查询学生记录"""
        if class_id is None:
            log.warning("班级ID不能为空.")
            raise ValidationError("班级ID不能为空.")

        with DBUtil.session_readonly() as _:
            student_list = StudentDao.select_by_class_id(class_id)

        return student_list

    @staticmethod
    def select_count() -> int:
        """获取学生记录数"""
        with DBUtil.session_readonly() as _:
            count = StudentDao.select_count()

        return count

    @staticmethod
    def select_page(page_req: PageRequest) -> PageResult[Student]:
        """获取学生记录分页列表"""
        if page_req is None:
            log.warning("分页请求不能为空.")
            raise ValidationError("分页请求不能为空.")

        with DBUtil.session_readonly() as _:
            count = StudentDao.select_count()
            if count <= 0:
                return PageResult.empty(page_req)

            student_list = StudentDao.select_page(
                page_req.order_by,
                page_req.sort,
                page_req.offset,
                page_req.page_size
            )
            result = PageResult.of(page_req, count, student_list)
            return result