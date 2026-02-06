import unittest

class Solution:
    # greedy approach to making splits < k, returns # splits
    def arr_to_min_splits_given_k(self, nums: list[int], k: int) -> int:
        splits: int = 1
        r_sum: int = 0

        for _, item in enumerate(nums):
            if r_sum + item > k:
                r_sum = item
                splits += 1
            else:
                r_sum += item

        return splits


    def splitArray(self, nums: list[int], k: int):
        left: int = max(nums)
        right: int = sum(nums)

        while left < right:
            mid = (left + right) // 2
            if k < self.arr_to_min_splits_given_k(nums=nums, k=mid):
                left = mid + 1
            else:
                right = mid

        return left

class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().splitArray([6, 3, 9, 2, 1, 8], 2)
        self.assertEqual(18, actual)


if __name__ == "__main__":
    unittest.main()
