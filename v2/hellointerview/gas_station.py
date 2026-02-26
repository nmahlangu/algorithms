

class Solution:
    def can_complete_circuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start: int = 0
        fuel: int = 0

        for i in range(len(gas)):
            if fuel - cost[i] + gas[i] < 0:
                start = i + 1
                fuel = 0

            else:
                fuel += gas[i] - cost[i]

        return start


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example(self):
        self.assertEqual(self.s.can_complete_circuit([5,2,0,3,3], [1,5,5,1,1]), 3)

    def test_no_solution(self):
        self.assertEqual(self.s.can_complete_circuit([2, 3, 4], [3, 4, 3]), -1)

    def test_start_at_zero(self):
        self.assertEqual(self.s.can_complete_circuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]), 4)

    def test_single_station(self):
        self.assertEqual(self.s.can_complete_circuit([5], [3]), 0)

    def test_single_station_no_solution(self):
        self.assertEqual(self.s.can_complete_circuit([3], [5]), -1)

    def test_all_equal(self):
        self.assertEqual(self.s.can_complete_circuit([3, 3, 3], [3, 3, 3]), 0)

    def test_start_at_last(self):
        self.assertEqual(self.s.can_complete_circuit([0, 0, 10], [3, 3, 4]), 2)

    def test_leetcode_example(self):
        self.assertEqual(self.s.can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)


if __name__ == "__main__":
    unittest.main()