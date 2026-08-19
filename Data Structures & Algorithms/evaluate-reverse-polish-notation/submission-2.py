class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                val = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(val))

            elif tokens[i] == '-':
                val = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(val))
            elif tokens[i] == '*':
                val = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(val))
            elif tokens[i] == '/':
                val = stack[-2] / stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(val))
            else:
                stack.append(int(tokens[i]))
        return stack[-1] if stack else 0