from typing import *

"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once.

"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        elif not word:
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if word[0] == board[row][col]:
                    if self.backtrack(board, row, col, 0, word):
                        return True

        return False

    def backtrack(
        self, board: List[List[str]], row: int, col: int, idx: int, word: str
    ) -> bool:
        if idx == len(word):
            return True
        elif not (0 <= row < len(board)):
            return False
        elif not (0 <= col < len(board[0])):
            return False
        elif board[row][col] != word[idx]:
            return False

        old_let: str = board[row][col]
        board[row][col] = "#"

        found: bool = (
            self.backtrack(board, row + 1, col, idx + 1, word)
            or self.backtrack(board, row - 1, col, idx + 1, word)
            or self.backtrack(board, row, col + 1, idx + 1, word)
            or self.backtrack(board, row, col - 1, idx + 1, word)
        )

        board[row][col] = old_let
        return found
