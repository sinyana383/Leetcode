from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        cur_len = m
        ptr2 = 0
        for i in range(0, len(nums1)):
            if ptr2 >= n:
                break
            if i >= cur_len:
                nums1[i] = nums2[ptr2]
                ptr2 += 1
                cur_len += 1
            elif nums1[i] >= nums2[ptr2]:
                for j in range (cur_len - 1, i - 1, -1):
                    nums1[j + 1] = nums1[j]
                nums1[i] = nums2[ptr2]
                ptr2 += 1
                cur_len += 1

sol = Solution()
nums1 = [2,0]
m = 1
nums2 = [1]
n = 1
sol.merge(nums1, m, nums2, n)
print(nums1)