"""
@Author  : 韩昊
@Company : *********
@Date    :
@Desc    :
@Version : 1.0
"""
#range(起始值)
#生成一个从0开始到5结束的范围,只传一个参数,表示到哪里结束，默认从0开始
for i in range(5):
    print(i,end=" ") #end="\n"
print()
print("=" * 30)
#生成一个从2到7的序列
for i in range(2,8):
    print(i,end=" ")
print()
print("=" * 30)
#range(5)指从0到4 range(n) 从0到n-1
#range(起始值,结束值,步长)
#生成一个从0到9的奇数序列
for i in range(1,11,2):
    print(i,end=" ")
print()
print("=" * 30)
#生成一个从0到9的偶数序列
for i in range(0,10,2):
    print(i,end=" ")
print()
#步长可以为负
#10到0降序排列
for i in range(10,0,-1):
    print(i,end=" ")
