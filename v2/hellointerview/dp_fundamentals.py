import unittest

"""
You can climb a staircase by taking either 1 or 2 steps at a time. If there are n steps in 
the staircase, how many distinct ways are there to climb to the top step? Assume stairs
will always be positive
"""


class Solution:
    def climb_stairs_dp_top_down(self, stairs: int) -> int:
        if stairs <= 1:
            return 1

        return self.climb_stairs_dp_top_down(
            stairs - 1
        ) + self.climb_stairs_dp_top_down(stairs - 2)

    def climb_stairs_2(self, stairs: int) -> int:
        if stairs < 0:
            return -1
        
        memo: dict[int, int] = {}
        return self.climb_stairs_dp_top_down(stairs)

    def climb_stairs_dp_top_down_memo(self, stairs: int, memo: dict[int, int]) -> int:
        if stairs <= 1:
            return 1

        if stairs in memo:
            return memo[stairs]

        memo[stairs] = self.climb_stairs_dp_top_down(
            stairs - 1
        ) + self.climb_stairs_dp_top_down(stairs - 2)
        
        return memo[stairs]

    def climb_stairs_bottom_up_1(self, stairs: int) -> int:
        if stairs <= 1:
            return 1

        dp: list[int] = [0] * (stairs + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, stairs + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[stairs]

    def climb_stairs_bottom_up_2(self, stairs: int) -> int:
        if stairs <= 1:
            return 1

        prev: int = 1
        curr: int = 1

        for _ in range(2, stairs + 1):
            new: int = prev + curr
            prev = curr
            curr = new

        return curr

class TestSolution(unittest.TestCase):
    def test_zero_stairs(self) -> None:
        actual = Solution().climb_stairs_dp_top_down(0)
        self.assertEqual(1, actual)

    def test_one_stair(self) -> None:
        actual = Solution().climb_stairs_dp_top_down(1)
        self.assertEqual(1, actual)

    def test_two_stairs(self) -> None:
        actual = Solution().climb_stairs_dp_top_down(2)
        self.assertEqual(2, actual)

    def test_three_stairs(self) -> None:
        actual = Solution().climb_stairs_dp_top_down(3)
        self.assertEqual(3, actual)

    def test_four_stairs(self) -> None:
        actual = Solution().climb_stairs_dp_top_down(4)
        self.assertEqual(5, actual)

    def test_five_stairs(self) -> None:
        actual = Solution().climb_stairs_dp_top_down(5)
        self.assertEqual(8, actual)

    def test_ten_stairs(self) -> None:
        actual = Solution().climb_stairs_dp_top_down(10)
        self.assertEqual(89, actual)



class TestSolution2(unittest.TestCase):
    def test_zero_stairs(self) -> None:
        actual = Solution().climb_stairs_2(0)
        self.assertEqual(1, actual)

    def test_one_stair(self) -> None:
        actual = Solution().climb_stairs_2(1)
        self.assertEqual(1, actual)

    def test_two_stairs(self) -> None:
        actual = Solution().climb_stairs_2(2)
        self.assertEqual(2, actual)

    def test_three_stairs(self) -> None:
        actual = Solution().climb_stairs_2(3)
        self.assertEqual(3, actual)

    def test_four_stairs(self) -> None:
        actual = Solution().climb_stairs_2(4)
        self.assertEqual(5, actual)

    def test_five_stairs(self) -> None:
        actual = Solution().climb_stairs_2(5)
        self.assertEqual(8, actual)

    def test_ten_stairs(self) -> None:
        actual = Solution().climb_stairs_2(10)
        self.assertEqual(89, actual)

    def test_negative_stairs(self) -> None:
        actual = Solution().climb_stairs_2(-1)
        self.assertEqual(-1, actual)


class TestSolutionBottomUp1(unittest.TestCase):
    def test_zero_stairs(self) -> None:
        actual = Solution().climb_stairs_bottom_up_1(0)
        self.assertEqual(1, actual)

    def test_one_stair(self) -> None:
        actual = Solution().climb_stairs_bottom_up_1(1)
        self.assertEqual(1, actual)

    def test_two_stairs(self) -> None:
        actual = Solution().climb_stairs_bottom_up_1(2)
        self.assertEqual(2, actual)

    def test_three_stairs(self) -> None:
        actual = Solution().climb_stairs_bottom_up_1(3)
        self.assertEqual(3, actual)

    def test_four_stairs(self) -> None:
        actual = Solution().climb_stairs_bottom_up_1(4)
        self.assertEqual(5, actual)

    def test_five_stairs(self) -> None:
        actual = Solution().climb_stairs_bottom_up_1(5)
        self.assertEqual(8, actual)

    def test_ten_stairs(self) -> None:
        actual = Solution().climb_stairs_bottom_up_1(10)
        self.assertEqual(89, actual)


class TestSolutionBottomUp2(unittest.TestCase):
    def test_zero_stairs(self) -> None:
        actual = Solution().climb_stairs_bottom_up_2(0)
        self.assertEqual(1, actual)

    def test_one_stair(self) -> None:
        actual = Solution().climb_stairs_bottom_up_2(1)
        self.assertEqual(1, actual)

    def test_two_stairs(self) -> None:
        actual = Solution().climb_stairs_bottom_up_2(2)
        self.assertEqual(2, actual)

    def test_three_stairs(self) -> None:
        actual = Solution().climb_stairs_bottom_up_2(3)
        self.assertEqual(3, actual)

    def test_four_stairs(self) -> None:
        actual = Solution().climb_stairs_bottom_up_2(4)
        self.assertEqual(5, actual)

    def test_five_stairs(self) -> None:
        actual = Solution().climb_stairs_bottom_up_2(5)
        self.assertEqual(8, actual)

    def test_ten_stairs(self) -> None:
        actual = Solution().climb_stairs_bottom_up_2(10)
        self.assertEqual(89, actual)


if __name__ == "__main__":
    unittest.main()
