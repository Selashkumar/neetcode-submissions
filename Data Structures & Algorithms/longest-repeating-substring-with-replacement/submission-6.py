class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        obj = {}
        maxL = 0
        res = 0
        for r in range(len(s)):
            obj[s[r]] = 1 + obj.get(s[r], 0)
            maxL = max(maxL, obj[s[r]])
            while (((r - l) + 1) - maxL) > k:
                obj[s[l]] -=1
                l +=1
            res = max(res, r - l + 1)
        return res