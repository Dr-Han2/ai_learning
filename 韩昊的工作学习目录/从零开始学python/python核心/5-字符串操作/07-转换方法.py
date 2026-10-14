"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
print("Hello World".upper())
print("Hello World".lower())

text = "   hello 1    "
print(text.strip())

#替换 replace
text1 = "There's a bad apple here"
#替换前
print(text1)
#替换bad —> good
print(text1.replace("bad", "good"))

# CSV格式：张三,18,男
csv_data = "张三,18,男"
print(f"CSV数据是 {csv_data}, type is {type(csv_data)}")
user_info = csv_data.split(",")
print(f"CSV数据转换成列表之后 {user_info}, type is {type(user_info)}")

# 字符串连接
print("*" * 30)
# 使用 _ 连接列表中的字符串元素. json(序列)
text2 = "_".join(user_info)
print(f"使用 _ 连接列表中的字符串元素 {text2}")

# 接收到用户的输入之后，去掉两边的空格
name = input("请输入姓名：")
print(f"输入的姓名是 {name}")
print(f"去空格后的姓名是 {name.strip()}")



