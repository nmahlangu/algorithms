from typing import *
import unittest

"""
1) recurrence relation
The length of LIS ending at index i is 1 greater than the max LIS ending at some index prev,
such that arr[prev] < arr[i] where prev < i. If no prev exists, LIS is 1
"""


class Solution:
    def longest_increasing_subsequence_td(self, nums: List[int]) -> int:
        max_lis: int = 1
        memo: list[int] = [-1] * len(nums)

        for i in range(1, len(nums)):
            max_lis = max(max_lis, self.lis_td_helper(nums, i, memo))

        return max_lis

    def lis_td_helper(self, nums: list[int], i: int, memo: list[int]) -> int:
        if i == 0:
            return 1

        if memo[i] != -1:
            return memo[i]

        lis: int = 1
        for j in range(i):
            if nums[j] < nums[i]:
                lis = max(lis, self.lis_td_helper(nums, j, memo) + 1)

        memo[i] = lis
        return lis

    def longest_increasing_subsequence_bu(self, nums: list[int]) -> int:
        if not nums:
            return 0

        dp: list[int] = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_classic_example(self):
        self.assertEqual(
            self.s.longest_increasing_subsequence_td([10, 9, 2, 5, 3, 7, 101, 18]), 4
        )

    def test_already_increasing(self):
        self.assertEqual(self.s.longest_increasing_subsequence_td([1, 2, 3, 4, 5]), 5)

    def test_strictly_decreasing(self):
        self.assertEqual(self.s.longest_increasing_subsequence_td([5, 4, 3, 2, 1]), 1)

    def test_single_element(self):
        self.assertEqual(self.s.longest_increasing_subsequence_td([42]), 1)

    def test_two_elements_increasing(self):
        self.assertEqual(self.s.longest_increasing_subsequence_td([1, 2]), 2)

    def test_two_elements_decreasing(self):
        self.assertEqual(self.s.longest_increasing_subsequence_td([2, 1]), 1)

    def test_all_equal(self):
        self.assertEqual(self.s.longest_increasing_subsequence_td([7, 7, 7, 7]), 1)

    def test_lis_not_at_end(self):
        self.assertEqual(self.s.longest_increasing_subsequence_td([2, 3, 7, 101, 1]), 4)

    def test_negative_numbers(self):
        self.assertEqual(
            self.s.longest_increasing_subsequence_td([-5, -3, -1, 0, 2]), 5
        )

    def test_mixed_positive_negative(self):
        self.assertEqual(
            self.s.longest_increasing_subsequence_td([3, -2, 0, 3, 6, 1]), 4
        )


class TestSolutionBU(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_classic_example(self):
        self.assertEqual(
            self.s.longest_increasing_subsequence_bu([10, 9, 2, 5, 3, 7, 101, 18]), 4
        )

    def test_already_increasing(self):
        self.assertEqual(self.s.longest_increasing_subsequence_bu([1, 2, 3, 4, 5]), 5)

    def test_strictly_decreasing(self):
        self.assertEqual(self.s.longest_increasing_subsequence_bu([5, 4, 3, 2, 1]), 1)

    def test_single_element(self):
        self.assertEqual(self.s.longest_increasing_subsequence_bu([42]), 1)

    def test_two_elements_increasing(self):
        self.assertEqual(self.s.longest_increasing_subsequence_bu([1, 2]), 2)

    def test_two_elements_decreasing(self):
        self.assertEqual(self.s.longest_increasing_subsequence_bu([2, 1]), 1)

    def test_all_equal(self):
        self.assertEqual(self.s.longest_increasing_subsequence_bu([7, 7, 7, 7]), 1)

    def test_lis_not_at_end(self):
        self.assertEqual(self.s.longest_increasing_subsequence_bu([2, 3, 7, 101, 1]), 4)

    def test_negative_numbers(self):
        self.assertEqual(
            self.s.longest_increasing_subsequence_bu([-5, -3, -1, 0, 2]), 5
        )

    def test_mixed_positive_negative(self):
        self.assertEqual(
            self.s.longest_increasing_subsequence_bu([3, -2, 0, 3, 6, 1]), 4
        )


if __name__ == "__main__":
    unittest.main()
