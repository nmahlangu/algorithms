from typing import *
import unittest


class Solution:
    def trappingWater(self, heights):
        if not heights:
            return 0
        left, right = 0, len(heights) - 1
        leftMax, rightMax = heights[left], heights[right]
        count = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                if heights[left] >= leftMax:
                    leftMax = heights[left]
                else:
                    count += leftMax - heights[left]
            else:
                right -= 1
                if heights[right] >= rightMax:
                    rightMax = heights[right]
                else:
                    count += rightMax - heights[right]

        return count

    def trappingWaterMine(self, height: List[int]):
        lmax: List[int] = [0] * len(height)
        rmax: List[int] = [0] * len(height)
        result: int = 0

        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                rmax[i] = height[i]
                continue
            rmax[i] = max(height[i], rmax[i + 1])

        for i in range(len(height)):
            if i == 0:
                lmax[i] = height[i]
            else:
                lmax[i] = max(height[i], lmax[i - 1])

            result += max(0, min(lmax[i], rmax[i]) - height[i])

        return result


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().trappingWater([3, 4, 1, 2, 2, 5, 1, 0, 2])
        self.assertEqual(10, actual)


if __name__ == "__main__":
    unittest.main()
