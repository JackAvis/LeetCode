class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        rocks_to_fill = []
        max_filled = 0
        for i in range(len(capacity)):
            if (capacity[i] - rocks[i]) > 0:
                rocks_to_fill.append(capacity[i] - rocks[i])
            else:
                max_filled += 1
        rocks_to_fill.sort()
        i = 0
        while additionalRocks > 0 and i < len(rocks_to_fill):
            additionalRocks -= rocks_to_fill[i]
            if additionalRocks >=0:
                max_filled += 1
            i += 1
        return max_filled