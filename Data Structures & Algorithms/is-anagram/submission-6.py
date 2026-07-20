class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        objs, objt ={},{}
        for i in range(len(t)):
            objs[s[i]] = 1 + objs.get(s[i],0)
            objt[t[i]] = 1 + objt.get(t[i],0)
        return objs == objt