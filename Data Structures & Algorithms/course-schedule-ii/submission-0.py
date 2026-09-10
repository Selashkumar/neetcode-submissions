class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = {i: [] for i in range(numCourses)}
        for pre, val in prerequisites:
            courseMap[pre].append(val)
        visit = set()
        cycle = set()
        res = []
        def dfs(cur):
            if cur in cycle:
                return False
            if cur in visit:
                return True
            cycle.add(cur)
            for c in courseMap[cur]:
                if not dfs(c):
                    return False
            visit.add(cur)
            cycle.remove(cur)
            res.append(cur)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
