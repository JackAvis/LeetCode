class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        def dfs(curNum, curCombination):
            if len(curCombination) == k:
                combinations.append(list(curCombination))
                return
            for i in range(curNum + 1, n + 1):
                curCombination.append(i)
                dfs(i, curCombination)
                curCombination.pop()
        dfs(0, [])
        return combinations