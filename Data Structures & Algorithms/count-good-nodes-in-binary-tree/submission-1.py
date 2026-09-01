# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def numOfGoodNodes(curr, maxRootVal):
            if not curr: return 0
            res = 1 if curr.val >= maxRootVal else 0
            maxVal = max(curr.val, maxRootVal)
            res += numOfGoodNodes(curr.left, maxVal)
            res += numOfGoodNodes(curr.right, maxVal)
            return res
        return numOfGoodNodes(root, root.val)