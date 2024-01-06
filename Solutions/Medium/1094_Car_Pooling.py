class Solution(object):
    def carPooling(self, trips, capacity):
        p = 0
        t = 0
        m = {}
        trips.sort(key=lambda x: x[1])
        for trip in trips:
            while trip[1] != t:
                t += 1
                if t in m:
                    p -= m[t]
            if trip[1] == t:
                p += trip[0]
                if p > capacity:
                    return False
                if trip[2] in m:
                    m[trip[2]] += trip[0]
                else:
                    m[trip[2]] = trip[0]
        return True
