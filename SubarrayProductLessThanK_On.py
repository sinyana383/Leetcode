import math
from itertools import product
from sys import prefix
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ln = len(nums)
        l = 0
        prod = 1
        res = 0

        r = 0
        prod *= nums[r]
        while r < ln:
            if prod < k:
                res += 1 + r - l
                r += 1
                if r >= ln:
                    break
                prod *= nums[r]
            else:
                prod //= nums[l]
                l += 1
                if l > r:
                    r = l
                    if r < ln:
                        prod *= nums[r]
                    else:
                        break

        return res



sol = Solution()
nums = [10,5,2,6]
k = 100
print(sol.numSubarrayProductLessThanK(nums,k))