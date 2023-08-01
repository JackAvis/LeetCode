class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexMap = {}
        for i in range(len(nums)):
            if nums[i] not in indexMap:
                indexMap[nums[i]] = [i]
            else:
                indexMap[nums[i]].append(i)
        for key in indexMap:
            indicies = indexMap[key]
            for i in range(len(indicies) - 1):
                leftElement = indicies[i]
                rightElement = indicies[i + 1]
                if abs(rightElement - leftElement) <= k:
                    return True
        return False

