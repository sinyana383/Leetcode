from collections import deque
from typing import List, Optional, Deque
from pprint import pprint

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def DFS_check(self, p: Optional[TreeNode], q: Optional[TreeNode])-> bool:
        if (p is None) != (q is None):
            return False
        if p is None and q is None:
            return True
        if p.val != q.val:
            return False

        if not self.DFS_check(p.left, q.left):
            return False
        if not self.DFS_check(p.right, q.right):
            return False

        return True

    def invertTreeDFS(self, root: Optional[TreeNode]):
        if root is None:
            return

        temp: TreeNode = root.left
        root.left = root.right
        root.right = temp

        self.invertTreeDFS(root.left)
        self.invertTreeDFS(root.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None or root.left is None and root.right is None:
            return True
        if (root.left is None) != (root.right is None):
            return False

        self.invertTreeDFS(root.right)
        return self.DFS_check(root.left, root.right)



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
# Test 1: symmetric
#
#              1
#            /   \
#           2     2
#          / \   / \
#         3   4 4   3

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)

root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)

root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)

print(Solution().isSymmetric(root1))  # True


# Test 2: same values, but NOT symmetric
#
#              1
#            /   \
#           2     2
#            \     \
#             3     3

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)

root2.left.right = TreeNode(3)
root2.right.right = TreeNode(3)

print(Solution().isSymmetric(root2))  # False


# Test 3: different values
#
#              1
#            /   \
#           2     2
#          /       \
#         3         4

root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(2)

root3.left.left = TreeNode(3)
root3.right.right = TreeNode(4)

print(Solution().isSymmetric(root3))  # False


# Test 4: one child only
#
#              1
#             /
#            2

root4 = TreeNode(1)
root4.left = TreeNode(2)

print(Solution().isSymmetric(root4))  # False


# Test 5: single node
#
#              1

root5 = TreeNode(1)

print(Solution().isSymmetric(root5))  # True


# Test 6: empty tree

root6 = None

print(Solution().isSymmetric(root6))  # True


# Test 7: deeper symmetric tree
#
#                  1
#              /       \
#             2         2
#            / \       / \
#           3   4     4   3
#          /     \   /     \
#         5       6 6       5

root7 = TreeNode(1)

root7.left = TreeNode(2)
root7.right = TreeNode(2)

root7.left.left = TreeNode(3)
root7.left.right = TreeNode(4)

root7.right.left = TreeNode(4)
root7.right.right = TreeNode(3)

root7.left.left.left = TreeNode(5)
root7.left.right.right = TreeNode(6)

root7.right.left.left = TreeNode(6)
root7.right.right.right = TreeNode(5)

print(Solution().isSymmetric(root7))  # True


# Test 8: almost symmetric, one missing node
#
#                  1
#              /       \
#             2         2
#            / \       / \
#           3   4     4   3
#          /
#         5
#
# Missing mirrored 5 on the right side

root8 = TreeNode(1)

root8.left = TreeNode(2)
root8.right = TreeNode(2)

root8.left.left = TreeNode(3)
root8.left.right = TreeNode(4)

root8.right.left = TreeNode(4)
root8.right.right = TreeNode(3)

root8.left.left.left = TreeNode(5)

print(Solution().isSymmetric(root8))  # False