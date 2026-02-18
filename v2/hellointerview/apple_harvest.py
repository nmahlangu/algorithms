import unittest


class Solution:
    def calc_harvest_hours(self, apples: list[int], rate: int) -> int:
        hours: int = 0
        for i in range(len(apples)):
            hours += (apples[i] + rate - 1) // rate
        return hours

    def minHarvestRate(self, apples: list[int], h: int):
        left: int = 1
        right: int = max(apples)

        while left < right:
            mid: int = (left + right) // 2
            hours: int = self.calc_harvest_hours(apples=apples, rate=mid)
            if hours > h:
                left = mid + 1
            else:
                right = mid

        return left


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().minHarvestRate([25, 9, 23, 8, 3], 5)
        self.assertEqual(25, actual)


if __name__ == "__main__":
    unittest.main()
