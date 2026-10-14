"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/9 10:19
@Version : 1.0
"""
from core.page_request import PageRequest
from core.page_result import PageResult
from dao.socre_dao import ScoreDao
from model.socre import Socre
from core.exceptions import ValidationError, BusinessException
from core import logger
from datetime import datetime
from utils.db_util import DBUtil

log = logger.get_logger()


class ScoreService:
    """成绩业务类"""

    @staticmethod
    def add(score: Socre) -> Socre:
        """新增成绩记录"""
        if score is None:
            log.warning("成绩信息不能为空.")
            raise ValidationError("成绩信息不能为空.")
        if score.stu_id is None or score.stu_id <= 0:
            log.warning("学生ID不能为空.")
            raise ValidationError("学生ID不能为空.")
        if score.course_id is None or score.course_id <= 0:
            log.warning("课程ID不能为空.")
            raise ValidationError("课程ID不能为空.")
        if score.score is None or score.score < 0 or score.score > 100:
            log.warning("分数必须在 0-100 之间.")
            raise ValidationError("分数必须在 0-100 之间.")

        now = datetime.now()
        score.create_time = now
        score.update_time = now

        with DBUtil.session_dml() as _:
            row = ScoreDao.insert(score)

        if row <= 0:
            log.warning("新增成绩记录失败.")
            raise BusinessException("新增成绩记录失败.")
        log.info(f"新增成绩记录成功. 成绩：{score}")
        return score

    @staticmethod
    def update(score: Socre) -> Socre:
        """更新成绩记录"""
        if score is None:
            log.warning("成绩信息不能为空.")
            raise ValidationError("成绩信息不能为空.")
        if score.id is None:
            log.warning("成绩ID不能为空.")
            raise ValidationError("成绩ID不能为空.")
        if score.score is not None and (score.score < 0 or score.score > 100):
            log.warning("分数必须在 0-100 之间.")
            raise ValidationError("分数必须在 0-100 之间.")

        score.update_time = datetime.now()

        with DBUtil.session_dml() as _:
            row = ScoreDao.update(score)

        if row <= 0:
            log.warning("更新成绩记录失败.")
            raise BusinessException("更新成绩记录失败.")
        log.info(f"更新成绩记录成功. 成绩：{score}")
        return score

    @staticmethod
    def delete(id: int) -> bool:
        """删除成绩记录"""
        if id is None:
            log.warning("成绩ID不能为空.")
            raise ValidationError("成绩ID不能为空.")

        with DBUtil.session_dml() as _:
            row = ScoreDao.delete(id)

        if row <= 0:
            log.warning("删除成绩记录失败.")
            raise BusinessException("删除成绩记录失败.")
        log.info(f"删除成绩记录成功. 成绩ID：{id}")
        return True

    @staticmethod
    def select_by_id(id: int) -> Socre:
        """根据ID查询成绩记录"""
        if id is None:
            log.warning("成绩ID不能为空.")
            raise ValidationError("成绩ID不能为空.")

        with DBUtil.session_readonly() as _:
            score = ScoreDao.select_by_id(id)

        return score

    @staticmethod
    def select_by_stu_id(stu_id: int) -> list[Socre]:
        """根据学生ID查询成绩记录"""
        if stu_id is None:
            log.warning("学生ID不能为空.")
            raise ValidationError("学生ID不能为空.")

        with DBUtil.session_readonly() as _:
            score_list = ScoreDao.select_by_stu_id(stu_id)

        return score_list

    @staticmethod
    def select_by_course_id(course_id: int) -> list[Socre]:
        """根据课程ID查询成绩记录"""
        if course_id is None:
            log.warning("课程ID不能为空.")
            raise ValidationError("课程ID不能为空.")

        with DBUtil.session_readonly() as _:
            score_list = ScoreDao.select_by_course_id(course_id)

        return score_list

    @staticmethod
    def select_count() -> int:
        """获取成绩记录数"""
        with DBUtil.session_readonly() as _:
            count = ScoreDao.select_count()

        return count

    @staticmethod
    def select_page(page_req: PageRequest) -> PageResult[Socre]:
        """获取成绩记录分页列表"""
        if page_req is None:
            log.warning("分页请求不能为空.")
            raise ValidationError("分页请求不能为空.")

        with DBUtil.session_readonly() as _:
            count = ScoreDao.select_count()
            if count <= 0:
                return PageResult.empty(page_req)

            score_list = ScoreDao.select_page(
                page_req.order_by,
                page_req.sort,
                page_req.offset,
                page_req.page_size
            )
            result = PageResult.of(page_req, count, score_list)
            return result