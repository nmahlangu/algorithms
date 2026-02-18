"""

dfs()
if no queens left:
    append path
    return

iterate over remaining options from curr_row, curr_col
    if valid option (no queen in curr_row, curr_col, or diagonals)
        append quene to path
        recurse
        pop queen

"""

import unittest


class Solution:
    def solve_n_queens(self, n: int) -> list[list[str]]:
        if not n:
            return []

        board: list[list[str]] = [["." for _ in range(n)] for _ in range(n)]

        result: list[list[str]] = []
        self.dfs(n, 0, board, result)
        return result

    def is_valid(self, board: list[list[str]], row: int, col: int) -> bool:
        # validate col
        for r in range(row, -1, -1):
            if board[r][col] == "Q":
                return False

        # validate up and left
        nr, nc = row - 1, col - 1
        while nc >= 0 and nr >= 0:
            if board[nr][nc] == "Q":
                return False
            nr, nc = nr - 1, nc - 1

        # validate up and right
        nr, nc = row - 1, col + 1
        while nc < len(board[0]) and nr >= 0:
            if board[nr][nc] == "Q":
                return False
            nr, nc = nr - 1, nc + 1

        return True

    def dfs(
        self, n: int, row: int, board: list[list[str]], result: list[list[str]]
    ) -> None:
        if row == len(board):
            result.append(["".join(r) for r in board])
            return

        cols: int = len(board[0])
        for col in range(cols):
            if self.is_valid(board, row, col):
                board[row][col] = "Q"
                self.dfs(n, row + 1, board, result)
                board[row][col] = "."


class TestSolution(unittest.TestCase):
    def test_example1(self):
        actual = Solution().solve_n_queens(4)
        self.assertEqual(
            [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]], actual
        )


if __name__ == "__main__":
    unittest.main()
