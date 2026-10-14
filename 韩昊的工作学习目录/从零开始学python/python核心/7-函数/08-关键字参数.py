"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
def create_user(user_id,
                user_name,
                nick_name,
                age=18,
                gender="man",
                is_admin=False):
    print(f"用户ID：{user_id}, 用户名：{user_name}, 昵称：{nick_name}, 年龄：{age}, 性别：{gender}, 是否是管理员：{is_admin}")

create_user(user_id=2,
            age=18,
            gender="man",
            user_name="李四",
            nick_name="list",
            is_admin=True)