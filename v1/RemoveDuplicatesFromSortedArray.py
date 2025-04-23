# Given a sorted array, remove the duplicates in place such that each element appear only once 
# and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# For example,
# Given input array nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 
# respectively. It doesn't matter what you leave beyond the new length.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i + 1

# Solution: Have 2 pointers start at the first and second element of the array. Traverse
# the array with the second pointer and whenever a non-duplicate element is encountered,
# move the first pointer over an element, overwrite where it points with the non-duplicate
# that the second pointer is pointing at, then increment the index of the second pointer.
# Return the first pointer + 1 (since 0 indexing). Time complexity is O(n) and space
# complexity is O(1)
