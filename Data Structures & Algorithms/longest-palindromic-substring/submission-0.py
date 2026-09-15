class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.resInd = 0
        self.resLen = 0
        def pali(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > self.resLen:
                    self.resLen = r - l + 1
                    self.resInd = l
                l -=1
                r += 1
        for i in range(len(s)):
            pali(i,i)
            pali(i, i+1)
        return s[self.resInd: self.resInd + self.resLen]