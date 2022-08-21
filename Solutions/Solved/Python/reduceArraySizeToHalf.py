class Solution(object):
    def minSetSize(self, arr):
        frequencyMap = {}
        for num in arr:
            if num not in frequencyMap:
                frequencyMap[num] = 1
            else:
                frequencyMap[num] += 1
                
        a = []
        for num in frequencyMap:
            a.append(frequencyMap[num])
        a.sort()
        a.reverse()
        size = 0
        total = 0
        while total < (len(arr) // 2):
            total += a[size]
            size += 1
        return size
        
        