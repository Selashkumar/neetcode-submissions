class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        col = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [['.'] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for i in range(n):
                if i not in col and (r+i) not in posDiag and (r- i) not in negDiag:
                    board[r][i] = 'Q'
                    col.add(i)
                    posDiag.add(r+i)
                    negDiag.add(r-i)
                    backtrack(r+1)
                    board[r][i] = '.'
                    col.remove(i)
                    posDiag.remove(r+i)
                    negDiag.remove(r-i)
        backtrack(0)
        return res