# Given a set of candidate numbers (C) and a target number (T), find all 
# unique combinations in C where the candidate numbers sums to T. The same
# number may be chosen from C unlimited number of times
# 
# Note:
# - All numbers (including target) will be positive integers.
# - Elements in a combination (a1, a2,... , ak) must be in non-descending 
#   order. (ie, a1 <= a2 <= ... <= ak).
# The solution set must not contain duplicate combinations.
# 
# For example,
# [2,3,6,7], 7 -> [2,2,3], 7

class Solution(object):
    def __init__(self):
        self.result = []

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # error checking
        if not candidates:
            return 0
        candidates.sort()
        self.helper(candidates, target, [])
        return self.result

    def helper(self, candidates, target, tmp_result):
        # base
        if not target:
            self.result.append(tmp_result)
            return

        # recursive
        for i, num in enumerate(candidates):
            if target - num >= 0:
                self.helper(candidates[:i+1],target-num,[num]+tmp_result)
        
# Solution: This problem is the same as the popular coin denominations one.
# https://github.com/nmahlangu/algorithms/blob/master/CoinDenominations.py
