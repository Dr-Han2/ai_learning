"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/9 10:18
@Version : 1.0
"""
from core.page_request import PageRequest
from core.page_result import PageResult
from dao.course_dao import CourseDao
from model.course import Course
from core.exceptions import ValidationError, BusinessException
from core import logger
from datetime import datetime
from utils.db_util import DBUtil

log = logger.get_logger()


class CourseService:
    """课程业务类"""

    @staticmethod
    def add(course: Course) -> Course:
        """新增课程记录"""
        if course is None:
            log.warning("课程信息不能为空.")
            raise ValidationError("课程信息不能为空.")
        if course.name is None or course.name.strip() == "":
            log.warning("课程名称不能为空.")
            raise ValidationError("课程名称不能为空.")
        if course.hour is not None and course.hour <= 0:
            log.warning("课程学时必须大于0.")
            raise ValidationError("课程学时必须大于0.")

        now = datetime.now()
        course.create_time = now
        course.update_time = now

        with DBUtil.session_dml() as _:
            row = CourseDao.insert(course)

        if row <= 0:
            log.warning("新增课程记录失败.")
            raise BusinessException("新增课程记录失败.")
        log.info(f"新增课程记录成功. 课程：{course}")
        return course

    @staticmethod
    def update(course: Course) -> Course:
        """更新课程记录"""
        if course is None:
            log.warning("课程信息不能为空.")
            raise ValidationError("课程信息不能为空.")
        if course.id is None:
            log.warning("课程ID不能为空.")
            raise ValidationError("课程ID不能为空.")

        course.update_time = datetime.now()

        with DBUtil.session_dml() as _:
            row = CourseDao.update(course)

        if row <= 0:
            log.warning("更新课程记录失败.")
            raise BusinessException("更新课程记录失败.")
        log.info(f"更新课程记录成功. 课程：{course}")
        return course

    @staticmethod
    def delete(id: int) -> bool:
        """删除课程记录"""
        if id is None:
            log.warning("课程ID不能为空.")
            raise ValidationError("课程ID不能为空.")

        with DBUtil.session_dml() as _:
            row = CourseDao.delete(id)

        if row <= 0:
            log.warning("删除课程记录失败.")
            raise BusinessException("删除课程记录失败.")
        log.info(f"删除课程记录成功. 课程ID：{id}")
        return True

    @staticmethod
    def select_by_id(id: int) -> Course:
        """根据ID查询课程记录"""
        if id is None:
            log.warning("课程ID不能为空.")
            raise ValidationError("课程ID不能为空.")

        with DBUtil.session_readonly() as _:
            course = CourseDao.select_by_id(id)

        return course

    @staticmethod
    def select_by_name(name: str) -> list[Course]:
        """根据名称查询课程记录"""
        if name is None or name.strip() == "":
            log.warning("课程名称不能为空.")
            raise ValidationError("课程名称不能为空.")

        with DBUtil.session_readonly() as _:
            course_list = CourseDao.select_by_name(name)

        return course_list

    @staticmethod
    def select_count() -> int:
        """获取课程记录数"""
        with DBUtil.session_readonly() as _:
            count = CourseDao.select_count()

        return count

    @staticmethod
    def select_page(page_req: PageRequest) -> PageResult[Course]:
        """获取课程记录分页列表"""
        if page_req is None:
            log.warning("分页请求不能为空.")
            raise ValidationError("分页请求不能为空.")

        with DBUtil.session_readonly() as _:
            count = CourseDao.select_count()
            if count <= 0:
                return PageResult.empty(page_req)

            course_list = CourseDao.select_page(
                page_req.order_by,
                page_req.sort,
                page_req.offset,
                page_req.page_size
            )
            result = PageResult.of(page_req, count, course_list)
            return result