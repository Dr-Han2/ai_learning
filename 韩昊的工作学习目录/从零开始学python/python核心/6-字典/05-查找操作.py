"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 定义一个字典（商品信息）
goods_dict = {
    "id": "g001",
    "name": "手机",
    "price": 3999,
    "brand": "华为",
    "stock": 100
}
print(f"price 键是否存在字典中{"price" in goods_dict}")
print(f"price 键是否存在字典{"price" not in goods_dict}")
print(f"discount 键是否在字典{"discount" in goods_dict}")
print(f"discount 键是否存在字典{"discount" not in goods_dict}")

#通过KEY获取VALUE
goods_id = goods_dict["id"]
print(f"商品ID:{goods_id}")

#跟俊discount KEY判断商品是否打折
if "discount" in goods_dict:
    print(f"商品的折扣信息是:{goods_dict['discount']}")
else:
    print("商品没有折扣信息")



#添加一个key = discount
goods_dict["discount"] = 0.8
if goods_dict.get("discount") is None:
    print("商品没有折扣信息")
else:
    print(f"商品的折扣信息是;{goods_dict['discount']}")

#获取所有的KEY
print("=" * 30)
keys = goods_dict.keys()
print(f"所有的KEY:{keys}")

#获取所有的VALUE
values = goods_dict.values()
print(f"所有的VALUE:{values}")

#获取所有的KEY/VALUE
items = goods_dict.items()
print(f"所有的KEY/VALUE:{items}")
print(type(items))

