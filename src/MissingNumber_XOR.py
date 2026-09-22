class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans ^= n
        for n in range(0, len(nums) + 1):
            ans ^= n
        return ans