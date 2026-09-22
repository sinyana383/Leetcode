from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in range(0, len(strs)):
            temp = "".join(sorted(strs[i]))
            if dic.get(temp) is None:
                dic[temp] = []
            dic[temp].append(strs[i])

        res = [[] for _ in dic]
        a_i = 0
        for k in dic:
            res[a_i] = dic[k]
            a_i += 1
        return res




sol = Solution()
strs  = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))