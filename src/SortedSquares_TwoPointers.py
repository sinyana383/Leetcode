from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [0] * size
        res_i = size - 1
        l = 0
        r = size - 1
        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                res[res_i] = nums[l]**2
                res_i -= 1
                l += 1
            else:
                res[res_i] = nums[r]**2
                res_i -= 1
                r -= 1
        return res

sol = Solution()
print(sol.sortedSquares([-7,-3,2,3,11]))