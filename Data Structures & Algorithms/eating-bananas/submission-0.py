class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m  = (l + r) // 2
            count = 0
            for p in piles:
                count += (p + m - 1) // m
            if count <= h:
                res = min(m, res)
                r = m - 1
            else:
                l = m + 1
            print(res)
        return res