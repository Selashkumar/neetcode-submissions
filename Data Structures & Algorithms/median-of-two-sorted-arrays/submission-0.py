class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        tot = len(a) + len(b)
        half = tot // 2
        if len(a) > len(b):
            a, b = b, a
        l, r = 0, len(a) - 1
        while True:
            m = (l + r) // 2
            point = half - m - 2
            aLeft = a[m] if m >= 0 else float("-inf")
            aRight = a[m + 1] if m + 1 < len(a) else float('inf')
            bLeft = b[point] if point >= 0 else float('-inf')
            bRight = b[point + 1] if point + 1 < len(b) else float('inf')
            
            if aLeft <= bRight and bLeft <= aRight:
                return (max(bLeft, aLeft) + min(bRight, aRight)) / 2 if tot % 2 == 0 else min(bRight, aRight)
            elif aLeft > bRight:
                r = m - 1
            else:
                l = m + 1