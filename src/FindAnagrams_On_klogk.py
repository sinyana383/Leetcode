from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        dic = {}
        p_s = (sorted(p))

        ls = len(s)
        lp = len(p)

        for i in range(0, ls):
            if ls - i < lp:
                break
            temp = s[i:i+lp]
            temp = sorted(temp)
            if temp == p_s:
                res.append(i)
        return res



sol = Solution()
s = "abab"
p = "ab"
print(sol.findAnagrams(s,p))