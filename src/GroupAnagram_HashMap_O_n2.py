from typing import List


class Solution:
    def isAnagram(self, str1, str2) -> bool:
        if len(str1) != len(str2):
            return False
        if len(str1) == 0:
            return True

        d = {}
        for s in str1:
            if d.get(s) is None:
                d[s] = 1
            else:
                d[s] += 1
        for s in str2:
            if d.get(s) is None:
                return False
            d[s] -= 1
            if d[s] <= 0:
                d.pop(s)

        if len(d) <= 0:
            return True
        return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        a_i = 0
        while len(strs) > 0:
            i = 0
            temp = strs[0]
            res.append([])
            res[a_i].append(temp)
            strs.pop(i)
            while i < len(strs):
                if self.isAnagram(temp, strs[i]):
                    res[a_i].append(strs[i])
                    strs.pop(i)
                else:
                    i += 1
            res[a_i].sort()
            a_i += 1
        return res




sol = Solution()
strs  = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))