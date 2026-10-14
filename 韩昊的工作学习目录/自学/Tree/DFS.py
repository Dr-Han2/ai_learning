"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def print_root(self):
        print(self.val, end=' ')


def tree_to_string(root):
    """将树转换成括号表示字符串，用于显示原树结构"""
    if not root:
        return 'None'
    if not root.left and not root.right:
        return str(root.val)
    return f"{root.val}({tree_to_string(root.left)}, {tree_to_string(root.right)})"


def DFS(root):
    """深度优先搜索（前序遍历，迭代实现）"""
    if not root:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        # 先压右，再压左，保证出栈顺序是 根 -> 左 -> 右
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


if __name__ == '__main__':
    root = TreeNode('A')
    root.left = TreeNode('B')
    root.right = TreeNode('C')
    root.left.left = TreeNode('D')
    root.right.left = TreeNode('E')
    root.right.right = TreeNode('F')
    root.right.left.left = TreeNode('G')
    root.right.left.right = TreeNode('H')

    print("原树结构：")
    print(tree_to_string(root))

    print("\nDFS 前序遍历结果：")
    print(DFS(root))