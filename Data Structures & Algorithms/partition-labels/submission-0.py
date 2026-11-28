class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, v in enumerate(s):
            lastIndex[v] = i
        res = []
        start = 0
        end = 0
        for i, v in enumerate(s):
            start +=1
            end = max(end, lastIndex[v])
            if i == end:
                res.append(start)
                start = 0
        return res