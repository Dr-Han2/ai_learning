"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/12 15:55
@Version : 1.0
"""
from fastapi import APIRouter, Body
from core.response import Response
from model.user import User
from service.user_service import UserService

router = APIRouter(prefix="/api/user", tags=["用户管理"])


@router.post("/login")
def login(
        username: str = Body(..., min_length=2, max_length=20, title="用户名", description="用户名必须2-20个字符"),
        password: str = Body(..., min_length=6, max_length=20, title="密码", description="密码必须6-20个字符")
):
    """用户登录"""
    user: User = UserService.check_login(username, password)
    return Response[User].success(user)