"""

Given an array of distinct integers candidates and a target integer target, generate all unique combinations of 
candidates which sum to target. The combinations may be returned in any order, and the same number may be chosen 
from candidates an unlimited number of times.

Constraints:

All values in candidates are positive integers.
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

"""

import unittest


class Solution:
    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        if not candidates:
            return []

        candidates.sort()
        result: list[list[int]] = []
        self.dfs(0, [], target, candidates, result)
        return result

    def dfs(
        self,
        start_cand: int,
        path: list[int],
        target: int,
        candidates: list[int],
        result: list[list[int]],
    ) -> None:
        if target == 0:
            result.append(path[:])
            return

        for i in range(start_cand, len(candidates)):
            if candidates[i] > target:
                return

            path.append(candidates[i])
            self.dfs(i, path, target - candidates[i], candidates, result)
            path.pop()


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().combination_sum([2, 3, 6, 7], 7)
        self.assertEqual([[2, 2, 3], [7]], actual)


if __name__ == "__main__":
    unittest.main()
