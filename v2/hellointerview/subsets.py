from typing import *


class Solution:
    def subsets(self, nums: List[int]):
        result: list[list[int]] = []
        self.dfs(0, [], nums, result)
        return result

    def dfs(self, idx: int, path: list[int], nums: int, result: list[int]):
        if idx == len(nums):
            result.append(path[:])
            return

        path.append(nums[idx])
        self.dfs(idx + 1, path, nums, result)

        path.pop()
        self.dfs(idx + 1, path, nums, result)
