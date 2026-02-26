from typing import *
import unittest

class Solution:
    def maxProfit(self, prices: List[int]):
        if not prices:
            return 0

        max_p: int = 0
        min_seen: int = prices[0]

        for price in prices:
            min_seen = min(min_seen, price)
            max_p = max(max_p, price - min_seen)

        return max_p

"""
prices = [3,4,6,2,5,8]
max_p:    0 1 3 3 3 6
min_seen: 3 3 3 2 2 2
"""


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example(self):
        self.assertEqual(self.s.maxProfit([3, 4, 6, 2, 5, 8]), 6)

    def test_classic(self):
        self.assertEqual(self.s.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_decreasing(self):
        self.assertEqual(self.s.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_single_element(self):
        self.assertEqual(self.s.maxProfit([5]), 0)

    def test_two_elements_profit(self):
        self.assertEqual(self.s.maxProfit([1, 5]), 4)

    def test_two_elements_loss(self):
        self.assertEqual(self.s.maxProfit([5, 1]), 0)

    def test_all_same(self):
        self.assertEqual(self.s.maxProfit([3, 3, 3, 3]), 0)

    def test_buy_at_end_of_dip(self):
        self.assertEqual(self.s.maxProfit([10, 2, 11]), 9)

    def test_empty(self):
        self.assertEqual(self.s.maxProfit([]), 0)

    def test_profit_at_end(self):
        self.assertEqual(self.s.maxProfit([2, 1, 4, 5, 2, 9]), 8)


if __name__ == "__main__":
    unittest.main()