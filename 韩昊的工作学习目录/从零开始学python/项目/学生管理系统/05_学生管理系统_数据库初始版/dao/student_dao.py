"""
@Author  : hanhao
@Company : 未来元启
@Date    : 2026/10/9 10:19
@Desc    : 
@Version : 1.0
"""
from model.student import Student
from utils.db_util import DBUtil
from sqlalchemy import text

from core.exceptions import DatabaseError
from core import logger

log = logger.get_logger()


class StudentDao:
    """学生数据库操作类"""

    @staticmethod
    def insert(student: Student) -> int:
        """写入学生记录"""
        session = None
        try:
            sql = ("INSERT INTO `t_student`"
                   "(`stu_num`, `name`, `gender`, `age`, `class_id`, `phone`, "
                   " `create_time`, `update_time`) "
                   "VALUES (:stu_num, :name, :gender, :age, :class_id, :phone, "
                   "        :create_time, :update_time)")
            params = {
                "stu_num": student.stu_num,
                "name": student.name,
                "gender": student.gender,
                "age": student.age,
                "class_id": student.class_id,
                "phone": student.phone,
                "create_time": student.create_time,
                "update_time": student.update_time,
            }
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            session.commit()
            student.id = result.lastrowid           # 回填自增主键
            return result.rowcount
        except Exception as e:
            if session:
                session.rollback()
            log.exception("插入学生记录失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def update(student: Student) -> int:
        """更新学生记录（动态拼 SQL，只更新传入的字段）"""
        session = None
        try:
            sql = "UPDATE `t_student` SET `update_time` = :update_time"
            params = {
                "update_time": student.update_time,
                "id": student.id,
            }
            if student.stu_num is not None and student.stu_num.strip() != "":
                sql += ", `stu_num` = :stu_num"
                params["stu_num"] = student.stu_num
            if student.name is not None and student.name.strip() != "":
                sql += ", `name` = :name"
                params["name"] = student.name
            if student.gender is not None and student.gender.strip() != "":
                sql += ", `gender` = :gender"
                params["gender"] = student.gender
            if student.age is not None:
                sql += ", `age` = :age"
                params["age"] = student.age
            if student.class_id is not None:
                sql += ", `class_id` = :class_id"
                params["class_id"] = student.class_id
            if student.phone is not None and student.phone.strip() != "":
                sql += ", `phone` = :phone"
                params["phone"] = student.phone
            sql += " WHERE `id` = :id"

            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            session.commit()
            return result.rowcount
        except Exception as e:
            if session:
                session.rollback()
            log.exception("更新学生记录失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def delete(id: int) -> int:
        """按主键删除学生"""
        session = None
        try:
            sql = "DELETE FROM `t_student` WHERE `id` = :id"
            params = {"id": id}
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            session.commit()
            return result.rowcount
        except Exception as e:
            if session:
                session.rollback()
            log.exception("删除学生记录失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def select_by_id(id: int) -> Student:
        """按主键查询"""
        session = None
        try:
            sql = ("SELECT `id`, `stu_num`, `name`, `gender`, `age`, "
                   "       `class_id`, `phone`, `create_time`, `update_time` "
                   "FROM `t_student` WHERE `id` = :id")
            params = {"id": id}
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            row = result.mappings().fetchone()
            return Student.from_dict(row)
        except Exception as e:
            log.exception("查询学生记录失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def select_by_stu_num(stu_num: str) -> Student:
        """按学号查询（学号唯一）"""
        session = None
        try:
            sql = ("SELECT `id`, `stu_num`, `name`, `gender`, `age`, "
                   "       `class_id`, `phone`, `create_time`, `update_time` "
                   "FROM `t_student` WHERE `stu_num` = :stu_num")
            params = {"stu_num": stu_num}
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            row = result.mappings().first()
            return Student.from_dict(row)
        except Exception as e:
            log.exception("按学号查询学生失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def select_by_name(name: str) -> list[Student]:
        """按姓名模糊查询（可能有重名，返回列表）"""
        session = None
        try:
            sql = ("SELECT `id`, `stu_num`, `name`, `gender`, `age`, "
                   "       `class_id`, `phone`, `create_time`, `update_time` "
                   "FROM `t_student` WHERE `name` LIKE :name")
            params = {"name": f"%{name}%"}
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            rows = result.mappings().fetchall()
            return [Student.from_dict(r) for r in rows]
        except Exception as e:
            log.exception("按姓名查询学生失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def select_by_class_id(class_id: int) -> list[Student]:
        """查询某个班级下的所有学生"""
        session = None
        try:
            sql = ("SELECT `id`, `stu_num`, `name`, `gender`, `age`, "
                   "       `class_id`, `phone`, `create_time`, `update_time` "
                   "FROM `t_student` WHERE `class_id` = :class_id "
                   "ORDER BY `id`")
            params = {"class_id": class_id}
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            rows = result.mappings().fetchall()
            return [Student.from_dict(r) for r in rows]
        except Exception as e:
            log.exception("按班级查询学生失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()

    @staticmethod
    def select_all() -> list[Student]:
        """查询全部学生"""
        session = None
        try:
            sql = ("SELECT `id`, `stu_num`, `name`, `gender`, `age`, "
                   "       `class_id`, `phone`, `create_time`, `update_time` "
                   "FROM `t_student` ORDER BY `id`")
            session = DBUtil.get_session()
            result = session.execute(text(sql))
            rows = result.mappings().fetchall()
            return [Student.from_dict(r) for r in rows]
        except Exception as e:
            log.exception("查询全部学生失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()
