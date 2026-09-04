from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        for i in range(1, ln):
            nums[i] += nums[i-1]
        return nums



sol = Solution()
nums = [1,1,1,1,1]
print(sol.runningSum(nums))