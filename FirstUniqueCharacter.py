import math
from itertools import product
from sys import prefix
from typing import List


class Solution:
    def firstUniqChar(self, s: str) -> int:
        ls = len(s)

        mappik = {}
        for i in range(0, ls):
            if mappik.get(s[i], -1) == -1:
                mappik[s[i]] = i
            else:
                mappik[s[i]] = -2

        for c in s:
            if mappik.get(c, -1) >= 0:
                return mappik[c]

        return -1


sol = Solution()
nums = "aadadaad"
print(sol.firstUniqChar(nums))