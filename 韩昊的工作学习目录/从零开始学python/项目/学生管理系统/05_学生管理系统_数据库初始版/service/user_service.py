"""
@Author  : hanhao
@Company : 未来元启
@Date    : 2026/10/9 10:19
@Desc    : 
@Version : 1.0
"""
from dao.user_dao import UserDao
from model.user import User
from core import logger

# 日志对象
log = logger.get_logger()


class UserService:
    """登录用户的业务处理类"""

    @staticmethod
    def check_login(username: str, password: str) -> User:
        """校验用户登录"""
        # 参数校验
        if username is None or username == "":
            log.warning("登录失败：用户名为空")
            return None
        if password is None or password == "":
            log.warning("登录失败：密码为空")
            return None

        # 调用DAO进行登录校验
        result = UserDao.check_login(username, password)

        # 判断结果
        if result:
            log.info("登录成功: %s", result)
            return result
        else:
            log.warning("登录失败：用户名或密码错误 username=%s", username)
            return None


if __name__ == '__main__':
    result = UserService.check_login("admin", "123456")
    print("登录结果:", result)