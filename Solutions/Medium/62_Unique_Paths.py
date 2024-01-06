class Solution(object):
    def uniquePaths(self, m, n):
        x = 1
        y = 1
        h = {}
        return self.paths(x, y, m, n, h)

    def paths(self, x, y, m, n, h):
        if x == m and y == n:
            return 1
        if x > m or y > n:
            return 0
        if (x, y) in h:
            return h[x, y]
        h[x, y] = self.paths(x + 1, y, m, n, h) + self.paths(x, y+1, m, n, h)
        return h[x, y]
