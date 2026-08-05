class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and nums[i-1] == n:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                tot = nums[i] + nums[left] + nums[right]
                if tot < 0:
                    left +=1
                elif tot > 0:
                    right -=1
                else:
                    ans.append([n , nums[left] ,nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
        return ans























        # ans = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 ans.add(tuple([nums[i], nums[j], nums[k]]))
        # return [list(i) for i in ans]