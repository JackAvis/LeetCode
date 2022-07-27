# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        sol = []
        comb = ""
        self.recurse(root, comb, sol)
        return sol
        
    def recurse(self, root, comb, sol):
        if root == None:
            return
        if root.left == None and root.right == None:
            sol.append(comb + str(root.val))
            return
        comb += str(root.val) + '->'
        self.recurse(root.left, comb, sol)
        self.recurse(root.right, comb, sol)
        
        
        
        
        