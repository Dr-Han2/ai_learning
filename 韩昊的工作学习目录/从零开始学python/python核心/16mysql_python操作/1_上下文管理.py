"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from contextlib import contextmanager

@contextmanager
def get_session():
    """
    使用contextmanager实现上下文管理器
    进入和退出之间用yield进行分隔
    """
    print("获取session,开启事务")
    session = "模拟session对象"

    try:
        print("返回session对象,供with内部代码使用")
        yield session
        #没有异常提交事务
        print("提供事务")

    except Exception as e:
        #出现异常
        print(f"回滚事务,异常{e}")
    finally:
        #释放数据库连接,关闭seesion
        print("关闭session,释放数据库连接")

if __name__ == "__main__":
    with get_session() as session:
        print("=========with中使用session对象=========")
        print(session)
        raise Exception("模拟异常")

    print("=========with代码块执行完毕=========")