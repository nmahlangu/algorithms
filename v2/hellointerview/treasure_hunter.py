"""
1) recurrence relation: dp(i) = max amount of treasure that can be collected from the first i houses 
dp(i) = max( dp(i-1), dp(i-2) + treasure[i - 1] )

2) base cases
dp(0) = 0
dp(1) = treasure[0]

3) recursive solution
4) add memoization
5) convert to bottom up
6) further optimizations
"""

import unittest


class Solution:
    # V1: Memoized top down DP
    def rob(self, treasure: list[int]) -> int:
        if not treasure:
            return 0

        memo: dict[int, int] = {}
        return self.rob_helper(treasure, len(treasure), memo)

    def rob_helper(self, treasure: list[int], house: int, memo: dict[int, int]) -> int:
        if house == 0:
            return 0
        elif house == 1:
            return treasure[0]

        if house in memo:
            return memo[house]

        memo[house] = max(
            self.rob_helper(treasure, house - 1, memo),
            self.rob_helper(treasure, house - 2, memo) + treasure[house - 1],
        )
        return memo[house]

    # V2: Memoized bottom up DP
    def rob2(self, treasure: list[int]) -> int:
        if not treasure:
            return 0

        dp: dict[int, int] = {0: 0, 1: treasure[0]}
        for i in range(2, len(treasure) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + treasure[i - 1])

        return dp[len(treasure)]

    # V3: Optimized bottom up DP
    def rob3(self, treasure: list[int]) -> int:
        if not treasure:
            return 0

        prev: int = 0
        curr: int = treasure[0]

        for i in range(2, len(treasure) + 1):
            take: int = prev + treasure[i - 1]
            skip: int = curr

            prev, curr = curr, max(take, skip)

        return curr


class TestSolution(unittest.TestCase):
    def test_example1(self) -> None:
        actual = Solution().rob([3, 1, 4, 1, 5])
        self.assertEqual(12, actual)

    def test_single_house(self) -> None:
        actual = Solution().rob([5])
        self.assertEqual(5, actual)

    def test_two_houses(self) -> None:
        actual = Solution().rob([1, 2])
        self.assertEqual(2, actual)

    def test_three_houses(self) -> None:
        actual = Solution().rob([2, 7, 9])
        self.assertEqual(11, actual)

    def test_four_houses(self) -> None:
        actual = Solution().rob([1, 2, 3, 1])
        self.assertEqual(4, actual)

    def test_all_same_values(self) -> None:
        actual = Solution().rob([5, 5, 5, 5, 5])
        self.assertEqual(15, actual)

    def test_empty(self) -> None:
        actual = Solution().rob([])
        self.assertEqual(0, actual)

    def test_descending(self) -> None:
        actual = Solution().rob([10, 5, 3, 1])
        self.assertEqual(13, actual)

    def test_alternating_high_low(self) -> None:
        actual = Solution().rob([100, 1, 100, 1, 100])
        self.assertEqual(300, actual)

    def test_all_zeros(self) -> None:
        actual = Solution().rob([0, 0, 0, 0])
        self.assertEqual(0, actual)


class TestSolution2(unittest.TestCase):
    def test_example1(self) -> None:
        actual = Solution().rob2([3, 1, 4, 1, 5])
        self.assertEqual(12, actual)

    def test_single_house(self) -> None:
        actual = Solution().rob2([5])
        self.assertEqual(5, actual)

    def test_two_houses(self) -> None:
        actual = Solution().rob2([1, 2])
        self.assertEqual(2, actual)

    def test_three_houses(self) -> None:
        actual = Solution().rob2([2, 7, 9])
        self.assertEqual(11, actual)

    def test_four_houses(self) -> None:
        actual = Solution().rob2([1, 2, 3, 1])
        self.assertEqual(4, actual)

    def test_all_same_values(self) -> None:
        actual = Solution().rob2([5, 5, 5, 5, 5])
        self.assertEqual(15, actual)

    def test_empty(self) -> None:
        actual = Solution().rob2([])
        self.assertEqual(0, actual)

    def test_descending(self) -> None:
        actual = Solution().rob2([10, 5, 3, 1])
        self.assertEqual(13, actual)

    def test_alternating_high_low(self) -> None:
        actual = Solution().rob2([100, 1, 100, 1, 100])
        self.assertEqual(300, actual)

    def test_all_zeros(self) -> None:
        actual = Solution().rob2([0, 0, 0, 0])
        self.assertEqual(0, actual)


class TestSolution3(unittest.TestCase):
    def test_example1(self) -> None:
        actual = Solution().rob3([3, 1, 4, 1, 5])
        self.assertEqual(12, actual)

    def test_single_house(self) -> None:
        actual = Solution().rob3([5])
        self.assertEqual(5, actual)

    def test_two_houses(self) -> None:
        actual = Solution().rob3([1, 2])
        self.assertEqual(2, actual)

    def test_three_houses(self) -> None:
        actual = Solution().rob3([2, 7, 9])
        self.assertEqual(11, actual)

    def test_four_houses(self) -> None:
        actual = Solution().rob3([1, 2, 3, 1])
        self.assertEqual(4, actual)

    def test_all_same_values(self) -> None:
        actual = Solution().rob3([5, 5, 5, 5, 5])
        self.assertEqual(15, actual)

    def test_empty(self) -> None:
        actual = Solution().rob3([])
        self.assertEqual(0, actual)

    def test_descending(self) -> None:
        actual = Solution().rob3([10, 5, 3, 1])
        self.assertEqual(13, actual)

    def test_alternating_high_low(self) -> None:
        actual = Solution().rob3([100, 1, 100, 1, 100])
        self.assertEqual(300, actual)

    def test_all_zeros(self) -> None:
        actual = Solution().rob3([0, 0, 0, 0])
        self.assertEqual(0, actual)


if __name__ == "__main__":
    unittest.main()
