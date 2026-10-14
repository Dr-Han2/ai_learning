"""
@Author  : hanhao
@Company : 未来元启
@Date    : 2026/10/9 10:19
@Desc    : 
@Version : 1.0
"""
from datetime import datetime

from model.score import Score
from dao.score_dao import ScoreDao
from dao.student_dao import StudentDao
from dao.course_dao import CourseDao
from core.exceptions import ValidationError, NotFoundError, AlreadyExistsError, BusinessException
from core import logger

# 日志对象
log = logger.get_logger()


class ScoreService:
    """成绩业务逻辑层"""

    @staticmethod
    def _validate_score_range(value):
        """成绩范围校验"""
        if value is not None and not (0 <= value <= 100):
            raise ValidationError("成绩必须在 0-100 之间", field="score", value=value)

    @staticmethod
    def _validate_student_exists(stu_id):
        """学生存在性校验"""
        if stu_id is None:
            raise ValidationError("学生 ID 不能为空", field="stu_id")
        if StudentDao.select_by_id(stu_id) is None:
            raise NotFoundError("学生", stu_id)

    @staticmethod
    def _validate_course_exists(course_id):
        """课程存在性校验"""
        if course_id is None:
            raise ValidationError("课程 ID 不能为空", field="course_id")
        if CourseDao.select_by_id(course_id) is None:
            raise NotFoundError("课程", course_id)

    @staticmethod
    def add(score: Score) -> int:
        """新增成绩"""
        if score is None:
            raise ValidationError("成绩信息不能为空")
        ScoreService._validate_student_exists(score.stu_id)
        ScoreService._validate_course_exists(score.course_id)
        ScoreService._validate_score_range(score.score)

        # 同一学生同一课程是否已有成绩
        if ScoreDao.select_by_stu_and_course(score.stu_id, score.course_id) is not None:
            raise AlreadyExistsError("成绩", field="stu_id+course_id",
                                     value=f"{score.stu_id}+{score.course_id}")

        now = datetime.now()
        score.create_time = now
        score.update_time = now
        row = ScoreDao.insert(score)
        if row <= 0:
            raise BusinessException("新增成绩记录失败")
        log.info("新增成绩成功 id=%s stu_id=%s course_id=%s",
                 score.id, score.stu_id, score.course_id)
        return row

    @staticmethod
    def update(score: Score) -> int:
        """更新成绩"""
        if score is None or score.id is None:
            raise ValidationError("更新时必须传入成绩 ID", field="id")

        # 成绩存在性校验
        exist = ScoreDao.select_by_id(score.id)
        if exist is None:
            raise NotFoundError("成绩", score.id)

        # 如果传入了新学生ID / 课程ID，校验存在性
        if score.stu_id is not None:
            ScoreService._validate_student_exists(score.stu_id)
        if score.course_id is not None:
            ScoreService._validate_course_exists(score.course_id)

        # 如果改了学生或课程，检查组合是否和别的记录冲突
        new_stu_id = score.stu_id if score.stu_id is not None else exist.stu_id
        new_course_id = score.course_id if score.course_id is not None else exist.course_id
        if new_stu_id != exist.stu_id or new_course_id != exist.course_id:
            conflict = ScoreDao.select_by_stu_and_course(new_stu_id, new_course_id)
            if conflict is not None and conflict.id != score.id:
                raise AlreadyExistsError("成绩", field="stu_id+course_id",
                                         value=f"{new_stu_id}+{new_course_id}")

        ScoreService._validate_score_range(score.score)

        score.update_time = datetime.now()
        row = ScoreDao.update(score)
        if row == 0:
            log.warning("更新成绩失败，未找到 id=%s", score.id)
        return row

    @staticmethod
    def delete(id: int) -> int:
        """删除成绩"""
        if id is None:
            raise ValidationError("删除时必须传入成绩 ID", field="id")
        row = ScoreDao.delete(id)
        if row == 0:
            log.warning("删除成绩失败，未找到 id=%s", id)
        return row

    @staticmethod
    def get_by_id(id: int) -> Score:
        """按ID查询成绩"""
        return ScoreDao.select_by_id(id)

    @staticmethod
    def list_by_student(stu_id: int) -> list[Score]:
        """查询某学生的所有成绩"""
        if stu_id is None:
            raise ValidationError("学生 ID 不能为空", field="stu_id")
        return ScoreDao.select_by_stu_id(stu_id)

    @staticmethod
    def list_by_course(course_id: int) -> list[Score]:
        """查询某课程的所有成绩"""
        if course_id is None:
            raise ValidationError("课程 ID 不能为空", field="course_id")
        return ScoreDao.select_by_course_id(course_id)

    @staticmethod
    def list_all() -> list[Score]:
        """查询全部成绩"""
        return ScoreDao.select_all()


if __name__ == '__main__':
    score = Score()
    score.stu_id = 1
    score.course_id = 1
    score.score = 90.0
    ScoreService.add(score)
    print("新增成绩ID:", score.id)