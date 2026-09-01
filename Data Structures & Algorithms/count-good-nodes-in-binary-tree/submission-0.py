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
            if curr.val >= maxRootVal:
                return (1 + numOfGoodNodes(curr.left, curr.val) + numOfGoodNodes(curr.right, curr.val))
            return numOfGoodNodes(curr.left, maxRootVal) + numOfGoodNodes(curr.right, maxRootVal)
        if not root: return 0
        return 1 + numOfGoodNodes(root.left, root.val) + numOfGoodNodes(root.right, root.val)