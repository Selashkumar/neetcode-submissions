class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        stack = []
        for i in range(n+1):
            ind = i
            while stack and (i == n or (stack[-1][1] >= heights[i])):
                ind, h = stack.pop()
                res = max(res,(i - ind) * h)
            if i < n:
                stack.append([ind,heights[i]])
        return res