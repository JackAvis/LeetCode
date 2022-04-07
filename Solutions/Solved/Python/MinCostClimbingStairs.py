class Solution(object):
    def minCostClimbingStairs(self, cost):
        # dp =  minimum cost necessary to reach step i 
        # We can arrive to i from either step i-1 or i-2
        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return 0
            if i not in memo:
                memo[i] = min(dp(i-1) + cost[i - 1], dp(i - 2) + cost[i - 2])
            return memo[i]
        memo = {}
        return dp(len(cost))