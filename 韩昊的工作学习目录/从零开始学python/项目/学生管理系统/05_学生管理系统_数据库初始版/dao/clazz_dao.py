"""
@Author  : hanhao
@Company : 未来元启
@Date    : 2026/10/9 10:19
@Desc    :
@Version : 1.0
"""
from model.clazz import Clazz
from utils.db_util import DBUtil
from sqlalchemy import text

from core.exceptions import DatabaseError
from core import logger

# 获取日志
log = logger.get_logger()


class ClazzDao:
    """班级数据库操作类"""

    # 公用查询列
    _COLUMNS = "`id`, `name`, `teacher_name`, `create_time`, `update_time`"

    @staticmethod
    def insert(clazz: Clazz) -> int:
        """写入班级记录"""
        session = None
        try:
            sql = ("INSERT INTO `t_class`(`name`, `teacher_name`, `create_time`, `update_time`) "
                   "VALUES (:name, :teacher_name, :create_time, :update_time)")
            params = {
                "name": clazz.name,
                "teacher_name": clazz.teacher_name,
                "create_time": clazz.create_time,
                "update_time": clazz.update_time,
            }
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            session.commit()                          # ← 关键：提交事务
            clazz.id = result.lastrowid               # ← 取自增主键
            return result.rowcount
        except Exception as e:
            if session:
                session.rollback()                    # ← 失败回滚
            log.exception("插入班级记录失败")           # ← 自动带堆栈
            raise DatabaseError(e) from e             # ← 保留原因链
        finally:
            if session:
                session.close()

    @staticmethod
    def update(clazz: Clazz) -> int:
        """更新班级记录"""
        session = None
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
            session.commit()                          # ← 提交
            return result.rowcount
        except Exception as e:
            if session:
                session.rollback()
            log.exception("更新班级记录失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def delete(id: int) -> int:
        """删除班级记录"""
        session = None
        try:
            sql = "DELETE FROM `t_class` WHERE `id` = :id"
            params = {"id": id}
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            session.commit()                          # ← 提交
            return result.rowcount
        except Exception as e:
            if session:
                session.rollback()
            log.exception("删除班级记录失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def select_by_id(id: int) -> Clazz:
        """根据ID进行查询"""
        session = None
        try:
            sql = (f"SELECT {ClazzDao._COLUMNS} "
                   f"FROM `t_class` WHERE `id` = :id")
            params = {"id": id}
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            row = result.mappings().fetchone()
            # Clazz.from_dict 内部已处理 None，直接返回即可
            return Clazz.from_dict(row)
        except Exception as e:
            log.exception("查询班级记录失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def select_by_name(name: str) -> Clazz:
        """根据名称进行查询"""
        session = None
        try:
            sql = (f"SELECT {ClazzDao._COLUMNS} "
                   f"FROM `t_class` WHERE `name` = :name")
            params = {"name": name}
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            row = result.mappings().first()
            # Clazz.from_dict 内部已处理 None，直接返回即可
            return Clazz.from_dict(row)
        except Exception as e:
            log.exception("查询班级记录失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def select_all() -> list[Clazz]:
        """查询全部班级"""
        session = None
        try:
            sql = (f"SELECT {ClazzDao._COLUMNS} "
                   f"FROM `t_class` ORDER BY `id`")
            session = DBUtil.get_session()
            rows = session.execute(text(sql)).mappings().fetchall()
            return [Clazz.from_dict(r) for r in rows]
        except Exception as e:
            log.exception("查询全部班级失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()