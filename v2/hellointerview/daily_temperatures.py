import unittest
from typing import *


class Solution:
    def dailyTemperatures(self, temps: list[int]):
        result: list[int] = [0] * len(temps)
        stack: list[int] = []

        for i, temp in enumerate(temps):
            while stack and temp > temps[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return result


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().dailyTemperatures([65, 70, 68, 60, 55, 75, 80, 74])
        self.assertEqual([1, 4, 3, 2, 1, 1, 0, 0], actual)


if __name__ == "__main__":
    unittest.main()
