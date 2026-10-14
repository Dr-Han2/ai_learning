"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#生成一个2*3的列表(矩阵)
#for 循环
matrix =[]
print(f"生成前的列表:{matrix}")

for i in range(2):
    row = []
    for j in range(3):
        row.append(j)
    matrix.append(row)
print(f"生成后的列表:{matrix}")

#推导式
matrix1 =[[j for j in range(3)]for i in range(2)]
print(matrix1)

#同理生成6*2
matrix2 =[[i,j] for i in range(2) for j in range(3)]
print(matrix2)
