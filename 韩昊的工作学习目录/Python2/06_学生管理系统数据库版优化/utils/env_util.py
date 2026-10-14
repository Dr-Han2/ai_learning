"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/9 10:22
@Version : 1.0
"""
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()


class EnvUtil:
    """环境变量工具类，全局数据库配置"""
    # 数据库主机
    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
    # 数据库端口号
    DB_PORT = int(os.getenv("DB_PORT", "3306"))
    # 数据库用户名
    DB_USER = os.getenv("DB_USER", "root")
    # 数据库密码
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    # 数据库名称
    DB_DATABASE = os.getenv("DB_DATABASE", "student_student_manage_db")
    # 数据库字符集
    DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

    # =========== 日志 ===========
    # 日志级别
    LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
    # 日志目录
    LOG_DIR = os.getenv("LOG_DIR", "logs")
    # 日志名
    LOG_NAME = os.getenv("LOG_NAME", "student")