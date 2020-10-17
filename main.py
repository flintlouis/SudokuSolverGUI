import pygame
import numpy as np
from sudoku import Sudoku
from info import Settings, handleKeys, initPygame
from puzzles import SUDOKUS
import os
import sys

def usage():
	print("\nUsage: python main.py <empty|easy|hard|evil|wrong>\n")
	exit()

def main():
	if len(sys.argv) != 2:
		usage()
	try:
		puzzle = SUDOKUS[sys.argv[1]]
	except:
		usage()
	os.system("clear")
	print("Loading...")
	surface, screen = initPygame()
	clock = pygame.time.Clock()
	myfont = pygame.font.SysFont("arialblack", 35)
	settings = Settings(surface, screen, clock, myfont)
	os.system("clear")

	sudoku = Sudoku(puzzle)
	sudoku.showSudoku(settings)
	while True:
		handleKeys(settings)
		if settings.start and not settings.finished:
			os.system("clear")
			if sudoku.solve(settings):
				print("SOLVED")
			else:
				print("UNSOLVABLE")
			settings.finished = True
			settings.start = False
		elif settings.start and settings.finished:
			sudoku.state = np.array(sudoku.starting_state)
			sudoku.showSudoku(settings)
			settings.finished = False
			settings.start = False

main()
