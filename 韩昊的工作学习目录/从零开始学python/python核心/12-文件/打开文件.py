"""
@Author  : 韩昊
@Company : 天津电子信息职业技术学院
@Date    :   2026/9/1 16:16
@Desc    :
@Version : 1.0
"""
#12-文件
# mode :打开文件的"方式",相当于"打开日记本的目的"(是只读，还是写内容),
# r 只读模式
# w 写入模式
# a 追加模式
# r+ 读写模式
#以只读的方式打开文件
file1 = open("./node.txt","r", encoding="utf-8")
# 查看file1的类型
print(f"file1的类型是:{type(file1)}")
print(f"file1 = {file1}")
#文件用完之后需要关闭
file1.close()
#读取文件内容
#1.read()方法:一次性读取文件全部内容
#2.readline()方法:逐行读取文件内容
#3.readlines()方法:读取所有行，返回列表