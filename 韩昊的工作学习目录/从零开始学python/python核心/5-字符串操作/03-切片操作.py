"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    :
@Version : 1.0
"""

#定义一个字符串
text = "hello, python!"

#获取字符串的长度
print(f"字符串text的长度为{len(text)}")

#获取字符串中索引从2到5的元素
print(f"字符串text索引从2到5的元素是:{text[2:6]}")
#前5个元素
print(f"字符串前5个元素是:{text[:5]}")

#end
print(f"{text[7:]}") #从7到结束元素

print(text[:])
#步长为2
print(text[::2])

#反向切片(step=-1)
print(text[::-1])
#后5个元素
print(text[-5:])
#步长为2反转字符串
print(text[::-2])