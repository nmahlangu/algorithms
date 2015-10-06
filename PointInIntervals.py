# You are given n integer intervals [a_i,b_i] on the real axes, and the
# absolute value of the coordinates is bounded by M. Determine a point
# that belongs to the maximum number of intervals. Point x belongs to the
# interval [a,b] if a <= x <= b

intervals = [(1,5),(2,4),(3,13),(6,10),(10,12),(11,13)]

def cal_max_intervals(intervals):
    if not intervals:
        return 0

    arr = []
    for elt in intervals:
        arr.append((elt[0],1))
        arr.append((elt[1],-1))
    arr.sort(key=lambda x:(x[0],-x[1]))

    current = 0
    max_so_far = 0
    for i, item in enumerate(arr):
        current += item[1]
        max_so_far = max(max_so_far,current)
    return max_so_far    

# Solution: Create an array of tuples, where a tuple is either a) the start
# of an interval, in which case the tuple is (start,1), or b) the end of
# an interval, in which case the tuple is (end,-1). Then sort the array
# of tuples with the key=lambda x: (x[0],-x[1]), as you want to process
# left ends before right ends when traversing through the points. Finally,
# iterate through the array and keep a running sum and add each element's
# elt[1]: it will be 1 if a new interval is starting or -1 if a current
# interval is ending. Time complexity is O(nlog(n)) and space complexity
# is O(n).

