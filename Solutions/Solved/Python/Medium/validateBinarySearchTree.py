# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lastLeftParent, lastRightParent):
            if not node:
                return True
            if node.val <= lastRightParent or node.val >= lastLeftParent:
                return False
            leftTree = dfs(node.left, node.val, lastRightParent)
            rightTree = dfs(node.right, lastLeftParent, node.val)
            return rightTree and leftTree
        return dfs(root, float('inf'), -2**31 - 1)
        