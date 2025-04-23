# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, 
# target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
# For example, given array S = {-1 2 1 -4}, and target = 1.
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return target
        nums.sort()
        result = float('inf')
        min_diff = float('inf')
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                elt_sum = nums[i] + nums[start] + nums[end]
                diff = abs(target - elt_sum)
                if diff < min_diff:
                    min_diff = diff
                    result = elt_sum
                if elt_sum < target:
                    start += 1
                else:
                    end -= 1
        return result

# Similarly to 3Sum, iterate over each element of the array and for each element, have 2 pointers:
# start, which is the next element in the array and end, which is the last element in the array. 
# Sum the three numbers at those indices and if the absolute value of target minus that sum is less
# than the absolute value of target minus any previous sum, update the result to be the sum of 
# the three numbers at those indices. If the sum is less than target, increment start; if the sum
# is greater than target, decrement end. Time complexity is O(n^2) and space complexity is O(1).
