import numpy as np

class Sudoku:
    def __init__(self):
        self.puzzle = np.full((9, 9), ' ', dtype=str)

    def __str__(self):
        return str(self.puzzle)

    def get(self, coords):
        if self.puzzle[coords[1], coords[0]] == ' ':
            return 0
        return self.puzzle[coords[1], coords[0]]

    def set(self, item, coords):
        self.puzzle[coords[1], coords[0]] = item