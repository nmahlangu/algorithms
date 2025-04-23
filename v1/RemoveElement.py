# Given an array and a value, remove all instances of that value in place and return the new length.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        i = j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i

# Solution: Have 2 pointers start at the first and second element. Traverse through the
# array with the second element and whenever the element it's pointing at is not
# equal to val, write it at the location of the first pointer and increment where
# the pointer points. Time complexity is O(n) and space complexity is O(1)
