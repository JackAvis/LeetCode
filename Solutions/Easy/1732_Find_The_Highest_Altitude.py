class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude = 0
        runningAltitude = 0
        for i in range(1, len(gain) + 1):
            runningAltitude += gain[i - 1]
            maxAltitude = max(maxAltitude, runningAltitude)
        return maxAltitude
            