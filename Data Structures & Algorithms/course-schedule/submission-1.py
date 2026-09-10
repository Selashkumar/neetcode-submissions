class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = { i:[] for i in range(numCourses)}
        visit = set()
        for pre in prerequisites:
            courseMap[pre[0]].append(pre[1])

        def dfs(cou):
            if cou in visit:
                return False
            if courseMap[cou] == []:
                return True
            visit.add(cou)
            for c in courseMap[cou]:
                if not dfs(c): return False
            visit.remove(cou)
            courseMap[cou] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True