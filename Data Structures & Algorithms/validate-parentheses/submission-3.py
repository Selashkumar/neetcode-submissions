class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':  return False
        q = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                q.append(s[i])
            else:
                if q and (
                       (s[i] == ')' and q[-1] == '(')
                    or (s[i] == '}' and q[-1] == '{') 
                    or (s[i] == ']' and q[-1] == '[')
                    ):
                    q.pop()
                else:
                    return False
        return len(q) == 0