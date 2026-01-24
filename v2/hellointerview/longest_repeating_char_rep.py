import unittest


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start: int = 0
        max_length: int = 0
        max_freq: int = 0
        seen: dict[str, int] = {}

        for end in range(len(s)):
            seen[s[end]] = seen.get(s[end], 0) + 1
            max_freq = max(max_freq, seen[s[end]])

            if k + max_freq < end - start + 1:
                seen[s[start]] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().characterReplacement("BBABCCDD", 2)
        self.assertEqual(5, actual)


if __name__ == "__main__":
    unittest.main()
