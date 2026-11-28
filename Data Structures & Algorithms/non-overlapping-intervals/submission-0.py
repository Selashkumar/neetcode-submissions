class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        curEnd = intervals[0][1]
        res =0
        for i in intervals[1:]:
            if curEnd > i[0]:
                curEnd = min(curEnd,i[1])
                res +=1
            else:
                curEnd = i[1]
        return res