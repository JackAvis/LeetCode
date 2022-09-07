# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sol: str = ""
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root.right is None and root.left is None:
            self.sol+= f"{str(root.val)}"
            return self.sol
        if root.right is None:
            self.sol += str(root.val)
            self.sol += "("
            self.tree2str(root.left)
            self.sol += ")"
            return self.sol
        if root.left is None:
            self.sol += str(root.val)
            self.sol += "()("
            self.tree2str(root.right)
            self.sol += ")"
            return self.sol
        self.sol += str(root.val) + "("
        self.tree2str(root.left)
        self.sol += ")("
        self.tree2str(root.right)
        self.sol += ")"
        return self.sol
        
        