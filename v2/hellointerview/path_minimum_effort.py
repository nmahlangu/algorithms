from typing import *
import heapq
from collections import defaultdict


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0

        rows: int = len(heights)
        cols: int = len(heights[0])
        effort_grid: list[list[float]] = [
            [float("inf") for _ in range(cols)] for _ in range(rows)
        ]

        # (max_effort, row, col)
        heap: list[tuple[int, int, int]] = [(0, 0, 0)]
        dirs: list[tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while heap:
            effort, row, col = heapq.heappop(heap)

            # check if reached destination
            if row == rows - 1 and col == cols - 1:
                return effort

            # already found a better path there
            if effort > effort_grid[row][col]:
                continue

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort: int = max(
                        effort, abs(heights[row][col] - heights[nr][nc])
                    )
                    if new_effort < effort_grid[nr][nc]:
                        effort_grid[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))

        return int(effort_grid[rows - 1][cols - 1])
