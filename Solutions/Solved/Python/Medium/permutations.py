class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def dfs(permSet, curPermutation):
            if len(curPermutation) == len(nums):
                permutations.append(list(curPermutation))
                return
            for i in range(len(nums)):
                if nums[i] not in permSet:
                    permSet.add(nums[i])
                    curPermutation.append(nums[i])
                    dfs(permSet, curPermutation)
                    curPermutation.pop()
                    permSet.remove(nums[i])
        dfs(set(), [])
        return permutations