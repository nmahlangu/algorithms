import unittest


class Solution:
    def longestSubstringWithoutRepeat(self, s):
        state: dict[str, int] = {}
        start: int = 0
        max_length: int = 0

        for end in range(len(s)):
            if s[end] in state:
                start = max(start, state[s[end]] + 1)

            state[s[end]] = end
            max_length = max(max_length, end - start + 1)

        return max_length


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().longestSubstringWithoutRepeat("substring")
        self.assertEqual(8, actual)


if __name__ == "__main__":
    unittest.main()
