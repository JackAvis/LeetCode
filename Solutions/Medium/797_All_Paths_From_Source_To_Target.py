class Solution(object):
    def allPathsSourceTarget(self, graph):
        target = len(graph) - 1
        sol = []
        path = [0]
        self.backtrack(graph, path, 0, sol)
        return sol
        
    def backtrack(self, graph, path, i, sol):
        if i == len(graph) - 1:
            sol.append(list(path))
            return
        
        for connection in graph[i]:
            path.append(connection) 
            self.backtrack(graph, path, connection, sol)
            path.pop()
            
        
            