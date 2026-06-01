class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j +=1
            count = int(s[i:j])
            i = j+1
            j = i + count
            ans.append(s[i:j])
            i = j
        return ans