"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from sympy import false


class MyWith:
    def __init__(self):
        print("初始化上下问管理器")

    def __enter__(self):
        print("进入MyWith， 获取数据库链接和session")
        return self

    #离开with之后运行
    def __exit__(self, exc_type, exc_val, exc_tb):
        """

        :param exc_type: 异常类型
        :param exc_val: 异常值
        :param exc_tb: 异常的跟踪信息
        :return:
        """
        print("离开MyWith， 释放数据库链接和session")

        if exc_type:
            print("异常类型:", exc_type)
            print(" 异常值:",exc_val)
            print("异常跟踪:", exc_tb)
            print("事务回滚")
        else:
            print("事务提交")

        return False
if __name__ == '__main__':
    with MyWith() as my_with:
        print("=======使用with=======")
        #模拟异常
        raise Exception("模拟异常")

    print("======退出with=======")
