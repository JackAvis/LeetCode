class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 2 binary searches
        # row wise
        left = 0
        right = len(matrix)
        while left < right:
            mid = left + (right - left) // 2
            # min k such that condition is true
            # smallest num <= target
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid
            else:
                left = mid + 1
        targetRow = left - 1
        # on cols
        left = 0
        right = len(matrix[targetRow])
        while left < right:
            mid = left + (right - left) // 2
            # min k such that condition is true
            # smallest num <= target
            if matrix[targetRow][mid] == target:
                return True
            if matrix[targetRow][mid] > target:
                right = mid
            else:
                left = mid + 1
        return False