# Given an unsorted array, find the max length of subsequence in which
# the numbers are in incremental order.
#
# Example:
# [7,2,3,1,5,8,9,6] -> [2,3,5,8,9] -> 5

result = 0
cache = {}

def max_len(arr):
    if not arr:
        return 0
    return max_helper(arr,len(arr)-1)

def max_helper(arr,i):
    # memoization
    global cache
    if i in cache:
        return cache[i]

    # base case
    if i == 0:
        return 1

    # recursive case
    max_ending_here = 1
    for j in xrange(i):
        prev = max_helper(arr,j)
        if arr[j] < arr[i]:
            max_ending_here = max(max_ending_here, prev + 1)        

    global result
    result = max(result, max_ending_here)
    cache[i] = result    
    return max_ending_here

# Solution: TODO
