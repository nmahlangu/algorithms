import unittest


class Solution:
    def employeeFreeTime(self, schedule: list[list[list[int]]]):
        if not schedule:
            return []

        all_sched: list[int] = []
        for s in schedule:
            for interval in s:
                all_sched.append(interval)

        all_sched.sort(key=lambda x: x[0])
        merged = [all_sched[0]]

        for i in range(1, len(all_sched)):
            if all_sched[i][0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], all_sched[i][1])
            else:
                merged.append(all_sched[i])

        result: list[tuple] = []
        for i in range(len(merged) - 1):
            result.append((merged[i][1], merged[i + 1][0]))

        return result


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().employeeFreeTime([[[2, 4], [7, 10]], [[1, 5]], [[6, 9]]])
        self.assertEqual([(5, 6)], actual)


if __name__ == "__main__":
    unittest.main()
