"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/9 10:19
@Version : 1.0
"""
from utils.db_util import DBUtil
from dao.user_dao import UserDao
from model.user import User
from core.exceptions import ValidationError, BusinessException
from core import logger

log = logger.get_logger()


class UserService:
    """登录用户的业务处理类"""

    @staticmethod
    def check_login(username: str, password: str) -> User:
        """校验用户登录"""
        if username is None or username.strip() == "":
            log.warning("用户名不能为空.")
            raise ValidationError("用户名不能为空.")

        if password is None or password.strip() == "":
            log.warning("密码不能为空.")
            raise ValidationError("密码不能为空.")

        with DBUtil.session_readonly() as session:
            result = UserDao.check_login(username, password)

        if result is None:
            log.info(f"{username} 登录失败")
            raise BusinessException("登录失败")
        log.info(f"{username} 登录成功")
        return result