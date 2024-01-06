class Solution(object):
    def transpose(self, matrix):
        solution = []
        for column in range(len(matrix[0])):
            temp = []
            for element in range(len(matrix)):
                temp.append(matrix[element][column])
            solution.append(temp)
        return solution
