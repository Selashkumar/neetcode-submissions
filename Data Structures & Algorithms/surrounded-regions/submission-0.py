class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        land = set()
        allLand = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] == 'X' or (r, c) in land: 
                return
            land.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    allLand.add((r,c))
                if (r == 0 or c == 0 or r == rows -1 or c == cols -1) and board[r][c] == 'O':
                    dfs(r, c)
        for r, c in allLand:
            if (r, c) not in land:
                board[r][c] = 'X'
