class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = {}
        return self.paths(obstacleGrid, 0, 0, m)

    def paths(self, obstacleGrid, row, col, m):
        if row == len(obstacleGrid):
            return 0
        if col == len(obstacleGrid[row]):
            return 0
        if obstacleGrid[row][col] == 1:
            return 0
        if row == len(obstacleGrid) - 1 and col == len(obstacleGrid[row]) - 1:
            return 1
        if (row, col) in m:
            return m[row, col]
        m[row, col] = self.paths(
            obstacleGrid, row + 1, col, m) + self.paths(obstacleGrid, row, col + 1, m)
        return m[row, col]
