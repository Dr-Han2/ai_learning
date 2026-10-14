"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 导入包
from fastapi import FastAPI, Path, Query, Form, Body

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

# 路径传参
@app.get("/users/{id}")
def get_user_by_id (
        id: int = Path(..., ge=1, title="用户ID标题", description="用户ID")
):
    """返回所有用户信息"""
    # 遍历users列表，找到对应的用户信息
    for user in users:
        if user["id"] == id:
            return user
    # 没有找到
    return {"message": "用户不存在"}


# QueryString 传参
# /users/select/name?name=小白&age=20
# 传入多个参数，根据用户名和年龄查找用户信息
@app.get("/users/select/name/age")
def get_user_by_name_and_age(
        name: str = Query(..., title="用户名标题", description="用户名"),
        age: int = Query(..., ge=0, le=999, title="年龄标题", description="年龄必须要0-999之间")
):
    """根据用户名和年龄查询用户信息"""
    # 遍历users列表，找到对应的用户信息
    for user in users:
        if user["name"] == name and user["age"] == age:
            return user
    # 没有找到
    return {"message": "用户不存在"}

# 新增用户
@app.post("/users/")
def create_user(
        name: str = Form(..., title="用户名标题", description="用户名"),
        age: int = Form(..., ge=0, le=999, title="年龄标题", description="年龄必须要0-999之间")
):
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
@app.put("/update_users")
def update_user(
        id: int = Body(..., ge=1, title="用户ID标题", description="用户ID"),
        name: str = Body(..., title="用户名标题", description="用户名"),
        age: int = Body(..., ge=0, le=999, title="年龄标题", description="年龄必须要0-999之间")
):
    """修改用户"""
    # 参数校验
    if id <= 0 or name == "" or age <= 0:
        return {"message": "参数错误"}

    # 遍历users列表，找到对应的用户信息
    for user in users:
        if user["id"] == id:
            user["name"] = name
            user["age"] = age
            return {"message": "用户修改成功", "user": user}
    # 没有找到
    return {"message": "用户不存在"}
