"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#使用数组实现Heap
class MaxHeap:
    def __init__(self, arr=None):
        self.heap = []
        if arr:
            self.heap = list(arr)
            self.build_heap()

    # 索引计算
    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # 上浮：用于插入
    def _sift_up(self, i):
        while i > 0:
            p = self._parent(i)
            if self.heap[i] > self.heap[p]:
                self._swap(i, p)
                i = p
            else:
                break

    # 下沉：用于删除堆顶、建堆
    def _sift_down(self, i, size=None):
        if size is None:
            size = len(self.heap)

        while True:
            largest = i
            l = self._left(i)
            r = self._right(i)

            if l < size and self.heap[l] > self.heap[largest]:
                largest = l
            if r < size and self.heap[r] > self.heap[largest]:
                largest = r

            if largest == i:
                break

            self._swap(i, largest)
            i = largest

    # 插入元素
    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    # 删除并返回堆顶最大值
    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")

        max_val = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._sift_down(0)

        return max_val

    # 查看堆顶
    def peek(self):
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    # 建堆：O(n)
    def build_heap(self):
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(i)

    def __len__(self):
        return len(self.heap)

    def __bool__(self):
        return bool(self.heap)

    def __repr__(self):
        return f"MaxHeap({self.heap})"

h = MaxHeap()

for x in [3, 1, 6, 5, 2, 4]:
    h.push(x)

print(h)          # MaxHeap([6, 5, 4, 3, 1, 2])
print(h.peek())   # 6
   # 6
print(h)          # MaxHeap([5, 3, 4, 1, 2])