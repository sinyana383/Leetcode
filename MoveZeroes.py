from typing import List


def moveZeroes(nums: List[int]) -> None:
    if len(nums) <= 1:
        return

    sz = -1
    fz = -1
    for i in range (0, len(nums)):
        if nums[i] == 0:
            if sz < 0:
                sz = i
            elif fz < 0:
                fz = i
        elif sz >= 0:
            nums[sz] = nums[i]
            nums[i] = 0
            sz += 1
            fz = i

    print(nums)



nums = [0,1,0,3,12]

print(moveZeroes(nums))