class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rows, cols = len(grid), len(grid[0])
        res = 0
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = '0'
            while q:
                qr, qc = q.popleft()
                for dr, dc in directions:
                    R, C = (qr + dr), (qc + dc)
                    if R < 0 or C < 0 or R == rows or C == cols or grid[R][C] == '0': 
                        continue
                    grid[R][C] = '0'
                    q.append((R, C))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r, c)
                    res +=1
        return res