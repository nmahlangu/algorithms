from typing import *


class Solution:
    def pacific_atlantic_flow(self, grid: List[List[int]]) -> list[list[int]]:
        if not grid or not grid[0]:
            return []

        rows: int = len(grid)
        cols: int = len(grid[0])

        atlantic_reachable: set[list[int]] = set()
        pacific_reachable: set[list[int]] = set()

        for row in range(rows):
            self.dfs(row=row, col=0, grid=grid, reachable=pacific_reachable)
            self.dfs(row=row, col=cols - 1, grid=grid, reachable=atlantic_reachable)

        for col in range(cols):
            self.dfs(row=0, col=col, grid=grid, reachable=pacific_reachable)
            self.dfs(row=rows - 1, col=col, grid=grid, reachable=atlantic_reachable)

        return list(atlantic_reachable & pacific_reachable)

    def dfs(self, row: int, col: int, grid: list[list[int]], reachable: set[list[int]]):
        if (row, col) in reachable:
            return

        reachable.add((row, col))
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr: int = row + dr
            nc: int = col + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if grid[nr][nc] >= grid[row][col]:
                    self.dfs(row=nr, col=nc, grid=grid, reachable=reachable)
