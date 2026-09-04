from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if t is None:
            return False
        if s is None or len(s) <= 0:
            return True

        s_i = 0
        for w in t:
            if s_i >= len(s):
                return True
            if s[s_i] == w:
                s_i += 1
        if s_i == len(s):
            return True
        return False


sol = Solution()
t  = "ahbgdc"
s = "abc"
print(sol.isSubsequence(s,t))