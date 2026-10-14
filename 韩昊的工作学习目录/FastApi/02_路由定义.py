"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 1. 导入FastAPI包
from fastapi import FastAPI
# 日志包
import logging

# 2. 创建导入的FastAPI实例（对象）
app = FastAPI(
    title="第一个FastAPI接口",
    description="This is an example of a FastAPI application.",
    version="0.1.0"
)

# 定义一个根目录的路由
@app.get("/")
def hello():
    """这是一个测试接口"""
    return {"message": "这是我的第一个FastAPI接口"}

# 需要查询所有的用户信息
users = [
        {"id": 1, "name": "小白", "age": 20},
        {"id": 2, "name": "小红", "age": 19},
        {"id": 3, "name": "小明", "age": 21}
    ]

# 定义一个接口，返回所有用户的信息
@app.get("/users")
def get_users():
    """返回所有用户的信息"""
    logging.debug("调用了users接口...")
    print(000)
    return users

# 定义一个接口，根据ID查询用户信息
# /users/select_by_id?id=1
@app.get("/users/select_by_id")
def get_user_by_id(id: int):
    """根据ID查询用户信息"""
    logging.debug("调用了users/select_by_id接口...")
    print(111)
    # 遍历users列表，找到对应的用户信息
    for user in users:
        if user["id"] == id:
            return user
    # 没有找到
    return {"message": "用户不存在"}

# 路径传参，根据ID查找用户信息
# /users/1
@app.get("/users/{id}")
def get_user_by_id_path(id: int):
    """根据ID查询用户信息"""
    logging.debug("调用了users/{id}接口...")
    print(222)
    # 遍历users列表，找到对应的用户信息
    for user in users:
        if user["id"] == id:
            return user
    # 没有找到
    return {"message": "用户不存在"}

# 传入多个参数，根据用户名和年龄查找用户信息
@app.get("/users/{name}/{age}")
def get_user_by_name_and_age(name: str, age: int):
    """根据用户名和年龄查询用户信息"""
    logging.debug("调用了users/{name}/{age}接口...")
    print(123)
    # 遍历users列表，找到对应的用户信息
    for user in users:
        if user["name"] == name and user["age"] == age:
            return user
    # 没有找到
    return {"message": "用户不存在"}

# 通过query string的方式传参，根据用户名和年龄查找用户信息
@app.get("/users/select/name/age")
def get_user_by_name_and_age(name, age):
    """根据用户名和年龄查询用户信息"""
    logging.debug("调用了users/{name}/{age}接口...")
    print(456)
    # 遍历users列表，找到对应的用户信息
    for user in users:
        if user["name"] == name and user["age"] == int(age):
            return user
    # 没有找到
    return {"message": "用户不存在"}