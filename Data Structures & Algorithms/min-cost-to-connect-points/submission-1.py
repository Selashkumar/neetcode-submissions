class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        visit = set()
        minHeap = [[0,0]]
        while len(visit) < n:
            cost, point = heapq.heappop(minHeap)
            if point in visit:
                continue
            visit.add(point)
            res += cost
            x1, y1 = points[point]
            for j in range(n):
                if j in visit:
                    continue
                x2, y2 = points[j]
                heapq.heappush(minHeap, [abs(x1 - x2) + abs(y1 - y2), j])
            
        return res