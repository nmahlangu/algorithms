"""
1) recurrence relation
- # of 1's in the binary repr of i = # of 1's in binary repr of i // 2 + if the last bit is a one
dp[i] = dp[i // 2] + i % 2

2) bases cases
- dp[0] = 0
- dp[1] = 1
-

"""


class Solution:
    def count_bits(self, n: int):
        dp: list[int] = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i // 2] + (i % 2)

        return dp
