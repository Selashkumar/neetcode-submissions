class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        obj = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for i in s:
            if i in obj:
                if q and q[-1] == obj[i]:
                    q.pop()
                else:
                    return False
            else:
                q.append(i)
        return len(q) == 0