import numpy as np
import pygame
from draw import drawSudoku, putNumbers
from info import FPS, handleKeys

class Sudoku():
    
    def __init__(self, state):
        try:
            self.state = np.array(state).astype('uint8')
        except Exception as e:
            raise Exception('Should only contain numbers')
        if self.state.shape != (9,9):
            raise Exception("Should have shape == (9,9)")
        if (self.state >= 0).all() and (self.state <= 9).all() == False:
            raise Exception('Should only contain numbers between 0-9')
            
        self.starting_state = state.copy()
                
    def check_row(self, row, number):
        return(number in self.state[row])

    def check_col(self, col, number):
        return(number in self.state[:, col])

    def check_square(self, row, col, number):
        row -= row % 3
        col -= col % 3
        for i in range(3):
            for j in range(3):
                if self.state[row+i, col+j] == number:
                    return True
        return False

    def check_available(self, row, col, number):
        if self.check_row(row, number)\
        or self.check_col(col, number)\
        or self.check_square(row, col, number):
            return False
        return True
    
    def get_index(self, row, column):
        return (row * 9) + column

    def get_row_col(self, index):
        return int(index / 9), (index % 9)
    
    def showSudoku(self, settings):
        settings.clock.tick(FPS)
        drawSudoku(settings.surface)
        settings.screen.blit(settings.surface, (0,0))
        putNumbers(settings.screen, self.state, settings.myfont)
        pygame.display.update()

    def __brute_force(self, settings, index):
        # Finished sudoku
        if index > 80:
            return True
        row, col = self.get_row_col(index)
        # If sudoku square is not empty
        if self.state[row, col] != 0:
            return(self.__brute_force(settings, index+1))
        # Show backtracking
        self.showSudoku(settings)
        handleKeys(settings)
        # Try numbers 0-9
        for n in range(1, 10):
            if self.check_available(row, col, n):
                self.state[row, col] = n
                if self.__brute_force(settings, index+1):
                    return True
                self.state[row, col] = 0
        return False

    def solve(self, settings):
        solved = self.__brute_force(settings, 0)
        self.showSudoku(settings)
        return solved
