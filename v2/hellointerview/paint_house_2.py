from typing import *

class Solution:
    def min_cost_ii(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        rows: int = len(costs)
        cols: int = len(costs[0])
        prev: list[int] = costs[0][:]

        for i in range(1, rows):
            min1, min2, min1_idx = float('inf'), float('inf'), -1

            # get prev row lowest 2 costs
            for j in range(cols):
                if prev[j] < min1:
                    min2 = min1
                    min1 = prev[j]
                    min1_idx = j
                elif prev[j] < min2:
                    min2 = prev[j]

            # compute costs of painting current row
            curr: list[int] = [0] * cols
            for j in range(cols):
                if j == min1_idx:
                    curr[j] = costs[i][j] + min2
                else: 
                    curr[j] = costs[i][j] + min1

            # save row for computing next row
            prev = curr

        return min(prev)