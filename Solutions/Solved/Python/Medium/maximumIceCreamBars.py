class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        runningTotal = 0
        bars = 0
        for i in range(len(costs)):
            runningTotal += costs[i]
            if runningTotal > coins:
                return bars
            bars += 1
        return bars