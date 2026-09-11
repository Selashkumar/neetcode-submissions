class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        par = [i for i in range(n)]
        rank = [1] * n
        def find(n1):
            ans = n1
            while ans != par[ans]:
                par[ans] = par[par[ans]]
                ans = par[ans]
            return ans
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return True
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return False
        for n1, n2 in edges:
            if union(n1, n2):
                return [n1, n2]