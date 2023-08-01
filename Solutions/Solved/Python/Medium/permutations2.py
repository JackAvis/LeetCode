class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        freqMap = {}
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1
        uniqueNums = set(nums)
        def dfs(curFreqs, curPermutation):
            if len(curPermutation) == len(nums):
                permutations.append(list(curPermutation))
                return
            for num in uniqueNums:
                if curFreqs[num] > 0:
                    curFreqs[num] -= 1
                    curPermutation.append(num)
                    dfs(curFreqs, curPermutation)
                    curPermutation.pop()
                    curFreqs[num] += 1
        dfs(freqMap, [])
        return permutations
