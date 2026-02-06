class Solution:
    def mergeIntervals(self, intervals: list[list[int]]):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        result: list[list[int]] = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])

        return result
