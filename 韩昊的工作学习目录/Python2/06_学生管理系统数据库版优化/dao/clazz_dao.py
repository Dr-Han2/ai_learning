"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/9 10:19
@Version : 1.0
"""
from model.clazz import Clazz
from utils.db_util import DBUtil
from sqlalchemy import text
from core.exceptions import DatabaseError
from core import logger

log = logger.get_logger()


class ClazzDao:
    """班级数据库操作类"""

    @staticmethod
    def insert(clazz: Clazz) -> int:
        """写入班级记录"""
        try:
            sql = ("INSERT INTO `t_class` (`name`, `teacher_name`, `create_time`, `update_time`) "
                   " VALUES (:name, :teacher_name, :create_time, :update_time)")
            params = {
                "name": clazz.name,
                "teacher_name": clazz.teacher_name,
                "create_time": clazz.create_time,
                "update_time": clazz.update_time
            }
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            clazz.id = result.lastrowid
            return result.rowcount
        except Exception as e:
            log.error("插入班级记录失败", e)
            raise DatabaseError("插入班级记录失败", e)

    @staticmethod
    def update(clazz: Clazz) -> int:
        """更新班级记录"""
        try:
            sql = "UPDATE `t_class` SET `update_time` = :update_time"
            params = {
                "update_time": clazz.update_time,
                "id": clazz.id
            }
            if clazz.name is not None and clazz.name.strip() != "":
                sql += ", `name` = :name"
                params["name"] = clazz.name
            if clazz.teacher_name is not None and clazz.teacher_name.strip() != "":
                sql += ", `teacher_name` = :teacher_name"
                params["teacher_name"] = clazz.teacher_name
            sql += " WHERE `id` = :id"

            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            return result.rowcount
        except Exception as e:
            log.error("更新班级记录失败", e)
            raise DatabaseError("更新班级记录失败", e)

    @staticmethod
    def delete(id: int) -> int:
        """删除班级记录"""
        try:
            sql = "DELETE FROM `t_class` WHERE `id` = :id"
            session = DBUtil.get_session()
            result = session.execute(text(sql), {"id": id})
            return result.rowcount
        except Exception as e:
            log.error("删除班级记录失败", e)
            raise DatabaseError("删除班级记录失败", e)

    @staticmethod
    def select_by_id(id: int) -> Clazz:
        """根据ID进行查询"""
        try:
            sql = ("SELECT `id`, `name`, `teacher_name`, `create_time`, `update_time` "
                   "FROM `t_class` WHERE `id` = :id")
            session = DBUtil.get_session()
            result = session.execute(text(sql), {"id": id})
            result = result.mappings().fetchone()
            return Clazz.from_dict(result)
        except Exception as e:
            log.error("查询班级记录失败", e)
            raise DatabaseError("查询班级记录失败", e)

    @staticmethod
    def select_by_name(name: str) -> Clazz:
        """根据名称进行查询"""
        try:
            sql = ("SELECT `id`, `name`, `teacher_name`, `create_time`, `update_time` "
                   "FROM `t_class` WHERE `name` = :name")
            session = DBUtil.get_session()
            result = session.execute(text(sql), {"name": name})
            result = result.mappings().first()
            return Clazz.from_dict(result)
        except Exception as e:
            log.error("查询班级记录失败", e)
            raise DatabaseError("查询班级记录失败", e)

    @staticmethod
    def select_count() -> int:
        """获取所有班级记录数"""
        try:
            sql = "SELECT COUNT(*) AS `count` FROM `t_class`"
            session = DBUtil.get_session()
            result = session.execute(text(sql))
            return result.scalar()
        except Exception as e:
            log.error("查询班级记录失败", e)
            raise DatabaseError("查询班级记录失败", e)

    @staticmethod
    def select_page(order_by: str, sort: str, start: int, num: int) -> list[Clazz]:
        """分页查询"""
        sql = (f"SELECT `id`, `name`, `teacher_name`, `create_time`, `update_time` "
               f"FROM `t_class` ORDER BY {order_by} {sort} LIMIT :start, :num")
        params = {
            "start": start,
            "num": num
        }
        session = DBUtil.get_session()
        result = session.execute(text(sql), params)
        result = result.mappings().all()
        return [Clazz.from_dict(row) for row in result]