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


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.DFS_check(p,q)



solution = Solution()

# Different structure
#
#    p       q
#    1       1
#   /         \
#  2           2

p = TreeNode(1)
p.left = TreeNode(2)

q = TreeNode(1)
q.right = TreeNode(2)

print(solution.isSameTree(p, q))  # Expected: False


# Same structure, different values
#
#    p       q
#    1       1
#   / \     / \
#  2   3   2   4

p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(4))

print(solution.isSameTree(p, q))  # Expected: False


# Both empty
p = None
q = None

print(solution.isSameTree(p, q))  # Expected: True