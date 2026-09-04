import math
from itertools import product
from sys import prefix
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ln = len(nums)
        odd_c = 0
        res = 0

        st_odd = -1
        fin_odd = ln

        l = 0
        r = 0
        while r < ln:
            if nums[r] % 2 == 1:
                odd_c += 1
                if st_odd == -1:
                    st_odd = r
                if odd_c == k:
                    fin_odd = r
                if odd_c > k:
                    res += (st_odd - l + 1) * (r - fin_odd)
                    st_odd += 1
                    l = st_odd
                    while nums[st_odd] % 2 != 1:
                        st_odd += 1
                    fin_odd = r
            r += 1
        res += (st_odd - l + 1) * (r - fin_odd)

        return res




sol = Solution()
nums = [2,4,6]
k = 1
print(sol.numberOfSubarrays(nums,k))