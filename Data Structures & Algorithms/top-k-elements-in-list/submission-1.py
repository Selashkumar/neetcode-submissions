class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        obj = {}
        for i in nums:
            obj[i] = 1 + obj.get(i, 0)
        fArr = []
        for num ,count in obj.items():
            fArr.append([count, num])
        fArr.sort()
        res = []
        while len(res) < k:
            res.append(fArr.pop()[1])
        return res