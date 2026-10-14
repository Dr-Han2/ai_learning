"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/9 10:16
@Version : 1.0
"""
import uvicorn
from fastapi import FastAPI
from core import logger
from core.exception_handler import ExceptionHandlerRegister

from controller import user_controller, clazz_controller, student_controller, course_controller, socre_controller

# 创建日志对对象
log = logger.get_logger()

# 创建FastAPI实例
app = FastAPI(
    title="学生管理系统",
    description="学生管理系统API服务",
    version="0.1.0"
)
logger.info("========== FastAPI服务开始启动===========")

# 注册全局异常处理器
ExceptionHandlerRegister.register(app)
log.info("全局异常处理器注册完成")

# ==========导入子路由==========
# 用户管理
app.include_router(user_controller.router)
logger.info(f"{user_controller.router.tags} 子路由启动成功, {user_controller.router.prefix}")

# 班级管理
app.include_router(clazz_controller.router)
logger.info(f"{clazz_controller.router.tags} 子路由启动成功, {clazz_controller.router.prefix}")

# 学生管理
app.include_router(student_controller.router)
logger.info(f"{student_controller.router.tags} 子路由启动成功, {student_controller.router.prefix}")

# 课程管理
app.include_router(course_controller.router)
logger.info(f"{course_controller.router.tags} 子路由启动成功, {course_controller.router.prefix}")

# 成绩管理
app.include_router(socre_controller.router)
logger.info(f"{socre_controller.router.tags} 子路由启动成功, {socre_controller.router.prefix}")

logger.info("========== FastAPI服务启动成功===========")


if __name__ == '__main__':
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)