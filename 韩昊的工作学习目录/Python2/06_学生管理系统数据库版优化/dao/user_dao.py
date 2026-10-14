"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/9 10:19
@Version : 1.0
"""
from utils.db_util import DBUtil
from model.user import User
from sqlalchemy import text
from core.exceptions import DatabaseError
from core import logger

log = logger.get_logger()


class UserDao:
    """系统用户数据访问对象"""

    @staticmethod
    def select_by_username(username: str) -> User:
        """根据用户名查询用户（登录时使用，密码比对在 Service 层）"""
        try:
            sql = ("select id, username, `password`, real_name, create_time, update_time "
                   "from t_user where username = :username")
            session = DBUtil.get_session()
            params = {
                "username": username
            }
            result = session.execute(text(sql), params)
            result = result.mappings().first()
            return User.from_dict(result)
        except Exception as e:
            log.error("数据库查询异常", e)
            raise DatabaseError("数据库查询异常", e)