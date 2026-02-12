from typing import *


class Solution:
    def number_of_islands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        count: int = 0
        visited: set[tuple[int, int]] = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    count += 1
                    self.dfs(row=row, col=col, grid=grid, visited=visited)

        return count

    def dfs(
        self, row: int, col: int, grid: List[List[int]], visited: set[tuple[int, int]]
    ) -> int:
        if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1:
            return

        if grid[row][col] != 1:
            return

        if (row, col) in visited:
            return

        visited.add((row, col))
        coords: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i, j in coords:
            self.dfs(row=row + i, col=col + j, grid=grid, visited=visited)
        return
