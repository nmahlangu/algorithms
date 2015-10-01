from sets import Set

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board:
            return False
        valid = set([str(n+1) for n in xrange(9)])
        for i in xrange(len(board)):
            row_seen = set()
            for j in xrange(len(board[i])):
                n = board[i][j]
                if n in valid:
                    if n not in row_seen:
                        row_seen.add(n)
                    else:
                        return False
        for i in xrange(len(board[0])):
            col_seen = set()
            for j in xrange(len(board)):
                n = board[j][i]
                if n in valid:
                    if n not in col_seen:
                        col_seen.add(n)
                    else:
                        return False
        return True

arr = ["....5..1.",
     ".4.3.....",
     ".....3..1",
     "8......2.",
     "..2.7....",
     ".15......",
     ".....2...",
     ".2.9.....",
     "..4......"]
print Solution().isValidSudoku(arr)
