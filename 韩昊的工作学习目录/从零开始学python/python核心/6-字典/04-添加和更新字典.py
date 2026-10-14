"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#创建一个空字典
dict1={}
#直接添加
dict1["name"]="张三"
print(f"dict1={dict1}")
#哪个KEY存在,则更新
dict1["name"]="李四"
print(f"更新后的字典dict1={dict1}")

#添加其他KEY/VAULE
dict1["age"]=18
dict1["gender"]="man"
print(f"dict1={dict1}")

#通过updata()批量添加
dict1.update({
    "phone":"13355556666",
    "email":"xxxx@qq.com",
    "name": "王五"
})
print(f"dict1={dict1}")