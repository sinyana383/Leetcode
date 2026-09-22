from collections import deque
from tkinter.constants import CENTER
from typing import List, Optional, Deque
from pprint import pprint
from enum import Enum

class Way(Enum):
    LEFT = 0
    RIGHT = 1
    CENTER = 2


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def DFS_check(self, root: Optional[TreeNode], left_bor:int, right_bor:int, par:int, way: Way)-> bool:
        if root is None:
            return True

        if way == Way.LEFT:
            right_bor = par
            if right_bor <= root.val or left_bor >= root.val:
                return False
        elif way == Way.RIGHT:
            left_bor = par
            if left_bor >= root.val or right_bor <= root.val:
                return False

        if self.DFS_check(root.left, left_bor, right_bor, root.val, Way.LEFT):
            return self.DFS_check(root.right, left_bor, right_bor, root.val, Way.RIGHT)
        return False



    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.DFS_check(root, float('-inf'), float('inf'), root.val, Way.CENTER)



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

solution = Solution()

# Test 1: Valid BST
#
#        2
#       / \
#      1   3

root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

print(solution.isValidBST(root1))  # True


# Test 2: Invalid BST
#
#        5
#       / \
#      1   4
#         / \
#        3   6
#
# 3 is in the right subtree of 5, but 3 < 5.

root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)

print(solution.isValidBST(root2))  # False


# Test 3: Important tricky case
#
#          10
#         /  \
#        5    15
#            /  \
#           6    20
#
# Locally:
# 6 < 15  <-- looks correct
#
# Globally:
# 6 is in the RIGHT subtree of 10,
# therefore it MUST be > 10.

root3 = TreeNode(10)
root3.left = TreeNode(5)
root3.right = TreeNode(15)
root3.right.left = TreeNode(6)
root3.right.right = TreeNode(20)

print(solution.isValidBST(root3))  # False


# Test 4: Same problem on the left side
#
#          10
#         /  \
#        5    15
#       / \
#      2   12
#
# 12 > 5 looks locally correct,
# but 12 is in the LEFT subtree of 10.
# Therefore 12 must be < 10.

root4 = TreeNode(10)
root4.left = TreeNode(5)
root4.right = TreeNode(15)
root4.left.left = TreeNode(2)
root4.left.right = TreeNode(12)

print(solution.isValidBST(root4))  # False


# Test 5: Larger valid BST
#
#              8
#           /     \
#          3       10
#         / \        \
#        1   6        14
#           / \       /
#          4   7     13

root5 = TreeNode(8)
root5.left = TreeNode(3)
root5.right = TreeNode(10)

root5.left.left = TreeNode(1)
root5.left.right = TreeNode(6)
root5.left.right.left = TreeNode(4)
root5.left.right.right = TreeNode(7)

root5.right.right = TreeNode(14)
root5.right.right.left = TreeNode(13)

print(solution.isValidBST(root5))  # True


# Test 6: Duplicate values are NOT allowed
#
#        2
#       / \
#      2   3

root6 = TreeNode(2)
root6.left = TreeNode(2)
root6.right = TreeNode(3)

print(solution.isValidBST(root6))  # False


# Test 7: Single node

root7 = TreeNode(1)

print(solution.isValidBST(root7))  # True