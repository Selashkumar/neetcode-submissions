class Solution:
    def rob(self, nums: List[int]) -> int:
        def giveMoney(houses):
            rob1, rob2 = 0,0
            for hou in houses:
                temp = max(hou + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(nums[0], giveMoney(nums[1:]),giveMoney(nums[:-1]))