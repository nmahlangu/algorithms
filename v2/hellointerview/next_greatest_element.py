import unittest
from typing import *


class Solution:
    def nextGreaterElement(self, nums: list[int]):
        result: list[int] = [-1] * len(nums)
        mi_stack: list[int] = []

        for i, num in enumerate(nums):
            while mi_stack and num > nums[mi_stack[-1]]:
                result[mi_stack[-1]] = num
                mi_stack.pop()

            mi_stack.append(i)

        return result


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().nextGreaterElement([2, 1, 3, 2, 4, 3])
        self.assertEqual([3, 3, 4, 4, -1, -1], actual)


if __name__ == "__main__":
    unittest.main()
