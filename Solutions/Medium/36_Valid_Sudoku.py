class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    # take a modular approach 
    # each rule at a time 
        # each row must containdigits 1-9 without repetition 
        for row in range(len(board)):
            rowVals = set()
            for col in range(len(board)):
                cell = board[row][col]
                # repeated value in row
                if cell in rowVals and cell != '.':
                    return False
                rowVals.add(cell)

        # each column must contain digits 1-9 without repetition
        for row in range(9):
            cellVals = set()
            for col in range(9):
                cell = board[col][row]
                # repeated value in col
                if cell in cellVals and cell != '.':
                    return False
                cellVals.add(cell)
    
        # each of the 9 3x3 sub boxes must contain 1-9 without repetition
        boxes = []
        boxCol = 0
        while boxCol < 3:
            box = set()
            for i in range(9):
                if i % 3 == 0:
                    box = set()
                for j in range(boxCol * 3, (boxCol + 1) * 3):
                    cell = board[i][j]
                    # if there is a duplicate in a 3x3 box
                    if cell in box and cell != '.':
                        return False
                    box.add(board[i][j])
                # add a box every 3 rows
                if i % 3 == 0:
                    boxes.append(box)
            boxCol += 1
        return True
