class Solution(object):
    def climbStairs(self, n):
        x = 0
        t = 0
        m = {}
        return self.recurse(n, x, m)

    def recurse(self, n, x, m):
        if x > n:
            return 0
        if x == n:
            return 1
        if x in m:
            return m[x]
        m[x] = self.recurse(n, x + 1, m) + self.recurse(n, x + 2, m)
        return m[x]
