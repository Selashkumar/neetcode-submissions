class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        stack.append([0, heights[0]])
        for i in range(1,len(heights)):
            ind = i
            while stack and stack[-1][1] > heights[i]:
                ind, h = stack.pop()
                res = max(res,(i - ind) * h)
            stack.append([ind,heights[i]])
        # print(stack)
        for i, h in stack:
            res = max((len(heights) - i) * h, res)
        return res