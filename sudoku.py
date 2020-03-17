import numpy as np

class Sudoku:
    def __init__(self):
        self.puzzle = np.full((9, 9), ' ', dtype=str)

    def __str__(self):
        horizontal_line = "+---+---+---+---+---+---+---+---+---+"
        horizontal_lineless = "+ - + - + - + - + - + - + - + - + - +"
        sudoku_board = ""

        for a in range(9):
            if a % 3 == 0:
                sudoku_board += horizontal_line + "\n"
            else:
                sudoku_board += horizontal_lineless + "\n"
            for b in range(9):
                sudoku_board += f"| {self.puzzle[a, b]} "
            sudoku_board += "|\n"
        sudoku_board += horizontal_line

        return sudoku_board

    def get(self, coords):
        if self.puzzle[coords[1], coords[0]] == ' ':
            return 0
        return self.puzzle[coords[1], coords[0]]

    def set(self, item, coords):
        self.puzzle[coords[1], coords[0]] = item