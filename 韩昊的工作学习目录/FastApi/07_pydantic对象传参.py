"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from fastapi import FastAPI
from pydantic import BaseModel,Field

app=FastAPI(
    title ="路径定义-post",
    description ="This is an example of FastAPI application.",
    version="0.1.0",
)
# 需求：接收用户信息，在系统中创建一个新用户
# 1. 定义Pydantic校验模型（校验新增用户的请求体)
class UserDTO(BaseModel):
    """用户信息"""
    name: str = Field(...,min_length=1,max_length=10,description="用户名,必填,2-10到字符")
    age: int = Field(...,ge=18, le=100, description="年龄,必填,18-100岁")
    phone: str | None = Field(None, pattern=r"^1[3-9]\d{9}$", description="手机号，可选，11位有效号码")
    gender: str | None = Field(None, enum=["男", "女"], description="性别，可选，男/女")

@app.post("/user/create")
def create_user(user: UserDTO):
    """
    创建用户接口
    :param user: 用户信息UserDTO
    :return:
    """
    print(user.name, user.age, user.phone, user.gender)

    return {"message": "用户创建成功", "user": user}


