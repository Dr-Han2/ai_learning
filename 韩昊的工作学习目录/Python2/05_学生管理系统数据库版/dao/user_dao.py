"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
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
    def check_login(username: str, password: str) -> User:
        try:
            sql=("select id, username, `password`,real_name`,`create_time`,update_time"
                 "from t_user where username= : username and password= : password")
            session=DBUtil.get_session()
            params={
                "username": username,
                "password": password
            }
            result=session.execute(text(sql),params)
            result=result.mappings().first()
            return User.from_dict()
        except Exception as e:
            log.error("数据库查询异常",e)
            raise DatabaseError("数据库查询异常",e)
