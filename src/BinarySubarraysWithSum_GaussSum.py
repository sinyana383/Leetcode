import math
from itertools import product
from sys import prefix
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ln = len(nums)
        sum = 0
        res = 0

        st_goal = -1
        fin_goal = ln

        l = 0
        r = 0
        if goal == 0:
            while r < ln:
                if nums[r] == 1:
                    zero_c = r - l
                    res += (1 + zero_c) * zero_c // 2
                    r += 1
                    l = r
                    continue
                r += 1
            zero_c = r - l
            res += (1 + zero_c) * zero_c // 2
            return res

        else:
            while r < ln:
                sum += nums[r]
                if nums[r] == 1:
                    if sum == 1:
                        st_goal = r
                    if sum == goal:
                        fin_goal = r
                    if sum > goal:
                        res += (st_goal - l + 1) * (r - fin_goal)
                        st_goal += 1
                        l = st_goal
                        while nums[st_goal] != 1:
                            st_goal += 1
                        fin_goal = r
                r += 1

            res += (st_goal - l + 1) * (r - fin_goal)

        return res



sol = Solution()
nums = [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0]
goal = 0
print(sol.numSubarraysWithSum(nums,goal))