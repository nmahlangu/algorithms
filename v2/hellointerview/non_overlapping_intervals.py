class Solution:
    def nonOverlappingIntervals(self, intervals: list[list[int]]):
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        end: int = intervals[0][1]
        count: int = 1

        for i in range(1, len(intervals)):
            # non-overlapping interval found
            if intervals[i][0] >= end:
                count += 1
                end = intervals[i][1]

        return len(intervals) - count
