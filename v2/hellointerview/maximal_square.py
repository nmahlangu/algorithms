"""
1) Recurrence relation
Maximal square ending at g[rows - 1][cols - 1] = max of (ms up, ms, left, ms up left) + 1
dp[i][j] = max(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1

2) Base cases is 0 for all 3

"""

from typing import *


class Solution:
    def maximal_square(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        rows: int = len(matrix)
        cols: int = len(matrix[0])
        dp: list[list[int]] = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        max_side: int = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == 1:
                    top: int = dp[i - 1][j]
                    diag: int = dp[i - 1][j - 1]
                    left: int = dp[i][j - 1]
                    dp[i][j] = min(top, left, diag) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side
