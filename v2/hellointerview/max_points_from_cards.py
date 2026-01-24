import unittest


class Solution:
    def maxScore(self, cards: list[int], k: int):
        state: int = 0
        start: int = k - 1
        max_score: int = 0

        for end in range(k - 1, -k - 1, -1):
            state += cards[end]

            if start - end + 1 == k:
                max_score = max(max_score, state)
                state -= cards[start]
                start -= 1

        return max_score


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().maxScore([1, 100, 10, 0, 4, 5, 6], 3)
        self.assertEqual(111, actual)


if __name__ == "__main__":
    unittest.main()
