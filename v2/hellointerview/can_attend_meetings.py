import unittest


class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]):
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().canAttendMeetings([(1, 5), (3, 9), (6, 8)])
        self.assertEqual(False, actual)


if __name__ == "__main__":
    unittest.main()
