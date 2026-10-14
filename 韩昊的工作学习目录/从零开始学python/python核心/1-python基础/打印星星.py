#确定行数
num = int(input("请输入一个整数"))

for i in range(1,num+1):
    for _ in range(i):
        print("*",end="")
    print()