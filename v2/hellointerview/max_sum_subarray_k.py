import unittest


class Solution:
    def maxSum(self, nums: list[int], k: int):
        max_s: int = 0
        start: int = 0

        for end in range(len(nums)):
            if end - start + 1 < k:
                continue

            max_s = max(max_s, sum(nums[start : end + 1]))
            start += 1

        return max_s


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().maxSum([2, 1, 5, 1, 3, 2], 3)
        self.assertEqual(9, actual)


if __name__ == "__main__":
    unittest.main()
