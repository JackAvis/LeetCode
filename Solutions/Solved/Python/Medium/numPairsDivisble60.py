class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        durations = {}
        for t in time:
            bucket = t % 60
            if bucket not in durations:
                durations[bucket] = 1
            else:
                durations[bucket] += 1
        pairs = 0
        for songLength in durations:
            songLengthNeeded = 60 - songLength
            if songLength == 30 or songLength == 0:
                    n = durations[songLength]
                    if n > 2:
                        pairs += math.factorial(n)//((2)*math.factorial(n-2))
                    else:
                        pairs += n - 1
            elif songLengthNeeded in durations:
                pairs += durations[songLength] * durations[songLengthNeeded]
                durations[songLength] = 0
        return pairs
        