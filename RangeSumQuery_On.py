from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        ln = len(nums)
        self.prefix_sums= [0] * ln
        self.prefix_sums[0] = nums[0]
        for i in range(1, ln):
            self.prefix_sums[i] += self.nums[i] + self.prefix_sums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        if left >= 1:
            return self.prefix_sums[right] - self.prefix_sums[left - 1]
        return self.prefix_sums[right]


# sol = Solution()
# print(sol.runningSum(nums))
nums = [-2, 0, 3, -5, 2, -1]

obj = NumArray(nums)

print(obj.sumRange(0, 2))  # Expected: 1
print(obj.sumRange(2, 5))  # Expected: -1
print(obj.sumRange(0, 5))  # Expected: -3