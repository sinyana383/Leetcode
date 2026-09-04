from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ln = len(nums)
        prefix = [0] * ln
        postfix = [0] * ln

        prefix[0] = nums[0]
        postfix[ln - 1] = nums[ln -1]
        for i in range(1, ln):
            prefix[i] = nums[i] + prefix[i - 1]
            postfix[ln - 1 - i] = nums[ln - 1 - i] + postfix[ln - i]

        for i in range(0, ln):
            if postfix[i] == prefix[i]:
                return i

        return -1



sol = Solution()
nums = [2,1,-1]
print(sol.pivotIndex(nums))