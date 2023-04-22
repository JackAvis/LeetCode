class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dfs(i, j):
            nonlocal memo
            if j < 0 or j >= len(triangle[i]):
                return 10**6
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(triangle) - 1:
                return triangle[i][j]
            memo[(i, j)] = min(dfs(i + 1, j + 1) + triangle[i][j], dfs(i + 1, j) + + triangle[i][j])
            return memo[(i, j)]
        return dfs(0, 0)

            
            