class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        temp = 1
        maxnum = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == (nums[i - 1] + 1):
                temp+=1
            else:
                maxnum = max(maxnum, temp)
                temp = 1
        return max(maxnum, temp)