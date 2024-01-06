class Solution(object):
    def minPathSum(self, grid):
        d = []
        dp = []
        for i in range(len(grid[0]) + 1):
            d.append(0)
        for i in range(len(grid)):
            dp.append(list(d))
        
        for row in range(len(dp)):
            for cell in range(1, len(dp[0])):
                if row == 0:
                    dp[row][cell] = dp[row][cell - 1] + grid[row][cell - 1]
                    continue
                if cell == 1:
                    dp[row][cell] = dp[row - 1][cell] + grid[row][cell - 1]
                    continue
                dp[row][cell] = min(dp[row - 1][cell], dp[row][cell - 1]) + grid[row][cell - 1]
        return dp[len(dp) - 1][len(dp[0]) - 1]