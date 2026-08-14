class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        obj ={}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in obj:
                l = max(l, obj[s[r]] + 1)
            obj[s[r]] = r
            res = max(res, (r -l) + 1)
        return res