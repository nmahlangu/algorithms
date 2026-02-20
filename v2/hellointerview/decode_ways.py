"""
12 (2)
1 2
12

123 (3)
1 2 3
1 23
12 3

1234 (4)
1 2 3 4
12 3 4
1 23 4
1 2 34
12 34

1) recurrence relation
- # of ways to decode a str of len(i) = # of ways to decode a str of len(i - 1) (take case) + # of ways to decode a str of len (i - 2) (append case)

2) base cases
[0] = 1
[1] = 1
"""


class Solution:
    def num_decodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == "0":
            return 0

        dp: list[int] = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(s) + 1):
            # last digit
            digit = int(s[i - 1])
            if digit != 0:
                dp[i] += dp[i - 1]

            # last 2 digits
            digit = int(s[i - 2 : i])
            if 10 <= digit <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]
