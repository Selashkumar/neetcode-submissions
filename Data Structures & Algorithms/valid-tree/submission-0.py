class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap ={i:[] for i in range(n)}
        for key, val in edges:
            edgeMap[key].append(val)
            edgeMap[val].append(key)
        visit = set()
        def dfs(cur, par):
            if cur in visit:
                return False
            visit.add(cur)
            for i in edgeMap[cur]:
                if i == par:
                    continue
                if not dfs(i,cur):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n