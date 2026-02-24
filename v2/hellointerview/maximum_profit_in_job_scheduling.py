from typing import *
import unittest
from bisect import bisect_right

"""
DESCRIPTION (inspired by Leetcode.com)
Given three arrays, starts, ends, and profits, each representing the start time, 
end time, and profit of jobs respectively, your task is to schedule the jobs to 
maximize total profit. You can only work on one job at a time, and once a job has 
been started, you must finish it before starting another. The goal is to find the 
maximum profit that can be earned by scheduling jobs such that they do not overlap.

Input:

starts = [1, 3, 6, 10]
ends = [4, 5, 10, 12]
profits = [20, 20, 100, 70]
The optimal solution would schedule the jobs as follows:

Start the first job at time 1 and complete it by 4 for a profit of 20. 
Start the next job at time 6 and complete it by 10 for a profit of 100. 
Start the last job at time 10 and complete it by 12 for a profit of 70.

The total profit is 20 + 100 + 70 = 190
"""

"""
1) Recurrence relation
MP for a schedule ending with job i is max MP for index j + profit[i], for all j where j < i and start[i] >= end[j]

2) Base cases:
dp[i] = profit[i]
"""

"""
0) Pre-computation
Sort by end time

1) Recurrence relation
MP for the first i jobs is max( MP for first i - 1 jobs, MP for number of jobs that finish 
before job i starts + profit[i] )

2) Base cases:
dp[0] = 0

"""


class Solution:
    # O(n ^ 2)
    def job_scheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ):
        if not profit:
            return 0

        dp: list[int] = profit[:]

        for i in range(1, len(profit)):
            for j in range(i):
                if startTime[i] >= endTime[j]:
                    dp[i] = max(dp[i], dp[j] + profit[i])

        return max(dp)

    # O(n log n)
    def job_scheduling_2(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ):
        if not profit:
            return 0

        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [0] * (len(jobs) + 1)

        for i in range(1, len(jobs) + 1):
            start, _, profit_ = jobs[i - 1]
            num_jobs: int = bisect_right([job[1] for job in jobs], start)

            skip: int = dp[i - 1]
            take: int = dp[num_jobs] + profit_
            dp[i] = max(skip, take)

        return dp[-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example(self):
        starts = [1, 3, 6, 10]
        ends = [4, 5, 10, 12]
        profits = [20, 20, 100, 70]
        self.assertEqual(self.s.job_scheduling(starts, ends, profits), 190)


class TestSolution2(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example(self):
        starts = [1, 3, 6, 10]
        ends = [4, 5, 10, 12]
        profits = [20, 20, 100, 70]
        self.assertEqual(self.s.job_scheduling_2(starts, ends, profits), 190)


if __name__ == "__main__":
    unittest.main()
