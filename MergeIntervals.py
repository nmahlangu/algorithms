# Given a collection of intervals, merge all overlapping intervals.
# For example,
#   Given [(1,3),(2,6),(8,10),(15,18)]
#   Return [(1,6),(8,10),(15,18)]

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []

        intervals = sorted(intervals,key=lambda x:x.start)
        curr = intervals[0]
        result = []
        
        for i, next in enumerate(intervals):
            # overlapping
            if curr.end >= next.start:
                merged = Interval(curr.start,max(curr.end,next.end))
                curr = merged
            # not overlapping        
            else:
                result.append(curr)
                curr = next
        result.append(curr)
        return result

# Solution: The key to solving this problem is to sort the intervals
# by their starting time before doing anything. Once done, there are
# two cases when comparing your current and next interval. If the
# current one ends before the next one starts, then you want to keep
# both. However, if the current one ends before the next one starts,
# then you want to replace both of those intervals with a new intervals
# with a new interval that starts when the current interval started
# and ends at max(current interval's end, next interval's end). Do
# this for all intervals and return the final set of intervals. Time
# complexity is O(nlog(n)), space complexity is O(1).
