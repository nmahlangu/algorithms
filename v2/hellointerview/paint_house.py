from typing import *

"""
1) Recurrence relation
Min cost to paint the first i houses, where house i is a given color A = cost of painting house
i that color + min (same thing for prev house but you paint color B, same thing for prev house but
you paint color C)

2) Base cases
dp[0][X] = cost of painting house 0 color X
"""

class Solution:
    def min_cost(self, costs: List[List[int]]):
        if not costs:
            return 0

        prev_red: int = costs[0][0]
        prev_blue: int = costs[0][1]
        prev_green: int = costs[0][2]

        for i in range(1, len(costs)):
            curr_red: int = costs[i][0] + min(prev_blue, prev_green)
            curr_blue: int = costs[i][1] + min(prev_red, prev_green)
            curr_green: int = costs[i][2] + min(prev_red, prev_blue)

            prev_red = curr_red
            prev_blue = curr_blue
            prev_green = curr_green

        return min(prev_red, prev_blue, prev_green)