import unittest
from typing import *

class Solution:
    def largestRectangleArea(self, heights: list[int]):
        # stores indexes, present here means we are looking for a lower index to the right
        stack: list[int] = []
        i: int = 0
        max_area: int = 0

        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                right = i - 1
                left = stack[-1] if stack else -1
                area = heights[top] * (right - left)
                max_area = max(max_area, area)

        while stack:
            top = stack.pop()
            right = i - 1
            left = stack[-1] if stack else -1
            area = heights[top] * (right - left)
            max_area = max(max_area, area)

        return max_area

class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().largestRectangleArea([2,8,5,6,2,3])
        self.assertEqual(15, actual)


if __name__ == "__main__":
    unittest.main()