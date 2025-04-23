# Given a set of candidate numbers (C) and a target number (T), find all
# unique combinations in C where the candidate numbers sums to T. The same
# number may be chosen from C unlimited number of times.
#
# Each number in C may only be used once in the combination
#
# Note:
# - All numbers (including target) will be positive integers.
# - Elements in a combination (a1, a2,... , ak) must be in non-descending
#   order. (ie, a1 <= a2 <= ... <= ak).
# The solution set must not contain duplicate combinations.
#
# For example,
# [2,3,6,7], 7 -> [2,2,3], 7

from sets import Set

class Solution(object):
    def __init__(self):
        self.result = []

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return 0
        candidates.sort()
        self.helper(candidates,target,[])
        return self.result

    def helper(self,candidates,target,tmp_result):
        # base case
        if not target:
            self.result.append(tmp_result)
            return
        elif not candidates:
            return        

        # recursive case
        i = 0
        while i < len(candidates):
            if i == 0 or candidates[i] != candidates[i-1]:
                num = candidates[i]
                if target - num >= 0:
                    self.helper(candidates[i+1:],target-num,tmp_result+[num])
            i += 1

# Solution: Similar to CombinationSum, but you need to make sure not to
# add the same number to an intermediate result more than once. But basically
# the subproblem at each step of the recursion is looping over the numbers
# you have left and seeing if adding it to the intermediate result (aka subtracting
# it from target) and recursing on the rest). Time complexity is O(n^n) and
# space complexity is O(n^n).
