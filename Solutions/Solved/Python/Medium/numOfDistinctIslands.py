class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = 0
        islandSet = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    moves = []
                    counter = [0]
                    self.dfs(grid, (i, j), moves, "", counter)
                    islandSet.add(''.join(moves))
                    islands += 1
        return len(islandSet)
        
        
        
    def dfs(self, grid, pos, moves, move, counter):
        if pos[0] >= len(grid):
            return 
        if pos[1] >= len(grid[0]):
            return
        if pos[1] < 0:
            return
        if pos[0] < 0:
            return
        if grid[pos[0]][pos[1]] == 0:
            return
        grid[pos[0]][pos[1]] = 0
        moves.append(move)
        self.dfs(grid, (pos[0] + 1, pos[1]), moves, 'd', counter)
        self.dfs(grid, (pos[0], pos[1] + 1), moves, 'r', counter)
        self.dfs(grid, (pos[0] - 1, pos[1]), moves, 'u', counter)
        self.dfs(grid, (pos[0], pos[1] - 1), moves, 'l', counter)
        moves.append("0")

        
            