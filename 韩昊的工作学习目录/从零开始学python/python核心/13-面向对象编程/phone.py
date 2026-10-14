"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import time
class Phone:
    def __init__(self, brand, model, os_version, color, screen_size, storage, battery_capacity, power_percent=100):
        """
        初始化手机信息
        """
        self.brand = brand
        self.model = model
        self.os_version = os_version
        self.color = color
        self.screen_size = screen_size
        self.storage = storage
        self.battery_capacity = battery_capacity
        self.power_percent = max(0, min(100, power_percent)) # 限制在0-100之间
        self.is_on = False # 默认关机状态

    def power_on(self):
        """开机"""
        if not self.is_on:
            self.is_on = True
            print("手机已开机")
        else:
            print("手机已经是开机状态")

    def power_off(self):
        """关机"""
        if self.is_on:
            self.is_on = False
            print("手机已关机")
        else:
            print("手机已经是关机状态")

    def charge(self):
        """充电，提升电量至 100，模拟充电过程"""
        print(f"开始充电，当前电量 {self.power_percent}%...")
        while self.power_percent < 100:
            self.power_percent += 10
            if self.power_percent > 100:
                self.power_percent = 100
            print(f"充电中... 当前电量 {self.power_percent}%")
            time.sleep(0.5) # 模拟充电等待时间
        print("充电完成，电量已达 100%")

    def make_call(self, phoneNumber):
        """拨打电话"""
        if self.is_on:
            print(f"正在拨打 {phoneNumber}")
        else:
            print("手机处于关机状态，无法拨打电话")

    def receive_call(self, phoneNumber):
        """接听电话"""
        if self.is_on:
            print(f"正在接听 {phoneNumber} 的来电")
        else:
            print("手机处于关机状态，无法接听电话")

    def send_message(self, phoneNumber, content):
        """发送短信"""
        if self.is_on:
            print(f"已向 {phoneNumber} 发送短信，内容：{content}")
        else:
            print("手机处于关机状态，无法发送短信")

