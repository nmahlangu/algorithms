from typing import *
from collections import deque

"""
You are given an m x n binary matrix grid where each cell contains either a 0 or a 1.

Write a function that returns a matrix of the same dimensions where each cell contains 
the distance to the nearest 0 in the original matrix. The distance between two adjacent 
cells is 1. If there is no 0 in the grid, return -1 for each cell.
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]):
        if not mat:
            return []

        rows: int = len(mat)
        cols: int = len(mat[0])
        queue: deque[tuple[int, int]] = deque([])
        result = [[-1 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))

        distance: int = 1
        directions: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)] 

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and result[nr][nc] == -1:
                        result[nr][nc] = distance
                        queue.append((nr, nc))

            distance += 1

        return result