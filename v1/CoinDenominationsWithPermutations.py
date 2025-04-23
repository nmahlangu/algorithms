# Given an array of integers and a target sum, return a list of lists where each sublist
# sums to the target element. You can assume the array has no duplicates in it. Furthermore,
# you an use any element an unlimited number of times.
#
# For example,
# [2,3,7] -> [[2,2,3],[2,3,2],[3,2,2],[7]]

result = []

def get_lists(arr,target):
    if not arr:
        return
    arr.sort()
    helper(arr,target,[])

def helper(arr,target,tmp):
    # base
    if not target:
        global result
        result.append(tmp)        

    # recursive
    for i, num in enumerate(arr):
        if target - num >= 0:
            helper(arr,target-num,[num]+tmp)

# Solution: Time complexity is O(n^n), since making O(n) recursive calls in
# each recursion, and space complexity is O(n^n) since storing all those results. 
