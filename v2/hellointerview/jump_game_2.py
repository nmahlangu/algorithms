from typing import *

class Solution:
    def jump(self, nums: List[int]):
        if not nums:
            return 0

        current_end: int = 0
        farthest: int = 0
        leaps: int = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if current_end == i:
                leaps += 1
                current_end = farthest

        return leaps




