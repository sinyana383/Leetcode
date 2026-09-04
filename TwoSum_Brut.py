from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    i,j = 0,0
    for i in range (0, len(nums)-1):
        for j in range (i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

nums = [3,2,4]
target = 6
print(twoSum(nums, target))