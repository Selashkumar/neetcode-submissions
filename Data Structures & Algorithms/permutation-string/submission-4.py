class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        arr1, arr2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            arr1[ord(s1[i]) - ord('a')] +=1
            arr2[ord(s2[i]) - ord('a')] +=1
        matches = 0
        for i in range(26):
            matches +=(1 if arr1[i] == arr2[i] else 0)
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26: return True
            index = ord(s2[r]) - ord('a')
            arr2[index] +=1
            if arr2[index] == arr1[index]:
                matches +=1
            elif arr1[index] + 1 == arr2[index]:
                matches -= 1
            index = ord(s2[l]) - ord('a')
            arr2[index] -=1
            if arr2[index] == arr1[index]:
                matches +=1
            elif arr1[index] - 1 == arr2[index]:
                matches -= 1
            l +=1
        return matches == 26