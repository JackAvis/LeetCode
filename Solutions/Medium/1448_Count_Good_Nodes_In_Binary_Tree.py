# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    goodNodeCount = 0
    def goodNodes(self, root: TreeNode) -> int:
        self.recurse(root, float('-inf'))
        return self.goodNodeCount
        
    def recurse(self, root, maxVal):
        if not root:
            return
        if not root.left and not root.right:
            if maxVal <= root.val:
                self.goodNodeCount += 1
            return 
        if maxVal <= root.val:
            self.goodNodeCount += 1
        maxVal = max(maxVal, root.val)
        self.recurse(root.left, maxVal)
        self.recurse(root.right, maxVal)