# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique 
# triplets in the array which gives the sum of zero.
# Notes: 
#   Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
#   The solution set must not contain duplicate triplets.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        result = []
        for i in range(len(nums)):
            elt = nums[i]
            if i == 0 or nums[i] > nums[i - 1]:
                start = i + 1 
                end = len(nums) - 1
                while start < end:
                    if elt + nums[start] + nums[end] == 0:
                        result.append([elt,nums[start],nums[end]])
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start-1]:             
                            start += 1
                        while start < end and nums[end] == nums[end+1]:
                            end -= 1
                    elif elt + nums[start] + nums[end] < 0:
                        start += 1
                    else:
                        end -= 1
        return result

# Solution: For each element of the array, have 2 pointers at the next element (start) and the last element of
# the array (end), respectively. If the 3 numbers sum to less than 0, move the start pointer right one element.
# If the numbers sum to more than 0, move the end pointer left one element. Repeat this until start == end. Time
# complexity is O(n^2) and space complexity is O(n).
