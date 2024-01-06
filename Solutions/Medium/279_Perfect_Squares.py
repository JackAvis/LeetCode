class Solution(object):
    def numSquares(self, n):
        validSquares = []
        i = 1
        square = 1
        while square <= n:
            validSquares.append(square)
            i += 1
            square = i * i
        # curSum = numSquares
        dpArray = []
        for _ in range(n + 1):
            dpArray.append(0)
        for curSum in range(len(dpArray)):
            for square in validSquares:
                if curSum + square <= n:
                    if dpArray[curSum + square] == 0:
                        dpArray[curSum + square] = dpArray[curSum] + 1
                    else: 
                        dpArray[curSum + square] = min(dpArray[curSum] + 1, dpArray[curSum + square])
        return dpArray[n]


        