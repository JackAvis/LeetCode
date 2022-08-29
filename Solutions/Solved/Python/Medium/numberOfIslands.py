class Solution(object):
    def numIslands(self, grid):
        m = set()
        numIslands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in m:
                    self.dfs(grid, m, (row, col))
                    numIslands += 1
        return numIslands
        
        
    def dfs(self, grid, m, cell):
        row = cell[0]
        col = cell[1]
        if row >= len(grid) or row < 0:
            return
        if col >= len(grid[0]) or col < 0:
            return
        m.add(cell)
        if row > 0:
            if grid[row - 1][col] == "1" and (row - 1, col) not in m:
                self.dfs(grid, m, (row-1, col))
        if col > 0:
            if grid[row][col - 1] == "1" and (row, col - 1) not in m:
                self.dfs(grid, m, (row, col-1))
        if row <= len(grid) - 2:
            if grid[row + 1][col] == "1" and (row + 1, col) not in m:
                self.dfs(grid, m, (row+1, col))
        if col <= len(grid[0]) - 2:
            if grid[row][col + 1] == "1" and (row, col + 1) not in m:
                self.dfs(grid, m, (row, col + 1))
        return 
            
    # (O(m * n))