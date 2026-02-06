import unittest


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # found it
            if nums[mid] == target:
                return mid

            # left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # right half is sorted
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
        self.assertEqual(4, actual)

    def test_example2(self):
        actual = Solution().search([4, 5, 6, 7, 0, 1, 2], 3)
        self.assertEqual(-1, actual)


if __name__ == "__main__":
    unittest.main()
