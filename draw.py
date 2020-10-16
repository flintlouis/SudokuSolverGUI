import pygame
from info import GRIDSIZE, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, GRID_WIDTH, GRID_HEIGHT

def drawSudoku(surface):
	surface.fill(WHITE)
	for i in range(int(GRID_WIDTH)):
		if i % 3:
			pygame.draw.line(surface, BLACK, (i*GRIDSIZE, 0), (i*GRIDSIZE, SCREEN_HEIGHT))
		else:
			pygame.draw.line(surface, BLACK, (i*GRIDSIZE, 0), (i*GRIDSIZE, SCREEN_HEIGHT), 5)
		for j in range(int(GRID_HEIGHT)):
			if j % 3:
				pygame.draw.line(surface, BLACK, (0, j*GRIDSIZE), (SCREEN_WIDTH, j*GRIDSIZE))
			else:
				pygame.draw.line(surface, BLACK, (0, j*GRIDSIZE), (SCREEN_WIDTH, j*GRIDSIZE), 5)

def putNumbers(screen, sudoku, myfont):
	for i in range(9):
		for j in range(9):
			if not sudoku[i][j]:
				continue
			text = myfont.render(f" {sudoku[i][j]}", 1, BLACK)
			screen.blit(text, (j*GRIDSIZE, i*GRIDSIZE))
	
	