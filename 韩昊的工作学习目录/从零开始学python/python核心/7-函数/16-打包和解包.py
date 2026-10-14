"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#打包 给一个变量赋多个值 它会自动把这些数据打包成一个元组
t=1,2,3,4
print(t) #(1,2,3,4)
print(type(t)) #(type:tuple

#解包列表
list = [1,2,3,4]
a,b,c,d=list
print(a,b,c,d)
#解包字符串
str = "hello"
a,b,c,d,e=str
print(a,b,c,d,e)
#解包元组
tuple1 =(1,2,3,4)
e,f,g,h=tuple1
print(e,f,g,h)