class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxRes = 0
        while l < r:
            if heights[l] < heights[r]:
                maxRes = max(maxRes, (r-l) * heights[l])
                l += 1
            else:
                maxRes = max(maxRes, (r-l) * heights[r])
                r -=1
        return maxRes