class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minHeap = [[grid[0][0], 0, 0]]
        visit.add((0, 0))
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        while minHeap:
            time, x1, y1 = heapq.heappop(minHeap)
            if x1 == n-1 and y1 == n-1:
                return time
            for dx, dy in directions:
                x2, y2 = x1 + dx, y1 + dy
                if x2 < 0 or y2 < 0 or x2 == n or y2 == n or (x2, y2) in visit:
                    continue
                visit.add((x2,y2))
                heapq.heappush(minHeap,[max(time, grid[x2][y2]), x2, y2])