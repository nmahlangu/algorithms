import unittest


class Solution:
    def maxSum(self, nums: int, k: int):
        max_sum: int = 0
        start: int = 0
        state: dict[int, int] = {}
        curr_sum: int = 0

        for end in range(len(nums)):
            curr_sum = curr_sum + nums[end]
            state[nums[end]] = state.get(nums[end], 0) + 1

            if end - start + 1 == k:
                if len(state) == k:
                    max_sum = max(max_sum, curr_sum)

                curr_sum = curr_sum - nums[start]
                state[nums[start]] = state[nums[start]] - 1
                if state[nums[start]] == 0:
                    del state[nums[start]]
                start += 1

        return max_sum


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().maxSum([3, 2, 2, 3, 4, 6, 7, 7, -1], 4)
        self.assertEqual(20, actual)


if __name__ == "__main__":
    unittest.main()
