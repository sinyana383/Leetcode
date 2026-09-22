from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    d = {}
    for i in range (0, len(nums)):
        d[target - nums[i]] = i

    for i in range (0, len(nums)):
        if d.get(nums[i]) is not None and d[nums[i]] != i:
            return sorted([d[nums[i]], i])

nums = [3,2,4]
target = 6
print(twoSum(nums, target))