"""
@Author  : 韩昊
@Company : 天津电子信息职业技术学院
@Date    :   2026/9/1 16:16
@Desc    :
@Version : 1.0
"""
# 1. 打开文件， 指定 mode=w 编码=utf-8
with open("./node.txt",mode="w",encoding="utf-8") as file:
    # 写入字符串,写入的内容后面不加换行符 自动换行
    file.write("今天心情很好")
    file.write("我正在学python\n")
    file.write("hello\n")
    file.write(f"星期{6}")

print("写入成功")

# 查看写入内容
with open("./node.txt",mode="r",encoding="utf-8") as file:
    print(file.read())