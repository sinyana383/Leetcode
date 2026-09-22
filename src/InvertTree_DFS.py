from collections import deque
from typing import List, Optional, Deque
from pprint import pprint

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTreeDFS(self, root: Optional[TreeNode]):
        if root is None:
            return

        temp:TreeNode = root.left
        root.left = root.right
        root.right = temp

        self.invertTreeDFS(root.left)
        self.invertTreeDFS(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertTreeDFS(root)
        return root

def print_tree(root):
    if root is None:
        print("Empty tree")
        return

    def height(node):
        if node is None:
            return 0
        return 1 + max(height(node.left), height(node.right))

    h = height(root)
    width = 2 ** h

    level = [root]

    for depth in range(h):
        spacing = width // (2 ** depth)

        # Print nodes
        line = ""
        for node in level:
            value = str(node.val) if node else " "
            line += value.center(spacing)
        print(line)

        # Print branches
        if depth < h - 1:
            branches = ""
            for node in level:
                if node:
                    left = "/" if node.left else " "
                    right = "\\" if node.right else " "
                    branches += (left + " " + right).center(spacing)
                else:
                    branches += " ".center(spacing)
            print(branches)

        # Build next level
        next_level = []
        for node in level:
            if node:
                next_level.append(node.left)
                next_level.append(node.right)
            else:
                next_level.extend([None, None])

        level = next_level


root = TreeNode(4)

root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print_tree(root)
sol = Solution()
sol.invertTree(root)
print_tree(root)