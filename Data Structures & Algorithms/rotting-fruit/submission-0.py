class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        freshOrenges = 0            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    freshOrenges +=1
        count = 0
        while q and freshOrenges > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    r, c = row + dr, col + dc
                    if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] != 1:
                        continue
                    q.append([r, c])
                    grid[r][c] = 2
                    freshOrenges -= 1
            count += 1
        return count if freshOrenges == 0 else -1