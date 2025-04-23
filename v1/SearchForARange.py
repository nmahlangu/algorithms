# Given a sorted array of integers, find the starting and ending position of a 
# given target value. Your algorithm's runtime complexity must be in the 
# order of O(log n).If the target is not found in the array, return [-1, -1].
# For example,
#   Given [5, 7, 7, 8, 8, 10] and target value 8,
#   return [3, 4].

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return result
        result = [-1,-1]
        left = right = self.binarySearch(nums, target, 0, len(nums) - 1)
        if left == right == -1:
            return result
        
        # get lower bound
        while True and left > 0:
            left_tmp = self.binarySearch(nums, target, 0, left - 1)
            if left_tmp == 0:
                left = 0
                break
            elif left_tmp == -1:
                break
            else:
                left = left_tmp
        result[0] = left

        # get upper bound
        while True and right < len(nums) - 1:
            right_tmp = self.binarySearch(nums, target, right + 1, len(nums) - 1)
            if right_tmp == len(nums) - 1:
                right = right_tmp
                break
            elif right_tmp == -1:
                break
            else:
                right = right_tmp
        result[1] = right

        return result  
            
    def binarySearch(self, nums, target, left, right):
        if not nums:
            return -1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1 

# Solution: Since the solution must be O(log(n)), we must use binary search.
# Binary search for the element in the array. If it's not there, return [-1,-1].
# To find the lower bound, repeatedly binary search to the left of that element and 
# whenever you find another matching element, limit the upper bound of the binary 
# search to the element before that. To find the upper bound, repeatedly binary
# search to the right of that element and whenever you find another matching
# element, limit the lower bound of the binary search to the element before that.
# Time complexity is O(log(n)) and space complexity is O(1).
