from collections import deque
from typing import List, Optional, Deque
from pprint import pprint

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        deqP = deque()
        deqQ = deque()
        deqP.append(p)
        deqQ.append(q)

        while len(deqP) >= 1 and len(deqQ) >= 1:
            curP:TreeNode = deqP.popleft()
            curQ:TreeNode = deqQ.popleft()

            if curP is None and curQ is not None or curP is not None and curQ is None:
                return False
            if not(curP is None and curQ is None or curP.val == curQ.val):
                return False

            if curQ is not None:
                deqQ.append(curQ.left)
                deqQ.append(curQ.right)
            if curP is not None:
                deqP.append(curP.left)
                deqP.append(curP.right)

        return True




#           1
#         /   \
#        2     3
#       / \     \
#      4   5     6
#         /     /
#        7     8

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

root.left.right.left = TreeNode(7)
root.right.right.left = TreeNode(8)

sol = Solution()
sol.levelOrderBFS(root)