class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for i in range(len(nums)):
            tempDp = defaultdict(int)
            for key, val in dp.items():
                tempDp[key+ nums[i]] += val
                tempDp[key- nums[i]] += val
            dp = tempDp
        return dp[target]


        # dp = {} # (ind, curSum): val
        # def dfs(i, curSum):
        #     if (i, curSum) in dp:
        #         return dp[(i, curSum)]
        #     if i == len(nums):
        #         return 1 if curSum == target else 0
        #     dp[(i, curSum)] = (dfs(i+1, curSum + nums[i]) + dfs(i+1, curSum + nums[i]))
        #     return dp[(i, curSum)]
        # return dfs(0, 0)