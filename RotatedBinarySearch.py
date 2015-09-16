# Suppose a sorted array is rotated at some pivot unknown to you beforehand
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicates exist in the array

class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            if nums[m] == target:
                return m
        
            # bottom half is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # top half is sorted
            else:
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

# Solution: While it may seem like it, you don't have to find where the array has been
# rotated. Comparing the mid to the first and last element, we can determine that either
# the bottom half or top half is in a strictly increasing order. If the target is in
# the half that is in strictly increasing order, recurse on that half of the array,
# else recurse on the other half of the array. Time complexity is O(log(n)) and space
# complexity is O(1).
