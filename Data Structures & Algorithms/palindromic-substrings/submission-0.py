class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res = 0
        def pali(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.res += 1
                l -=1
                r +=1
        for i in range(len(s)):
            pali(i,i)
            pali(i,i+1)
        return self.res