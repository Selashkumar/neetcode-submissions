class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        val = 0
        for n in nums:
            if val < 0:
                val = 0
            val += n
            res = max(res, val)
        return res