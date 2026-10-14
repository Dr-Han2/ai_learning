"""
@Author  : hanhao
@Company : 未来元启
@Date    : 2026/10/9 10:27
@Desc    : 
@Version : 1.0
"""
import threading

# 导入包
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
# 导入环境变量工具
from utils.env_util import EnvUtil
from contextlib import contextmanager
# 装饰器工具，保留原函数名、文档注释
from functools import wraps


class DBUtil:
    """
    数据库全局工具类
    核心能力：单例引擎+SQLAlchemy连接池、天然防SQL注入、自动归还连接、统一执行CRUD
    规范：所有DAO层只能调用此类，禁止自己写pymysql连接
    """
    # 定义私有数据库引擎，全局唯一，禁止外部访问
    __engine = None
    # session工厂
    __SessionLocal = None
    # 线程锁，保证单例
    __lock = threading.Lock()

    # 初始化数据库引擎
    @classmethod
    def _init_engine(cls):
        # 外层判断，避免重复申请锁
        if cls.__engine is None:
            # 加锁，同一时间只能有一个线程创建引擎
            with cls.__lock:
                # 内层判断，避免重复创建对象，保证单例
                if cls.__engine is None:
                    # 拼接mysql连接url，统一从环境变量读取配置
                    connect_url = (
                        f"mysql+pymysql://{EnvUtil.DB_USER}:{EnvUtil.DB_PASSWORD}"
                        f"@{EnvUtil.DB_HOST}:{EnvUtil.DB_PORT}/{EnvUtil.DB_DATABASE}"
                        f"?charset={EnvUtil.DB_CHARSET}"
                    )
                    # 创建引擎，配置连接池核心参数
                    cls.__engine = create_engine(
                        url=connect_url,
                        pool_size=5,          # 常驻空闲连接数量
                        max_overflow=10,      # 峰值额外最大临时连接
                        pool_timeout=30,      # 获取连接超时30秒，防止卡死
                        pool_recycle=3600,    # 1小时回收连接，规避mysql断开空闲连接
                        pool_pre_ping=True,   # 使用连接前自动ping校验存活，杜绝断连报错
                        echo=False,           # 生产关闭sql打印，开发改为True调试
                        echo_pool=False,      # 关闭连接池日志，减少输出
                    )
                    # 创建Session对象
                    cls.__SessionLocal = sessionmaker(
                        bind=cls.__engine,
                        autoflush=False,
                        autocommit=False
                    )

    # 获取session对象
    @classmethod
    def get_session(cls) -> Session:
        """
        获取 session 对象
        说明：每次调用都返回一个全新的 session，调用方负责 close()
             底层连接由 SQLAlchemy 连接池管理，开销极小，避免 thread_local 缓存已关闭 session 的问题
        """
        # 初始化数据库引擎
        cls._init_engine()
        # 返回全新的session
        return cls.__SessionLocal()

    # 用户DML操作的上下文管理器，处理事务
    @classmethod
    @contextmanager
    def session_dml(cls):
        """用户DML操作的上下文管理器，处理事务"""
        # 获取session
        session = cls.get_session()
        try:
            # 返回session 用于with中的as 定义的变量
            yield session
            # 提交事务
            session.commit()
        except Exception as e:
            # 回滚事务
            session.rollback()
            # 继续抛出异常
            raise e
        finally:
            # 关闭session，归还连接池
            session.close()

    # 只用于查询的上下文管理器，不需要处理事务
    @classmethod
    @contextmanager
    def session_readonly(cls):
        """只用于查询的上下文管理器，不需要处理事务"""
        # 获取session
        session = cls.get_session()
        try:
            # 返回session 用于with中的as 定义的变量
            yield session
        finally:
            # 关闭session，归还连接池
            session.close()


# 定义在类外面
# 全局事务装饰器（对外暴露工具，Service仅导入此装饰器）
# 增删修必须使用事务，加入事务的DAO方法，自动管理事务
# 如果没有加 @transactional，需要手动创建session
def transactional(func):
    """
    事务自动管理装饰器, （推荐在Service层使用）
    核心能力：自动创建session、自动commit、异常自动rollback、最终自动close
    注意1：所有数据库操作共用同一个session，保证原子事务
    注意2：若DAO内部已自行commit/rollback/close，则不要叠加使用本装饰器，避免重复提交
    """
    @wraps(func)  # 保留原函数名、文档注释
    def wrapper(*args, **kwargs):
        # 1. 装饰器内部自动生成session，service不用关心数据库创建逻辑
        session: Session = DBUtil.get_session()
        try:
            # 2. 执行业务逻辑
            result = func(*args, **kwargs)
            # 3. 无异常自动提交事务，数据持久入库
            session.commit()
            return result
        except Exception as e:
            # 4. 任意异常自动回滚，本次所有数据库操作全部失效
            session.rollback()
            # 抛出原异常，上层可捕获处理业务报错
            raise e
        finally:
            # 5. 无论成功失败，强制关闭session，连接归还连接池
            session.close()
    return wrapper