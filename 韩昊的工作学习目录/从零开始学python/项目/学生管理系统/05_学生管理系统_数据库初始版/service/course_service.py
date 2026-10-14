"""
@Author  : hanhao
@Company : 未来元启
@Date    : 2026/10/9 10:18
@Desc    : 
@Version : 1.0
"""
from datetime import datetime

from model.course import Course
from dao.course_dao import CourseDao
from core.exceptions import ValidationError, AlreadyExistsError, BusinessException, NotFoundError
from core import logger

# 日志对象
log = logger.get_logger()


class CourseService:
    """课程业务逻辑层"""

    @staticmethod
    def add(course: Course) -> int:
        """新增课程"""
        # 校验
        if course is None:
            log.warning("课程信息不能为空.")
            raise ValidationError("课程信息不能为空.")
        if not course.name or not course.name.strip():
            log.warning("课程名称不能为空.")
            raise ValidationError("课程名称不能为空.", field="name")
        # 唯一性校验：精确匹配
        if CourseDao.select_by_name_exact(course.name) is not None:
            log.warning("课程名称已存在.")
            raise AlreadyExistsError("课程", field="name", value=course.name)
        if course.hour is not None and course.hour <= 0:
            log.warning("课程学时必须为正整数.")
            raise ValidationError("课程学时必须为正整数.", field="hour")

        # 设置创建和更新时间
        now = datetime.now()
        course.create_time = now
        course.update_time = now

        row = CourseDao.insert(course)
        if row <= 0:
            log.warning("新增课程记录失败.")
            raise BusinessException("新增课程记录失败.")
        log.info("新增课程成功 id=%s name=%s", course.id, course.name)
        return row

    @staticmethod
    def update(course: Course) -> int:
        """更新课程"""
        if course is None or course.id is None:
            raise ValidationError("更新时必须传入课程 ID", field="id")

        # 课程存在性校验
        exist = CourseDao.select_by_id(course.id)
        if exist is None:
            raise NotFoundError("课程", course.id)

        # 如果传入了新课程名，检查是否和其他课程冲突
        if course.name is not None and course.name.strip() != "":
            conflict = CourseDao.select_by_name_exact(course.name)
            if conflict is not None and conflict.id != course.id:
                raise AlreadyExistsError("课程", field="name", value=course.name)

        if course.hour is not None and course.hour <= 0:
            raise ValidationError("课程学时必须为正整数", field="hour")

        course.update_time = datetime.now()
        row = CourseDao.update(course)
        if row == 0:
            log.warning("更新课程失败，未找到 id=%s", course.id)
        return row

    @staticmethod
    def delete(id: int) -> int:
        """删除课程"""
        if id is None:
            raise ValidationError("删除时必须传入课程 ID", field="id")
        row = CourseDao.delete(id)
        if row == 0:
            log.warning("删除课程失败，未找到 id=%s", id)
        return row

    @staticmethod
    def get_by_id(id: int) -> Course:
        """按ID查询课程"""
        return CourseDao.select_by_id(id)

    @staticmethod
    def list_all() -> list[Course]:
        """查询全部课程"""
        return CourseDao.select_all()


if __name__ == '__main__':
    course = Course()
    course.name = "测试课程"
    course.hour = 40
    CourseService.add(course)
    print("新增课程ID:", course.id)