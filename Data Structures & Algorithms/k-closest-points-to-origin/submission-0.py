class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[(p1*p1) + (p2*p2), p1, p2 ] for p1, p2 in points]
        heapq.heapify(points)
        res = []
        while k:
            k -=1
            dist, x, y = heapq.heappop(points)
            res.append([x, y])
        return res