class Solution(object):
    def getMaximumGenerated(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(1, n + 1):
            if dp[n] != 0:
                return max(dp)
            dp[2 * i] = dp[i]
            if dp[n] != 0:
                return max(dp)
            dp[2 * i + 1] = dp[i] + dp[i + 1]
        



        