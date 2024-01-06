class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        memo = {}
        def dfs(row, col, curMoveCount):
            nonlocal memo
            # out of bounds
            if (row, col, curMoveCount) in memo:
                return memo[(row, col, curMoveCount)]
            if row < 0 or col < 0 or row > n - 1 or col > n - 1:
                return 0
            if curMoveCount == k:
                return 1
            memo[(row, col, curMoveCount)] =  dfs(row - 2, col - 1, curMoveCount + 1) + dfs(row - 1, col - 2, curMoveCount + 1) + dfs(row - 2, col + 1, curMoveCount + 1) + dfs(row - 1, col + 2, curMoveCount + 1) + dfs(row + 1, col + 2, curMoveCount + 1) + dfs(row + 2, col + 1, curMoveCount + 1) + dfs(row + 2, col - 1, curMoveCount + 1) + dfs(row + 1, col - 2, curMoveCount + 1)
            return memo[(row, col, curMoveCount)]
        return dfs(row, column, 0) / 8**k


