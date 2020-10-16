import pygame
import sys

SCREEN_WIDTH = 450
SCREEN_HEIGHT = 450

GRIDSIZE = 50
GRID_WIDTH = SCREEN_WIDTH / GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRIDSIZE

FPS = 100

WHITE = (255,255,255)
BLACK = (0,0,0)

class Settings(object):
	def __init__(self, surface, screen, clock, myfont):
		self.surface = surface
		self.screen = screen
		self.clock = clock
		self.myfont = myfont
		self.start = False
		self.finished = False

def handleKeys(settings):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
		elif event.type == pygame.KEYDOWN and not settings.start:
			if event.key == pygame.K_SPACE:
				settings.start = True

def initPygame():
	pygame.init()
	pygame.display.set_caption("Sudoku Solver")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
	surface = pygame.Surface(screen.get_size())
	surface = surface.convert()
	return surface, screen
