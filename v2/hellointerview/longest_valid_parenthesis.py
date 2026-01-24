import unittest
from typing import *


class Solution:
    def longest_valid_parentheses(self, s: str):
        stack: [int] = [-1]
        max_len: int = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len

class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().longest_valid_parentheses(")()())")
        self.assertEqual(4, actual)


if __name__ == "__main__":
    unittest.main()
