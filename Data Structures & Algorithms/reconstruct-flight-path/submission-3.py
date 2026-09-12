class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticketMap = collections.defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            ticketMap[src].append(dst)
        res = []
        def dfs(src):
            while ticketMap[src]:
                dfs(ticketMap[src].pop())
            res.append(src)
        dfs('JFK')
        return res[::-1]