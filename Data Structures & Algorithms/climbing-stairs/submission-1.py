class Solution:
    def climbStairs(self, n: int) -> int:
        # res = 0
        # def dfs(cur):
        #     nonlocal res
        #     if cur == n:
        #         res += 1
        #         return
        #     if cur > n:
        #         return
        #     dfs(cur+1)
        #     dfs(cur+2)
        # dfs(0)
        # return res
        one, two = 1,1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one