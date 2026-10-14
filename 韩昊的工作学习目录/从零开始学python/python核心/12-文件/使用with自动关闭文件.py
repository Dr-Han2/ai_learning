with open("./node.txt","r",encoding="utf-8") as file:
    print(file.read())
print("文件操作完成")
print("文件是否关闭，", file.closed)