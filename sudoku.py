#   Author  :   CodeSenpaiii

class Solver:

    def __init__(self, sudoku:list):
        self.sudoku = sudoku
        self.solved = sudoku

    def is_solved(self):
        for row in self.sudoku:
            if 0 in row:
                return False
        return True
    
    def possibles(self):
        possibles = {}
        temp = {}
        min = 9
        _row, _pos = None, None

        for index, row in enumerate(self.solved):
            for i, r in enumerate(row):    
                if r == 0:  # Calculating the possible values for blank spots represented with 0
                    row = self.solved[index]
                    col = [r[i] for r in self.solved]
                    possibilities = list({1, 2, 3, 4, 5, 6, 7, 8, 9} - (set(row) | set(col)))
                    if min > len(possibilities) and possibilities:
                        min = len(possibilities)
                        _row, _pos = index, i
                    temp[i] = possibilities
            possibles[index] = temp.copy()
            temp.clear()

        if _row or _pos:
            self.solved[_row][_pos] = possibles[_row][_pos][0]
        else:
            return None

    def solve(self):
        while not self.is_solved():
            if not self.possibles():
                break
        
        return self.solved