"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 导入包
from fastapi import FastAPI

app = FastAPI(
    title="路径定义-post",
    description="This is an example of a FastAPI application.",
    version="0.1.0"
)

users = [
        {"id": 1, "name": "小白", "age": 20},
        {"id": 2, "name": "小红", "age": 19},
        {"id": 3, "name": "小明", "age": 21}
    ]

# POST传参，模拟新增用户
@app.post("/users/create")
def create_user(name: str, age: int):
    """新增用户"""
    # 构造用户信息
    user = {
        "id": len(users) + 1,
        "name": name,
        "age": age
    }
    # 打印用户信息
    print(user)
    # 添加用户信息到列表
    users.append(user)
    print(users)
    # 返回结果
    return {"message" : True}