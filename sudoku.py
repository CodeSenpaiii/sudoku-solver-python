#   Author  :   CodeSenpaiii

class Solver:

    def __init__(self, sudoku:list):
        self.sudoku = sudoku

    def solve(self):
        while True:
            possibles = {}
            temp = {}
            min = 9
            _row, _pos = None, None

            for index, row in enumerate(self.sudoku):
                for i, r in enumerate(row):    
                    if r == 0:  # Calculating the possible values for blank spots represented with 0
                        row = self.sudoku[index]
                        col = [r[i] for r in self.sudoku]
                        possibilities = list({1, 2, 3, 4, 5, 6, 7, 8, 9} - (set(row) | set(col)))
                        if min > len(possibilities) and possibilities:
                            min = len(possibilities)
                            _row, _pos = index, i
                        temp[i] = possibilities
                possibles[index] = temp.copy()
                temp.clear()

            if _row or _pos:
                self.sudoku[_row][_pos] = possibles[_row][_pos][0]
            else:
                return self.sudoku
                
