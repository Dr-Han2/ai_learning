"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from classCellPhoneandMothd import CellPhone

if __name__ == "__main__":
    #创建两个对象 苹果 华为
    Phone1 = CellPhone("华为","冰晶蓝")
    Phone2 = CellPhone("苹果","玫瑰金")
    #访问属性
    print(Phone1.__dict__)
    print(Phone2.__dict__)
    #调用方法
    Phone1.send_message()
    Phone1.take_phone()
