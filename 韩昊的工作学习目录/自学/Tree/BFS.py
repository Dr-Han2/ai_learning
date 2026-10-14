"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def print_root(self):
        """打印当前节点的值"""
        print(self.val, end=' ')


def tree_to_string(root):
    """将二叉树转成括号表示字符串，用于显示原树结构"""
    if not root:
        return 'None'
    if not root.left and not root.right:
        return str(root.val)
    return f"{root.val}({tree_to_string(root.left)}, {tree_to_string(root.right)})"


def BFS(root):
    """广度优先搜索（层序遍历，迭代实现）"""
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


if __name__ == '__main__':
    # 构建示例树
    root = TreeNode('A')
    root.left = TreeNode('B')
    root.right = TreeNode('C')
    root.left.left = TreeNode('D')
    root.right.left = TreeNode('E')
    root.right.right = TreeNode('F')
    root.right.left.left = TreeNode('G')
    root.right.left.right = TreeNode('H')

    # 1. 先输出原树结构
    print("原树结构：")
    print(tree_to_string(root))

    # 2. 再输出 BFS 层序遍历结果
    print("\nBFS 层序遍历结果：")
    print(BFS(root))