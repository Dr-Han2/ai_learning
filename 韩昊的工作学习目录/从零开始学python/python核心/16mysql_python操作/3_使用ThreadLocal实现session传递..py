"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import threading

class DBUtil:
    """
    数据库工具类
    """
    # 只演示流程，不做真实实现
    def __init__(self):
        # 创建线程本地变量
        self._thread_local = threading.local()


    def get_session(self):
        """
        获取session对象
        :return:
        """
        # 判断本地线程有没有一个名字为session的属性
        if not hasattr(self._thread_local, "session"):
            # 创建session对象
            session = "SessionLocal()"
            print(f"创建session {session}")
            # 动态为_thread_local添加一个session属性
            self._thread_local.session = session
        # 返回session对象
        # getattr(self._thread_local, "session")
        print(f"返回session {self._thread_local.session}")
        return self._thread_local.session

    def remove_session(self):
        """
        移除session对象
        :return:
        """
        # 判断本地线程有没有一个名字为session的属性
        if hasattr(self._thread_local, "session"):
            # 移除session对象
            session = self._thread_local.session
            print(f"删除session {session}")
            # 删除对象中的属性
            delattr(self._thread_local, "session")
