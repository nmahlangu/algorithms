"""
1) RR
dp[i][j] = dp[i][j-1] + dp[i-1][j]
dp[i][j] = max unique paths at grid[i - 1][j - 1]

2) Base cases
dp[0][1] = 1
dp[1][0] = 1
"""

import unittest


class Solution:
    def unique_paths_bottom_up(self, m: int, n: int) -> int:
        if not m or not n:
            return 0

        dp: list[list[int]] = [[0] * (n) for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1]

    def unique_paths_top_down(self, m: int, n: int) -> int:
        memo: dict[tuple[int, int]] = {}
        return self.unique_paths_top_down_helper(m, n, memo)

    def unique_paths_top_down_helper(
        self, m: int, n: int, memo: dict[tuple[int, int]]
    ) -> int:
        if m == 1:
            return 1
        elif n == 1:
            return 1

        if (m, n) in memo:
            return memo[(m, n)]

        memo[(m, n)] = self.unique_paths_top_down_helper(
            m - 1, n, memo
        ) + self.unique_paths_top_down_helper(m, n - 1, memo)
        return memo[(m, n)]


class TestBottomUp(unittest.TestCase):
    def test_example1(self) -> None:
        actual = Solution().unique_paths_bottom_up(2, 3)
        self.assertEqual(3, actual)

    def test_example2(self) -> None:
        actual = Solution().unique_paths_bottom_up(3, 7)
        self.assertEqual(28, actual)


class TestTopDown(unittest.TestCase):
    def test_example1(self) -> None:
        actual = Solution().unique_paths_top_down(2, 3)
        self.assertEqual(3, actual)

    def test_example2(self) -> None:
        actual = Solution().unique_paths_top_down(3, 7)
        self.assertEqual(28, actual)


if __name__ == "__main__":
    unittest.main()
