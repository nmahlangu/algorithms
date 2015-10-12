# Given an array of integers, find the largest sum of contiguous subarray in
# that array.

def largest_sum(arr):
    if not arr:
        return 0

    max_sum = curr_sum = arr[0]
    for elt in arr[1:]:
        curr_sum = max(curr_sum + elt, elt)
        max_sum = max(max_sum,curr_sum)
    return max_sum

# Best way to think about this problem is in terms of dynamic programming.
# Keep a global max and update it to be the max of the itself and the sum of 
# the current contiguous subarray that we're looking at, and reset our current 
# contiguous subarray sum to ith element if the current sum plus the number 
# at the ith index is less then the current sum. Time complexity is O(n) 
# and space complexity is O(1).
