class Solution(object):
    def minFallingPathSum(self, matrix):
        checker = 0
        o = 99999
        h = {}
        for i in range(len(matrix)):
            checker = self.minsum(matrix, 0, i, h)
            if checker < o:
                o = checker
        return o

    def minsum(self, matrix, row, col, h):
        if row == len(matrix) or row == -1:
            return 99999  # infinity
        if col == len(matrix[row]) or col == -1:
            return 99999  # infinity
        if (row, col) in h:
            return h[row, col]
        if row == len(matrix) - 1:
            return matrix[row][col]
        if (row, col) in h:
            return h[row, col]
        h[row, col] = matrix[row][col] + min(self.minsum(matrix, row + 1, col - 1, h), self.minsum(
            matrix, row + 1, col + 1, h), self.minsum(matrix, row + 1, col, h))
        return h[row, col]
