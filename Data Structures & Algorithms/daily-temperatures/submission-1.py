class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        index = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1] < temp:
                stack.pop()
                j = index.pop()
                res[j] = i - j
            stack.append(temp)
            index.append(i)
        return res
