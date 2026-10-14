"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 定义一个场景
file_name = "USER_docment.txt"
# 判断文件名是否以USER_开头
print(f"文件名是否以USER_开头 {file_name.startswith("USER_")}")
#判断文件名是否以.txt结尾
print(f"文件名是否以.txt结尾{file_name.endswith(".txt")}")

#加入判断条件中
if file_name.startswith("USER_") and file_name.endswith(".txt"):
    print("文件名符合要求,可以读取文件")
else:
    print("文件不符合要求")
#判断方法
print("hello".isalpha()) #全是字母？
print("123".isdigit())   #全是数字？
print("hello123".isalnum()) #字母或数字？
print(" ".isspace())        #空格？
print("hello".islower())    #小写？
print("HELLO".isupper())    #大写？
print("Hello World".istitle()) #每个单词首个字母大写？