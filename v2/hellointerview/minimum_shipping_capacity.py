import unittest


class Solution:
    # given quantities and capacity, use greedy approach to calculate
    # the minimum number of boxes
    def calc_greedy_min_boxes_for_capacity(
        self, quantities: list[int], capacity: int
    ) -> int:
        count: int = 0
        for q in quantities:
            count += (q + capacity - 1) // capacity
        return count

    def minimumShippingCapacity(self, quantities: list[int], maxBoxes: int):
        left: int = 1
        right: int = max(quantities)

        while left < right:
            mid: int = (left + right) // 2
            num_boxes: int = self.calc_greedy_min_boxes_for_capacity(
                quantities=quantities, capacity=mid
            )

            # found quantity that works, try to check a smaller one
            if num_boxes <= maxBoxes:
                right = mid

            # num boxes is too much, try higher capacities
            else:
                left = mid + 1

        return left


class TestSolution(unittest.TestCase):
    def test1(self):
        actual = Solution().minimumShippingCapacity(quantities=[1, 2, 5, 9], maxBoxes=6)
        self.assertEqual(actual, 5)

    def test2(self):
        actual = Solution().minimumShippingCapacity(
            quantities=[3, 6, 7, 11], maxBoxes=8
        )
        self.assertEqual(actual, 4)


if __name__ == "__main__":
    unittest.main()
