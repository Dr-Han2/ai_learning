"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/9 10:19
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
        try:
            sql = ("INSERT INTO `t_student` (`stu_num`, `name`, `gender`, `age`, `class_id`, `phone`, `create_time`, `update_time`) "
                   " VALUES (:stu_num, :name, :gender, :age, :class_id, :phone, :create_time, :update_time)")
            params = {
                "stu_num": student.stu_num,
                "name": student.name,
                "gender": student.gender,
                "age": student.age,
                "class_id": student.class_id,
                "phone": student.phone,
                "create_time": student.create_time,
                "update_time": student.update_time
            }
            session = DBUtil.get_session()
            result = session.execute(text(sql), params)
            student.id = result.lastrowid
            return result.rowcount
        except Exception as e:
            log.error("插入学生记录失败", e)
            raise DatabaseError("插入学生记录失败", e)

    @staticmethod
    def update(student: Student) -> int:
        """更新学生记录"""
        try:
            sql = "UPDATE `t_student` SET `update_time` = :update_time"
            params = {
                "update_time": student.update_time,
                "id": student.id
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
            return result.rowcount
        except Exception as e:
            log.error("更新学生记录失败", e)
            raise DatabaseError("更新学生记录失败", e)

    @staticmethod
    def delete(id: int) -> int:
        """删除学生记录"""
        try:
            sql = "DELETE FROM `t_student` WHERE `id` = :id"
            session = DBUtil.get_session()
            result = session.execute(text(sql), {"id": id})
            return result.rowcount
        except Exception as e:
            log.error("删除学生记录失败", e)
            raise DatabaseError("删除学生记录失败", e)

    @staticmethod
    def select_by_id(id: int) -> Student:
        """根据ID进行查询"""
        try:
            sql = ("SELECT `id`, `stu_num`, `name`, `gender`, `age`, `class_id`, `phone`, `create_time`, `update_time` "
                   "FROM `t_student` WHERE `id` = :id")
            session = DBUtil.get_session()
            result = session.execute(text(sql), {"id": id})
            result = result.mappings().fetchone()
            return Student.from_dict(result)
        except Exception as e:
            log.error("查询学生记录失败", e)
            raise DatabaseError("查询学生记录失败", e)

    @staticmethod
    def select_by_name(name: str) -> list[Student]:
        """根据姓名进行查询"""
        try:
            sql = ("SELECT `id`, `stu_num`, `name`, `gender`, `age`, `class_id`, `phone`, `create_time`, `update_time` "
                   "FROM `t_student` WHERE `name` = :name")
            session = DBUtil.get_session()
            result = session.execute(text(sql), {"name": name})
            result = result.mappings().all()
            return [Student.from_dict(row) for row in result]
        except Exception as e:
            log.error("查询学生记录失败", e)
            raise DatabaseError("查询学生记录失败", e)

    @staticmethod
    def select_by_stu_num(stu_num: str) -> Student:
        """根据学号进行查询"""
        try:
            sql = ("SELECT `id`, `stu_num`, `name`, `gender`, `age`, `class_id`, `phone`, `create_time`, `update_time` "
                   "FROM `t_student` WHERE `stu_num` = :stu_num")
            session = DBUtil.get_session()
            result = session.execute(text(sql), {"stu_num": stu_num})
            result = result.mappings().fetchone()
            return Student.from_dict(result)
        except Exception as e:
            log.error("查询学生记录失败", e)
            raise DatabaseError("查询学生记录失败", e)

    @staticmethod
    def select_by_class_id(class_id: int) -> list[Student]:
        """根据班级ID进行查询"""
        try:
            sql = ("SELECT `id`, `stu_num`, `name`, `gender`, `age`, `class_id`, `phone`, `create_time`, `update_time` "
                   "FROM `t_student` WHERE `class_id` = :class_id ORDER BY `id` ASC")
            session = DBUtil.get_session()
            result = session.execute(text(sql), {"class_id": class_id})
            result = result.mappings().all()
            return [Student.from_dict(row) for row in result]
        except Exception as e:
            log.error("查询班级学生失败", e)
            raise DatabaseError("查询班级学生失败", e)

    @staticmethod
    def select_count() -> int:
        """获取所有学生记录数"""
        try:
            sql = "SELECT COUNT(*) AS `count` FROM `t_student`"
            session = DBUtil.get_session()
            result = session.execute(text(sql))
            return result.scalar()
        except Exception as e:
            log.error("查询学生记录数失败", e)
            raise DatabaseError("查询学生记录数失败", e)

    @staticmethod
    def select_page(order_by: str, sort: str, start: int, num: int) -> list[Student]:
        """分页查询"""
        sql = (f"SELECT `id`, `stu_num`, `name`, `gender`, `age`, `class_id`, `phone`, `create_time`, `update_time` "
               f"FROM `t_student` ORDER BY {order_by} {sort} LIMIT :start, :num")
        params = {
            "start": start,
            "num": num
        }
        session = DBUtil.get_session()
        result = session.execute(text(sql), params)
        result = result.mappings().all()
        return [Student.from_dict(row) for row in result]