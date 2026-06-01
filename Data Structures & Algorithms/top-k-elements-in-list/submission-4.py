class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        obj = {}
        for i in range(len(nums)):
            obj[nums[i]] = 1 + obj.get(nums[i],0)
        ans= []
        for num, count in obj.items():
            ans.append([count, num])
        ans.sort()
        res = []
        while len(res) < k:
            res.append(ans.pop()[1])
        return res






















        # obj = {}
        # for i in range(len(nums)):
        #     obj[nums[i]] = 1 + obj.get(nums[i], 0)
        # ans = []
        # for num, count in obj.items():
        #     ans.append([count, num])
        # ans.sort()
        # res = []
        # while len(res) < k:
        #     res.append(ans.pop()[1])
        # return res