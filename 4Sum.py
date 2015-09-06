
# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? 
# Find all unique quadruplets in the array which gives the sum of target.
# Notes:
#   Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
#   The solution set must not contain duplicate quadruplets.
#   For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
#    A solution set is:
#    (-1,  0, 0, 1)
#    (-2, -1, 1, 2)
#    (-2,  0, 0, 2)

from sets import Set

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        quadruplets = set()
        for i in range(len(nums)):    
            for j in range(i+1,len(nums)):
                start = j+1
                end = len(nums) - 1
                while start < end:
                    num_sum = nums[i] + nums[j] + nums[start] + nums[end]
                    if num_sum == target:
                        quadruplets.add((nums[i],nums[j],nums[start],nums[end]))
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
                    elif num_sum < target:
                        start += 1
                    else:
                        end -= 1
        return list(map(lambda x: list(x),quadruplets))

# Very similar to 3Sum. Have 2 loops which generate all pairs (i,j) such that i < j. For each of those pairs,
# have 2 pointers at the next element (start) and the last element of the array (end), respectively. If the 4
# numbers at those indices sum to the target, store an array of those 4 numbers. If the numbers to more than the
# target, move the end pointer left one element. If the numbers sum to less than the target, move the start pointer
# right one element. Time complexity is O(n^3) and space complexity is O(n).
