class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i in range(len(heights)+1):
            ind = i
            while stack and (i == len(heights) or (stack[-1][1] > heights[i])):
                ind, h = stack.pop()
                res = max(res,(i - ind) * h)
            if i < len(heights):
                stack.append([ind,heights[i]])
        # print(stack)
        # for i, h in stack:
        #     res = max((len(heights) - i) * h, res)
        return res