"""
if no more letters:
    if current string is a palindrome, store all in results as one

option 1
add letter to current string
    dfs the rest

option 2
skip letter, finish a, start b
if a is a palindrome:
    dfs the rest
"""

import unittest


class Solution:
    def is_palindrome(self, s: str) -> bool:
        if not s:
            return True

        left: int = 0
        right: int = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def partition(self, s: str) -> list[list[str]]:
        if not s:
            return []

        result: list[list[str]] = []
        self.dfs(s, 0, [], result)
        return result

    def dfs(self, s: str, start: int, path: list[str], result: list[list[str]]) -> None:
        if start == len(s):
            result.append(path[:])
            return

        for end in range(start, len(s)):
            sub_s: str = s[start : end + 1]
            if self.is_palindrome(sub_s):
                path.append(sub_s)
                self.dfs(s, end + 1, path, result)
                path.pop()


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().partition("noon")
        self.assertEqual([["n", "o", "o", "n"], ["n", "oo", "n"], ["noon"]], actual)


if __name__ == "__main__":
    unittest.main()
