"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
class Goods:
    """
    商品类
    """
    #构造方法
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
    #创建商品加入折扣 9折 要重新计算价格

    @classmethod
    def create_discount_goods(cls,name,price,stock,discount):
        #重新计算商品价格
        discount_price = price * discount
        #创建一个对象
        goods =cls(name,discount_price)
        return goods

#创建正常价格商品
goods1 =Goods("手机",3500,100)
print(goods1.price)
goods1.create_discount_goods("手机",3500,100,9)

