"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/9 10:19
@Version : 1.0
"""
from model.socre import Socre
from utils.db_util import DBUtil
from sqlalchemy import text
from core.exceptions import DatabaseError
from core import logger

log = logger.get_logger()


class ScoreDao:
    """成绩数据库操作类"""

    @staticmethod
    def insert(score: Socre) -> int:
        """写入成绩记录"""
        try:
            sql = ("INSERT INTO `t_score` (`stu_id`, `course_id`, `score`, `exam_time`, `create_time`, `update_time`) "
                   " VALUES (:stu_id, :course_id, :score, :exam_time, :create_time, :update_time)")
            params = {
                "stu_id": score.stu_id,
                "course_id": score.course_id,
                "score": score.score,
                "exam_time": score.exam_time,
                "create_time": score.create_time,
                "update_time": score.update_time
            }
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            score.id = result.lastrowid
            return result.rowcount
        except Exception as e:
            log.error("插入成绩记录失败", e)
            raise DatabaseError("插入成绩记录失败", e)

    @staticmethod
    def update(score: Socre) -> int:
        """更新成绩记录"""
        try:
            sql = "UPDATE `t_score` SET `update_time` = :update_time"
            params = {
                "update_time": score.update_time,
                "id": score.id
            }
            if score.score is not None:
                sql += ", `score` = :score"
                params["score"] = score.score
            if score.exam_time is not None:
                sql += ", `exam_time` = :exam_time"
                params["exam_time"] = score.exam_time
            sql += " WHERE `id` = :id"

            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            return result.rowcount
        except Exception as e:
            log.error("更新成绩记录失败", e)
            raise DatabaseError("更新成绩记录失败", e)

    @staticmethod
    def delete(id: int) -> int:
        """删除成绩记录"""
        try:
            sql = "DELETE FROM `t_score` WHERE `id` = :id"
            session = DBUtil.get_session()
            result = session.execute(text(sql), {"id": id})
            return result.rowcount
        except Exception as e:
            log.error("删除成绩记录失败", e)
            raise DatabaseError("删除成绩记录失败", e)

    @staticmethod
    def select_by_id(id: int) -> Socre:
        """根据ID进行查询"""
        try:
            sql = ("SELECT `id`, `stu_id`, `course_id`, `score`, `exam_time`, `create_time`, `update_time` "
                   "FROM `t_score` WHERE `id` = :id")
            session = DBUtil.get_session()
            result = session.execute(text(sql), {"id": id})
            result = result.mappings().fetchone()
            return Socre.from_dict(result)
        except Exception as e:
            log.error("查询成绩记录失败", e)
            raise DatabaseError("查询成绩记录失败", e)

    @staticmethod
    def select_by_stu_id(stu_id: int) -> list[Socre]:
        """根据学生ID进行查询"""
        try:
            sql = ("SELECT `id`, `stu_id`, `course_id`, `score`, `exam_time`, `create_time`, `update_time` "
                   "FROM `t_score` WHERE `stu_id` = :stu_id")
            session = DBUtil.get_session()
            result = session.execute(text(sql), {"stu_id": stu_id})
            result = result.mappings().all()
            return [Socre.from_dict(row) for row in result]
        except Exception as e:
            log.error("查询学生成绩失败", e)
            raise DatabaseError("查询学生成绩失败", e)

    @staticmethod
    def select_by_course_id(course_id: int) -> list[Socre]:
        """根据课程ID进行查询"""
        try:
            sql = ("SELECT `id`, `stu_id`, `course_id`, `score`, `exam_time`, `create_time`, `update_time` "
                   "FROM `t_score` WHERE `course_id` = :course_id")
            session = DBUtil.get_session()
            result = session.execute(text(sql), {"course_id": course_id})
            result = result.mappings().all()
            return [Socre.from_dict(row) for row in result]
        except Exception as e:
            log.error("查询课程成绩失败", e)
            raise DatabaseError("查询课程成绩失败", e)

    @staticmethod
    def select_count() -> int:
        """获取所有成绩记录数"""
        try:
            sql = "SELECT COUNT(*) AS `count` FROM `t_score`"
            session = DBUtil.get_session()
            result = session.execute(text(sql))
            return result.scalar()
        except Exception as e:
            log.error("查询成绩记录数失败", e)
            raise DatabaseError("查询成绩记录数失败", e)

    @staticmethod
    def select_page(order_by: str, sort: str, start: int, num: int) -> list[Socre]:
        """分页查询"""
        sql = (f"SELECT `id`, `stu_id`, `course_id`, `score`, `exam_time`, `create_time`, `update_time` "
               f"FROM `t_score` ORDER BY {order_by} {sort} LIMIT :start, :num")
        params = {
            "start": start,
            "num": num
        }
        session = DBUtil.get_session()
        result = session.execute(text(sql), params)
        result = result.mappings().all()
        return [Socre.from_dict(row) for row in result]