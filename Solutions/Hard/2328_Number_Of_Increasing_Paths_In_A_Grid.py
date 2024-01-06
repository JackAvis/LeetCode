class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # dp problem 
        numIncreasing = 0
        memo = {}
        def dfs(row, col, prev):
            nonlocal memo
            if row < 0 or row  > len(grid) - 1:
                return 0
            if col < 0 or col > len(grid[row]) - 1:
                return 0
            currentValue = grid[row][col]
            if prev >= currentValue:
                return 0
            if (row, col) in memo:
                return memo[(row, col)]
            increasingPaths = 0
            # up
            up = dfs(row - 1, col, currentValue) 
            # down
            down = dfs(row + 1, col, currentValue) 
            # left
            left = dfs(row, col - 1, currentValue) 
            # right
            right = dfs(row, col + 1, currentValue) 
            increasingPaths += up + down + left + right + 1
            memo[(row, col)] = increasingPaths
            return increasingPaths
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                numIncreasing += dfs(r, c, 0)
        return numIncreasing % (10**9 + 7)