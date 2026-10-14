"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/9 10:27
@Version : 1.0
"""
import threading

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from utils.env_util import EnvUtil
from contextlib import contextmanager
from functools import wraps


class DBUtil:
    """
    数据库全局工具类
    核心能力：单例引擎+SQLAlchemy连接池、天然防SQL注入、自动归还连接、统一执行CRUD
    """
    __engine = None
    __SessionLocal = None
    __thread_local = threading.local()
    __lock = threading.Lock()

    @classmethod
    def _init_engine(cls):
        if cls.__engine is None:
            with cls.__lock:
                if cls.__engine is None:
                    connect_url = f"mysql+pymysql://{EnvUtil.DB_USER}:{EnvUtil.DB_PASSWORD}@{EnvUtil.DB_HOST}:{EnvUtil.DB_PORT}/{EnvUtil.DB_DATABASE}?charset={EnvUtil.DB_CHARSET}"
                    cls.__engine = create_engine(
                        url=connect_url,
                        pool_size=5,
                        max_overflow=10,
                        pool_timeout=30,
                        pool_recycle=3600,
                        pool_pre_ping=True,
                        echo=False,
                        echo_pool=False
                    )
                    cls.__SessionLocal = sessionmaker(
                        bind=cls.__engine,
                        autoflush=False,
                        autocommit=False
                    )

    @classmethod
    def get_session(cls) -> Session:
        """获取session对象，并用thread local 存储"""
        cls._init_engine()
        if not hasattr(cls.__thread_local, "session"):
            session = cls.__SessionLocal()
            cls.__thread_local.session = session
        return cls.__thread_local.session

    @classmethod
    def remove_session(cls):
        """删除线程绑定的session对象"""
        if hasattr(cls.__thread_local, "session"):
            try:
                session = cls.__thread_local.session
                session.close()
            finally:
                delattr(cls.__thread_local, "session")

    @classmethod
    @contextmanager
    def session_dml(cls):
        """用户DML操作的上下文管理器，处理事务"""
        session = cls.get_session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            cls.remove_session()

    @classmethod
    @contextmanager
    def session_readonly(cls):
        """只用于查询的上下文管理器，不需要处理事务"""
        session = cls.get_session()
        try:
            yield session
        finally:
            cls.remove_session()


def transactional(func):
    """事务自动管理装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        session: Session = DBUtil.get_session()
        try:
            result = func(*args, **kwargs)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        finally:
            DBUtil.remove_session()
    return wrapper