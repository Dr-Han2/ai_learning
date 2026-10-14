"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id : int = None
    username : str = None
    real_name : str = None
    create_name : str = None
    create_date : datetime = None
    update_date : datetime = None

    #定义一个从字典到对象的转换方法
    @staticmethod
    def from_dict(dic):
        """从字典到对象"""
        if dic is None:
            return None
        # 转换
        return User(**dic)
