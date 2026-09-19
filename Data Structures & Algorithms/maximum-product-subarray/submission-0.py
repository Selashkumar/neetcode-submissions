class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1,1
        for num in nums:
            temp = curMax
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(num * temp, num * curMin, num)
            res = max(res, curMax, curMin)
        return res