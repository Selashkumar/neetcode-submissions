class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = 1
        for i in range(len(nums)-2, -1, -1):
            if step <= nums[i]:
                step = 1
            else:
                step += 1
        return step == 1
