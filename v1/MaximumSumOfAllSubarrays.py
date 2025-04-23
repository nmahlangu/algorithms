# A sub-array has one number of some continous numbers. Given an integer
# array with positive and negative numbers, get the maximum sum of all
# sub-arrays.

def max_sum(arr):
    if not arr:
        return 0
    if max(arr) < 0:
        return max(arr)

    max_ending_here = 0
    max_so_far = 0
    for num in arr:
        max_ending_here += num
        if max_ending_here < 0:
            max_ending_here = 0
        else:
            max_so_far = max(max_ending_here,max_so_far)
    return max_so_far

# Define f(i) as the maximum sum of a sum-array ended with the ith number.
# f(i) can then be written as f(i) = { arr[i] if i == 0 or f(i-1) < 0
                                       arr[i] + f(i - 1) if i != 0 and f(i-1) > 0
# Time complexity is O(n) and space complexity is O(1).
