# Given a list of integers, return the sum of the maximum subset that doesn't
# include any two adjacent elements.

max_helper_dict = {}
def calc_max_subset(arr):
    if not arr:
        return 0
    return calc_max_helper(arr,len(arr)-1)

def calc_max_helper(arr, i):
    # base case
    if i == 0 or i == 1:
        return arr[i]

    # recursive case
    global max_helper_dict
    if i in max_helper_dict:
        return max_helper_dict[i]
    else:
        a = arr[i] + calc_max_helper(arr,i-2)
        b = calc_max_helper(arr,i-1)
        max_helper_dict[i] = max(a,b)
        return max(a,b)

# Solution: Given an array of size n arr[0.....n-1], define a function f(i)
# to be the maximum sum from arr[0....i] where i is the last element in the
# sum. Using dynamic programming, we can solve each subproblem separately.
# If i == 0, return the 0th element. Else if i == 1, return the 1st element.
# Else, return the maximum of the arr[i]th element + f(i-2), or f(i-1). 
# Time complexity O(n^2) and space complexity is O(n).
