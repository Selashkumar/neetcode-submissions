class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = {}
        dirArr = [(-1,0),(1,0),(0,-1),(0, 1)]
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] =1
            for di,dj in dirArr:
                r,c = i+di, j+dj
                if r >= 0 and r < rows and c >= 0 and c < cols and matrix[i][j] < matrix[r][c]:
                    dp[(i,j)] = max(dp[(i,j)], 1+ dfs(r,c))
            return dp[(i,j)]
        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i,j))
        return res