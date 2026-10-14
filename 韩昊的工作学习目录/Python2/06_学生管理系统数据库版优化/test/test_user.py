"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/10 15:34
@Version : 1.0
"""
from model.user import User
from service.user_service import UserService


def test_check_login():
    """测试用户登录"""
    user: User = UserService.check_login("admin", "123456")
    assert user is not None


def test_assert():
    assert 1 == 1