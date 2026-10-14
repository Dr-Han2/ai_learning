"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
class CellPhone:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def call(self):
        print("打电话")

    def send_message(self):
        print("发消息")

    def take_phone(self):
        print("拍照")
