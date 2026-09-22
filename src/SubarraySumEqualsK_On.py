from sys import prefix
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        ln = len(nums)
        prefix = 0
        dic = {}

        dic[0] = 1
        for n in nums:
            prefix += n
            target = prefix - k
            res += dic.get(target, 0)

            dic[prefix] = dic.get(prefix, 0) + 1
        return res



sol = Solution()
nums = [1,-1,0]
k = 0
print(sol.subarraySum(nums,k))