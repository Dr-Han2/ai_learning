"""
@Author   : 韩昊
@Company  : 天津电子信息职业技术学院
:@Date    :   2026/9/1
@Desc     :    17:23
@Version  : 1.0
"""
#完成图片复制
# 1. 读取图片
with open("./DC151D747E570778F622C80EB6F8B79A.png",mode="rb") as file:
    source_pic = file.read()
    print(f"图片大小是：{len(source_pic)}")
    #查看前50个字节
    print(source_pic[:50])

#2.  复制图片
with open("./DC151D747E570778F622C80EB6F8B79A.png",mode="wb") as file:
    #写入目标文件
    file.write(source_pic)

print("图片复制完成")
