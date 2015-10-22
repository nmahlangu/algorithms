# Given an array of integers and a target sum, return the number of ways you can combine
# elements in the array to sum to the target element. You can assume the array has no 
# duplicates in it. Furthermore, you an use any element an unlimited number of times.
#
# For example,
# [2,3,7] -> [[2,2,3],[2,3,2],[3,2,2],[7]] -> 4

cache = {}

def count(arr,target):
    # check if answer has been memoized earliero
    if target in cache:
        return cache[target]    

    # base case
    if target < 0:
        return 0
    elif target == 0:
        return 1

    # recursive case
    num_ways = 0
    for i in xrange(len(arr)):
        num_ways += count(arr,target-arr[i])
    cache[target] = num_ways
    return num_ways

print count([2,3,7],7)

# This problem is basically counting the number of results in 
# CoinDenominationsWithPermutations.py. Time complexity is O(target * len(arr)) 
# and space complexity is O(target).
