# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        return self.customBinarySearch(nums, target, 0, len(nums) - 1)        

    def customBinarySearch(self, nums, target, left, right):
        mid = (left + right) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.customBinarySearch(nums, target, left, mid - 1) if left < mid else mid
        else:
            return self.customBinarySearch(nums, target, mid + 1, right) if mid < right else mid + 1

# If the target is present in the array, return that index. If it's not, we want to find the
# last element we checked in the array. If the target is smaller than that element, we insert
# the target at that index. If the target is greater than that element, we insert the target 
# one index to the right. Time complexity is O(log(n)) and space complexity is O(1).
