from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        c = 0
        st = 0
        dic = {}

        for f in range(0,len(s)):
            if dic.get(s[f]) is None or dic[s[f]] <= 0:
                dic[s[f]] = 1
                c += 1
                res = max(res, c)
            else:
                while s[st] != s[f]:
                    dic[s[st]] = 0
                    c -= 1
                    st += 1
                st += 1
        res = max(res, c)
        return res



sol = Solution()
s = "aabaab!bb"
print(sol.lengthOfLongestSubstring(s))