from typing import *

class Solution:

    def sortColors(self, nums):
        left, right = 0, len(nums) - 1
        i = 0

        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1

        return nums

    def sortColorsMine(self, nums: List[int]):
        index: int = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1

        for i in range(index, len(nums)):
            if nums[i] == 1:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1 

        return nums

s = Solution()
assert s.sortColors([2,1,2,0,1,0,1,0,1]) == [0,0,0,1,1,1,1,2,2]