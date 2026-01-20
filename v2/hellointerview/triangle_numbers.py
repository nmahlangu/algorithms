from typing import *

class Solution:
    def triangleNumber(self, heights: List[int]):
        heights.sort()
        
        count: int = 0
        for i in range(len(heights) - 1, 1, -1):
            left: int = 0
            right: int = i - 1

            while right > left:
                curr_sum: int = heights[left] + heights[right]
                if curr_sum > heights[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1  

        return count