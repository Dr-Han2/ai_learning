"""
@Author  : hanhao
@Company : 未来元启
@Date    : 2026/10/9 10:19
@Desc    : 
@Version : 1.0
"""
from model.score import Score
from utils.db_util import DBUtil
from sqlalchemy import text

from core.exceptions import DatabaseError
from core import logger

log = logger.get_logger()


class ScoreDao:
    """成绩数据库操作类"""

    # 公用查询列
    _COLUMNS = ("`id`, `stu_id`, `course_id`, `score`, `exam_time`, "
                "`create_time`, `update_time`")

    @staticmethod
    def insert(score: Score) -> int:
        """写入成绩记录"""
        session = None
        try:
            sql = ("INSERT INTO `t_score`"
                   "(`stu_id`, `course_id`, `score`, `exam_time`, `create_time`, `update_time`) "
                   "VALUES (:stu_id, :course_id, :score, :exam_time, :create_time, :update_time)")
            params = {
                "stu_id": score.stu_id,
                "course_id": score.course_id,
                "score": score.score,
                "exam_time": score.exam_time,
                "create_time": score.create_time,
                "update_time": score.update_time,
            }
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            session.commit()                          # ← 提交事务
            score.id = result.lastrowid               # ← 回填自增主键
            return result.rowcount                    # ← 返回受影响行数
        except Exception as e:
            if session:
                session.rollback()                    # ← 失败回滚
            log.exception("插入成绩记录失败")           # ← 自动带堆栈
            raise DatabaseError(e) from e             # ← 保留原因链
        finally:
            if session:
                session.close()

    @staticmethod
    def update(score: Score) -> int:
        """更新成绩记录（动态拼 SQL，只更新传入的字段）"""
        session = None
        try:
            sql = "UPDATE `t_score` SET `update_time` = :update_time"
            params = {"update_time": score.update_time, "id": score.id}

            # 动态构造SQL，学生ID是否传入
            if score.stu_id is not None:
                sql += ", `stu_id` = :stu_id"
                params["stu_id"] = score.stu_id
            # 课程ID是否传入
            if score.course_id is not None:
                sql += ", `course_id` = :course_id"
                params["course_id"] = score.course_id
            # 分数是否传入
            if score.score is not None:
                sql += ", `score` = :score"
                params["score"] = score.score
            # 考试日期是否传入
            if score.exam_time is not None:
                sql += ", `exam_time` = :exam_time"
                params["exam_time"] = score.exam_time
            # 构造更新条件
            sql += " WHERE `id` = :id"

            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            session.commit()                          # ← 提交
            return result.rowcount
        except Exception as e:
            if session:
                session.rollback()
            log.exception("更新成绩记录失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def delete(id: int) -> int:
        """删除成绩记录"""
        session = None
        try:
            sql = "DELETE FROM `t_score` WHERE `id` = :id"
            params = {"id": id}
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            session.commit()                          # ← 提交
            return result.rowcount
        except Exception as e:
            if session:
                session.rollback()
            log.exception("删除成绩记录失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def select_by_id(id: int) -> Score:
        """根据ID进行查询"""
        session = None
        try:
            sql = f"SELECT {ScoreDao._COLUMNS} FROM `t_score` WHERE `id` = :id"
            params = {"id": id}
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            row = result.mappings().fetchone()
            return Score.from_dict(row)
        except Exception as e:
            log.exception("按ID查询成绩失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def select_by_stu_id(stu_id: int) -> list[Score]:
        """根据学生ID查询成绩列表"""
        session = None
        try:
            sql = (f"SELECT {ScoreDao._COLUMNS} FROM `t_score` "
                   f"WHERE `stu_id` = :stu_id ORDER BY `id`")
            params = {"stu_id": stu_id}
            session = DBUtil.get_session()
            rows = session.execute(text(sql), params).mappings().fetchall()
            return [Score.from_dict(r) for r in rows]
        except Exception as e:
            log.exception("按学生查询成绩失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def select_by_course_id(course_id: int) -> list[Score]:
        """根据课程ID查询成绩列表"""
        session = None
        try:
            sql = (f"SELECT {ScoreDao._COLUMNS} FROM `t_score` "
                   f"WHERE `course_id` = :course_id ORDER BY `id`")
            params = {"course_id": course_id}
            session = DBUtil.get_session()
            rows = session.execute(text(sql), params).mappings().fetchall()
            return [Score.from_dict(r) for r in rows]
        except Exception as e:
            log.exception("按课程查询成绩失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def select_by_stu_and_course(stu_id: int, course_id: int) -> Score:
        """根据学生+课程查询唯一成绩"""
        session = None
        try:
            sql = (f"SELECT {ScoreDao._COLUMNS} FROM `t_score` "
                   f"WHERE `stu_id` = :stu_id AND `course_id` = :course_id")
            params = {"stu_id": stu_id, "course_id": course_id}
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            row = result.mappings().first()
            return Score.from_dict(row)
        except Exception as e:
            log.exception("按学生+课程查询成绩失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def select_all() -> list[Score]:
        """查询全部成绩"""
        session = None
        try:
            sql = f"SELECT {ScoreDao._COLUMNS} FROM `t_score` ORDER BY `id`"
            session = DBUtil.get_session()
            rows = session.execute(text(sql)).mappings().fetchall()
            return [Score.from_dict(r) for r in rows]
        except Exception as e:
            log.exception("查询全部成绩失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()