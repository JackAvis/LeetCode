class Solution:
    def maxAncestorDiff(self, root) -> int:
        sol = 0
        def recurse(root, curMin, curMax):
            nonlocal sol
            if root == None:
                return
            curMax = max(curMax, root.val)
            curMin = min(curMin, root.val)
            if curMax != -1 and curMin != float('inf'):
                diff = max(abs(root.val - curMin), abs(root.val - curMax))
                sol = max(sol, diff)
            recurse(root.right, curMin, curMax)
            recurse(root.left, curMin, curMax)
        recurse(root, float('inf'), -1)
        return sol