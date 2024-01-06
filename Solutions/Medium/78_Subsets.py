class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        def backtrack(index, subset):
            sol.append(list(subset))
            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        backtrack(0, [])
        return sol

