"""
@Author  : hanhao
@Company : 未来元启
@Date    : 2026/10/9 10:19
@Desc    : 
@Version : 1.0
"""
from model.course import Course
from utils.db_util import DBUtil
from sqlalchemy import text

from core.exceptions import DatabaseError
from core import logger

log = logger.get_logger()


class CourseDao:
    """课程数据库操作类"""

    _COLUMNS = "`id`, `name`, `hour`, `create_time`, `update_time`"

    @staticmethod
    def insert(course: Course) -> int:
        session = None
        try:
            sql = ("INSERT INTO `t_course`(`name`, `hour`, `create_time`, `update_time`) "
                   "VALUES (:name, :hour, :create_time, :update_time)")
            params = {
                "name": course.name,
                "hour": course.hour,
                "create_time": course.create_time,
                "update_time": course.update_time,
            }
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            session.commit()
            course.id = result.lastrowid
            return result.rowcount
        except Exception as e:
            if session:
                session.rollback()
            log.exception("插入课程记录失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def update(course: Course) -> int:
        session = None
        try:
            sql = "UPDATE `t_course` SET `update_time` = :update_time"
            params = {"update_time": course.update_time, "id": course.id}

            if course.name is not None and course.name.strip() != "":
                sql += ", `name` = :name"
                params["name"] = course.name
            if course.hour is not None:
                sql += ", `hour` = :hour"
                params["hour"] = course.hour
            sql += " WHERE `id` = :id"

            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            session.commit()
            return result.rowcount
        except Exception as e:
            if session:
                session.rollback()
            log.exception("更新课程记录失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def delete(id: int) -> int:
        session = None
        try:
            session = DBUtil.get_session()
            result = session.execute(text("DELETE FROM `t_course` WHERE `id` = :id"), {"id": id})
            session.commit()
            return result.rowcount
        except Exception as e:
            if session:
                session.rollback()
            log.exception("删除课程记录失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def select_by_id(id: int) -> Course:
        session = None
        try:
            sql = f"SELECT {CourseDao._COLUMNS} FROM `t_course` WHERE `id` = :id"
            session = DBUtil.get_session()
            row = session.execute(text(sql), {"id": id}).mappings().fetchone()
            return Course.from_dict(row)
        except Exception as e:
            log.exception("按ID查询课程失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def select_by_name(name: str) -> list[Course]:
        """按名称模糊查询（用于搜索）"""
        session = None
        try:
            sql = f"SELECT {CourseDao._COLUMNS} FROM `t_course` WHERE `name` LIKE :name"
            session = DBUtil.get_session()
            rows = session.execute(text(sql), {"name": f"%{name}%"}).mappings().fetchall()
            return [Course.from_dict(r) for r in rows]
        except Exception as e:
            log.exception("按名称查询课程失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def select_by_name_exact(name: str) -> Course:
        """按名称精确查询（用于唯一性校验）"""
        session = None
        try:
            sql = f"SELECT {CourseDao._COLUMNS} FROM `t_course` WHERE `name` = :name"
            session = DBUtil.get_session()
            row = session.execute(text(sql), {"name": name}).mappings().first()
            return Course.from_dict(row)
        except Exception as e:
            log.exception("按名称精确查询课程失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def select_all() -> list[Course]:
        session = None
        try:
            sql = f"SELECT {CourseDao._COLUMNS} FROM `t_course` ORDER BY `id`"
            session = DBUtil.get_session()
            rows = session.execute(text(sql)).mappings().fetchall()
            return [Course.from_dict(r) for r in rows]
        except Exception as e:
            log.exception("查询全部课程失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()