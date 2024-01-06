class Solution(object):
    def minDeletionSize(self, strs):
        colRemoved = 0
        for col in range(len(strs[0])):
            for row in range(len(strs)):
                if row < len(strs) - 1:
                    if ord(strs[row][col]) > ord(strs[row + 1][col]):                        
                        colRemoved += 1
                        break
        return colRemoved