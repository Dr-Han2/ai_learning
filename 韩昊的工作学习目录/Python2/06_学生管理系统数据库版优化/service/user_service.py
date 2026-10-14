"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/9 10:19
@Version : 1.0
"""
import bcrypt

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

        # 1. 按用户名查询用户（密码比对在 Python 层做，不在 SQL 里做）
        with DBUtil.session_readonly() as session:
            user = UserDao.select_by_username(username)

        # ===== 临时调试，问题解决后删掉 =====
        print(f"[DEBUG] 查询到的用户对象 user = {user}")
        if user is not None:
            print(f"[DEBUG] 数据库中的密码哈希 password = {user.password}")
            print(f"[DEBUG] 数据库中的密码哈希长度 = {len(user.password)}")
            matched = bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8"))
            print(f"[DEBUG] bcrypt 比对结果 matched = {matched}")
        # ===== 临时调试结束 =====

        # 2. 用户不存在，统一返回「登录失败」，避免暴露账号是否存在
        if user is None:
            log.info(f"{username} 登录失败")
            raise BusinessException("登录失败")

        # 3. 用 bcrypt 在 Python 侧比对密码哈希
        if not bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
            log.info(f"{username} 登录失败")
            raise BusinessException("登录失败")

        log.info(f"{username} 登录成功")
        return user