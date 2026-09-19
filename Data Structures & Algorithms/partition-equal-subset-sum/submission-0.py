class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        for i in range(len(nums) - 1, -1, -1):
            tempDp = set()
            for t in dp:
                tempDp.add(t + nums[i])
                tempDp.add(t)
            dp = tempDp
        return True if target in dp else False
