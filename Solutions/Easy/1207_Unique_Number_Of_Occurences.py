class Solution(object):
    def uniqueOccurrences(self, arr):
        o = {}
        for num in arr:
            if num not in o:
                o[num] = 1
            else:
                o[num] += 1
        o_set = set()
        for num in o:
            if o[num] in o_set:
                return False
            else:
                o_set.add(o[num])
        return True