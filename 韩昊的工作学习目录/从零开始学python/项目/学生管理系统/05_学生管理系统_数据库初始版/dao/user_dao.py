"""
@Author  : hanhao
@Company : 未来元启
@Date    : 2026/10/9 10:19
@Desc    : 
@Version : 1.0
"""
from utils.db_util import DBUtil
from model.user import User

from sqlalchemy import text

from core.exceptions import DatabaseError
from core import logger

# 获取日志
log = logger.get_logger()


class UserDao:
    """系统用户数据访问对象"""

    # 用户登录
    @staticmethod
    def check_login(username: str, password: str) -> User:
        """
        校验用户登录
        :param username: 用户名
        :param password: 密码
        :return: 用户对象
        """
        session = None
        try:
            # 定义SQL
            sql = ("SELECT id, username, `password`, real_name, create_time, update_time "
                   "FROM t_user WHERE username = :username AND password = :password")
            # 绑定参数
            params = {
                "username": username,
                "password": password
            }
            # 获取session
            session = DBUtil.get_session()
            # 执行SQL
            result = session.execute(text(sql), params)
            # 转换成一个字典
            row = result.mappings().first()
            # 返回结果
            return User.from_dict(row)
        except Exception as e:
            log.exception("登录校验失败")
            raise DatabaseError(e) from e
        finally:
            if session:
                session.close()


if __name__ == '__main__':
    result = UserDao.check_login("admin", "123456")
    print(result)
    print(f"result type = {type(result)}")  # User