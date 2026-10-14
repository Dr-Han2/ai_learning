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

# RestFul API 范式
# 用一个路径定义增删改查，用不同方法进行区分
@app.get("/users")
def get_users():
    """返回所有用户信息"""
    return users

# 新增用户
@app.post("/users/")
def create_user(name: str, age: int):
    """新增用户"""
    user = {
        "id": len(users) + 1,
        "name": name,
        "age": age
    }
    users.append(user)
    print(users)
    return {"message": "用户新增成功", "user": user}

# 修改用户
@app.put("/users/{id}/{name}/{age}")
def update_user(id: int, name: str, age: int):
    """修改用户"""
    # 遍历users列表，找到对应的用户信息
    for user in users:
        if user["id"] == id:
            user["name"] = name
            user["age"] = age
            return {"message": "用户修改成功", "user": user}
    # 没有找到
    return {"message": "用户不存在"}


@app.get("/users/{id}")
def get_user_by_id (id: int):
    """返回所有用户信息"""
    # 遍历users列表，找到对应的用户信息
    for user in users:
        if user["id"] == id:
            return user
    # 没有找到
    return {"message": "用户不存在"}

# 删除用户
@app.delete("/users/{id}")
def delete_user(id: int):
    """删除用户"""
    # 遍历users列表，找到对应的用户信息
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return {"message": "用户删除成功"}
    # 没有找到
    return {"message": "用户不存在"}
