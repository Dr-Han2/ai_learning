"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/9 10:19
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

    @staticmethod
    def insert(course: Course) -> int:
        """写入课程记录"""
        try:
            sql = ("INSERT INTO `t_course` (`name`, `hour`, `create_time`, `update_time`) "
                   " VALUES (:name, :hour, :create_time, :update_time)")
            params = {
                "name": course.name,
                "hour": course.hour,
                "create_time": course.create_time,
                "update_time": course.update_time
            }
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            course.id = result.lastrowid
            return result.rowcount
        except Exception as e:
            log.error("插入课程记录失败", e)
            raise DatabaseError("插入课程记录失败", e)

    @staticmethod
    def update(course: Course) -> int:
        """更新课程记录"""
        try:
            sql = "UPDATE `t_course` SET `update_time` = :update_time"
            params = {
                "update_time": course.update_time,
                "id": course.id
            }
            if course.name is not None and course.name.strip() != "":
                sql += ", `name` = :name"
                params["name"] = course.name
            if course.hour is not None:
                sql += ", `hour` = :hour"
                params["hour"] = course.hour
            sql += " WHERE `id` = :id"

            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            return result.rowcount
        except Exception as e:
            log.error("更新课程记录失败", e)
            raise DatabaseError("更新课程记录失败", e)

    @staticmethod
    def delete(id: int) -> int:
        """删除课程记录"""
        try:
            sql = "DELETE FROM `t_course` WHERE `id` = :id"
            session = DBUtil.get_session()
            result = session.execute(text(sql), {"id": id})
            return result.rowcount
        except Exception as e:
            log.error("删除课程记录失败", e)
            raise DatabaseError("删除课程记录失败", e)

    @staticmethod
    def select_by_id(id: int) -> Course:
        """根据ID进行查询"""
        try:
            sql = ("SELECT `id`, `name`, `hour`, `create_time`, `update_time` "
                   "FROM `t_course` WHERE `id` = :id")
            session = DBUtil.get_session()
            result = session.execute(text(sql), {"id": id})
            result = result.mappings().fetchone()
            return Course.from_dict(result)
        except Exception as e:
            log.error("查询课程记录失败", e)
            raise DatabaseError("查询课程记录失败", e)

    @staticmethod
    def select_by_name(name: str) -> list[Course]:
        """根据课程名进行查询"""
        try:
            sql = ("SELECT `id`, `name`, `hour`, `create_time`, `update_time` "
                   "FROM `t_course` WHERE `name` = :name")
            session = DBUtil.get_session()
            result = session.execute(text(sql), {"name": name})
            result = result.mappings().all()
            return [Course.from_dict(row) for row in result]
        except Exception as e:
            log.error("查询课程记录失败", e)
            raise DatabaseError("查询课程记录失败", e)

    @staticmethod
    def select_count() -> int:
        """获取所有课程记录数"""
        try:
            sql = "SELECT COUNT(*) AS `count` FROM `t_course`"
            session = DBUtil.get_session()
            result = session.execute(text(sql))
            return result.scalar()
        except Exception as e:
            log.error("查询课程记录数失败", e)
            raise DatabaseError("查询课程记录数失败", e)

    @staticmethod
    def select_page(order_by: str, sort: str, start: int, num: int) -> list[Course]:
        """分页查询"""
        sql = (f"SELECT `id`, `name`, `hour`, `create_time`, `update_time` "
               f"FROM `t_course` ORDER BY {order_by} {sort} LIMIT :start, :num")
        params = {
            "start": start,
            "num": num
        }
        session = DBUtil.get_session()
        result = session.execute(text(sql), params)
        result = result.mappings().all()
        return [Course.from_dict(row) for row in result]