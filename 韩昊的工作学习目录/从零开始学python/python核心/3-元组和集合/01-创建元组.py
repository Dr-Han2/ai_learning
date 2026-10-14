"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#使用小括号创建元组
tuple0 =(1,"hello", True, 3.14, "张三")
print(f"tuple0: {tuple0}")
print(f"tuple的类型是: {type(tuple0)}")
print("=" * 30 )

#定义一个空元组
tuple1=()
print(f"tuple1: {tuple1}")
print(f"tuple1的类型是: {type(tuple1)}")
print("=" * 30 )

#定义一个只含一个元素的元组
tuple2=("张三",)
print(f"tuple2: {tuple2}")
print(f"tuple2的类型是 : {type(tuple2)}")
print("=" * 30 )

#根据已有的序列来创建一个元组,本质上是类型转换
nums=[1,2,3,4,5]
tuple3 = tuple(nums)
print(f"tuple3: {tuple3}")
print(f"tuple3的类型是 : {type(tuple3)}")
print(f"nums的类型是 : {type(nums)}")
