from typing import *


class Solution:

    def moveZeroes(nums):
        nextNonZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nextNonZero], nums[i] = nums[i], nums[nextNonZero]
                nextNonZero += 1


s = Solution()
assert s.moveZeroes([1, 0, 4, 0, 3, 0, 1]) == [1, 4, 3, 1, 0, 0, 0]
