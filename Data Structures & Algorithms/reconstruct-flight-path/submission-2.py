class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticketMap = collections.defaultdict(list)
        for src, dst in tickets:
            ticketMap[src].append(dst)
        for src in ticketMap:
            ticketMap[src].sort(reverse= True)
        res = []
        def dfs(src):
            while ticketMap[src]:
                dfs(ticketMap[src].pop())
            res.append(src)
        dfs('JFK')
        return res[::-1]