from typing import *
from collections import deque

class Solution:
    def rotting_oranges(self, grid: List[List[str]]):
        if not grid:
            return -1

        queue: deque[tuple(int, int)] = deque([(0, 0)])
        fresh_orgs: int = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "R":
                    queue.append((row, col))
                elif grid[row][col] == "F":
                    fresh_orgs += 1

        num_minutes: int = 0
        directions: list[tuple[int, int]] = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows: int = len(grid)
        cols: int = len(grid[0])

        while queue and fresh_orgs > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "F":
                        grid[nr][nc] = "R"
                        fresh_orgs -= 1
                        queue.append((nr, nc))

            num_minutes += 1

        return num_minutes if fresh_orgs == 0 else -1