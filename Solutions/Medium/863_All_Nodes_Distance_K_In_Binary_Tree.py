# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # looked at solution, change the tree into an undirected graph
        graph = collections.defaultdict(list)
        def dfs(root, parentNode):
            nonlocal graph
            if not root:
                return
            # to find distance we can travel from parent to child and child to parent
            if parentNode:
                graph[root.val].append(parentNode.val)
                graph[parentNode.val].append(root.val)
            dfs(root.left, root)
            dfs(root.right, root)
        dfs(root, None)

        # now that it is represented as a graph, we can dfs from the target on the graph
        sol = []
        def dfsGraph(node, visited, curDist):
            nonlocal sol
            if curDist == k:
                sol.append(node)
                return
            if not graph[node]:
                return
            visited.add(node)
            for adjacentNode in graph[node]:
                if adjacentNode not in visited:
                    dfsGraph(adjacentNode, visited, curDist + 1)
        dfsGraph(target.val, set(), 0)
        return sol



