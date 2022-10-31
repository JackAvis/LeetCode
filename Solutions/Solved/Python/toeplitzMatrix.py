class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if (row, col) in m:
                    if m[(row, col)] != matrix[row][col]:
                        return False
                m[(row + 1, col + 1)] = matrix[row][col]
        return True
        