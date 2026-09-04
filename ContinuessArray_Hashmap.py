from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ln = len(nums)
        mapik = {}

        max_count = 0
        presum = 0
        for i in range(0, ln):
            if nums[i] == 0:
                nums[i] = -1
            presum += nums[i]
            if mapik.get(presum) is None:
                mapik[presum] = i
            else:
                max_count = max(max_count, i - mapik[presum])
            if presum == 0:
                max_count = max(max_count, i + 1)

        goal = presum
        if goal == 0:
            return ln
        return max_count


sol = Solution()
nums = [0,1,1]
print(sol.findMaxLength(nums))