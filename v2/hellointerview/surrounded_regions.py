from typing import *


class Solution:
    def surrounded_regions(self, grid: List[List[str]]):
        if not grid:
            return []

        rows: int = len(grid)
        cols: int = len(grid[0])

        for row in range(rows):
            self.dfs_mark_s(row=row, col=0, grid=grid)
            self.dfs_mark_s(row=row, col=cols - 1, grid=grid)

        for col in range(cols):
            self.dfs_mark_s(row=0, col=col, grid=grid)
            self.dfs_mark_s(row=rows - 1, col=col, grid=grid)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "S":
                    grid[row][col] = "O"
                elif grid[row][col] == "O":
                    grid[row][col] = "X"

        return grid

    def dfs_mark_s(self, row: int, col: int, grid: List[List[str]]):
        if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1:
            return

        if grid[row][col] != "O":
            return

        grid[row][col] = "S"
        coords: List[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r, c in coords:
            self.dfs_mark_s(row=row + r, col=col + c, grid=grid)
