class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        islands = []
        def getIslands(row, col):
            if row < 0 or row > len(grid) - 1:
                return False
            if col < 0 or col > len(grid[0]) - 1:
                return False
            if grid[row][col] == 1 or grid[row][col] == -1:
                return True
            grid[row][col] = -1
            up = getIslands(row-1, col)
            down = getIslands(row+1, col)
            left = getIslands(row, col-1)
            right = getIslands(row, col+1)
            return up and down and left and right
        numClosedIslands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    if getIslands(row, col):
                        numClosedIslands += 1
        return numClosedIslands