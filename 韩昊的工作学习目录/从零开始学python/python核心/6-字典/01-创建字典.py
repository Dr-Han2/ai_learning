"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#1创建字典
#使用大括号创建一个空字典
dict1 ={}
print(f"dict1的类型是{type(dict1)}")
print(f"dict1 ={dict1}")

#可以用类型对应的方式创建一个空字典 dict
dict2 = dict()
print(f"dict2的类型是{type(dict2)}")
print(f"dict2 ={dict2}")

dict3 = {"name": "小明",
         "age": 18,
         "score": 95,
         "gender": "男"
}
print(f"dict3={dict3}")

dict4 = dict(name="张三", age=18, score=100, gender="女" )
print(f"dict4={dict4}")
#元组
dict5 = dict([("name", " 李四"),("age", 18),("score", 95),("gender", "男")])
print(f"dict5={dict5}")

# 重复的KEY，后面的会覆盖前面的值
dict6 = {
    "stu_no" : "S101",
    "name" : "张三",
    "age" : 18,
    "gender" : "男",
    "name" : "李四"
}
print(f"dict6={dict6}")

#使用不可变的类型作为KEY
dict7={
    1:"张三",
    2:"李四"
}
print(f"dict7={dict7}")

# 使用元组做为KEY
dict8 = {
    (1, 2) : "张三",
    (3, 4) : "李四"
}
print(f"dict8 = {dict8}")

#使用列表做为KEY
#dict9 = {
 #   [1, 2] : "张三",
 #   [3, 4] : "李四"
#}
#print(f"dict9 = {dict9}")