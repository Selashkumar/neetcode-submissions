class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        pointCostMap = collections.defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                pointCostMap[i].append([dist, j])
                pointCostMap[j].append([dist, i])
        res = 0
        visit = set()
        minHeap = [[0,0]]
        while len(visit) < n:
            cost, point = heapq.heappop(minHeap)
            if point in visit:
                continue
            visit.add(point)
            for neiCost, nei in pointCostMap[point]:
                if nei in visit:
                    continue
                heapq.heappush(minHeap, [neiCost, nei])
            res += cost
        return res