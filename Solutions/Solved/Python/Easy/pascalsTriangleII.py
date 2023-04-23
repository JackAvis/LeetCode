class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for i in range(rowIndex + 1):
            row = []
            for j in range(i + 1):
                row.append(1)
            triangle.append(row)
        for i in range(rowIndex ):
            for j in range(len(triangle[i])):
                if j + 1 != len(triangle[i]):
                    triangle[i + 1][j + 1] = triangle[i][j] + triangle[i][j + 1]
        return triangle[-1]