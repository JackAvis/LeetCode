class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # terminal -> [] at node index
        # sage node -> all paths starting from their node lead to terminal
        # plan: dfs on each node to find if safe and store in map
        safeNodes = []
        safeMap = {}
        def dfs(index, visited):
            nonlocal safeMap
            nonlocal safeNodes
            if index in safeMap:
                return safeMap[index]
            if index in visited:
                return False
            if not graph[index]:
                return True
            isSafe = True
            visited.add(index)
            for node in graph[index]:
                safeMap[node] = dfs(node, visited)
                isSafe = safeMap[node] and isSafe
            visited.remove(index)
            return isSafe
        for i in range(len(graph)):
            safeMap[i] = dfs(i, set())
            if safeMap[i]:
                safeNodes.append(i)
        return safeNodes
