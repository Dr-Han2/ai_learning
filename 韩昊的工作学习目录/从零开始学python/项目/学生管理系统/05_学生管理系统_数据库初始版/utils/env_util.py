"""
@Author  : hanhao
@Company : 未来元启
@Date    : 2026/10/9 10:22
@Desc    : 
@Version : 1.0
"""
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

class EnvUtil:
    """环境变量工具类，全局数据库配置"""
    # 数据库主机
    DB_HOST = os.getenv("DB_HOST")
    # 数据库端口号
    DB_PORT = int(os.getenv("DB_PORT"))
    # 数据库用户名
    DB_USER = os.getenv("DB_USER")
    # 数据库密码
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    # 数据库名称
    DB_DATABASE = os.getenv("DB_DATABASE")
    # 数据库字符集
    DB_CHARSET = os.getenv("DB_CHARSET")

    # =========== 日志 ===========
    # 日志级别（默认 INFO）
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    # 日志目录（默认 logs）
    LOG_DIR = os.getenv("LOG_DIR", "logs")
    # 日志名（默认 student）
    LOG_NAME = os.getenv("LOG_NAME", "student")


# 测试
if __name__ == '__main__':
    print(EnvUtil.DB_HOST)
    print(EnvUtil.DB_PORT)
    print(EnvUtil.DB_USER)
    print(EnvUtil.DB_PASSWORD)
    print(EnvUtil.DB_DATABASE)
    print(EnvUtil.DB_CHARSET)