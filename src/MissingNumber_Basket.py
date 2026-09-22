from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        basket = [0] * (len(nums) + 1)
        for n in nums:
            basket[n] += 1
        for i in range (0, len(basket)):
            if basket[i] < 1:
                return i
        return -1

sol = Solution()
print(sol.missingNumber([3,0,1]))