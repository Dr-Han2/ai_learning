"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#数组实现二叉树
#i的左字树 2*i + 1 i的右子树 2*i + 2
#i的父节点 (i-1) // 2

class ArrayBinaryTree:
    def __init__(self,arr):
        self.arr = arr

    def left(self,i):
        index = 2 * i + 1
        if index < len(self.arr):
            return self.arr[index]
        return None

    def right(self,i):
        index = 2 * i + 2
        if index < len(self.arr):
            return self.arr[index]
        return None

    def parent(self,i):
        if i == 0 :
            return None
        index = (i - 1) // 2
        return self.arr[index]

    def show(self):
        print(self.arr)

arr_tree = ArrayBinaryTree([1, 2, 3, 4, 5, 6])
arr_tree.show()
print(arr_tree.left(0))
print(arr_tree.right(1))
print(arr_tree.parent(5))