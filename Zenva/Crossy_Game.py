import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()
TICK_RATE = 60
is_game_over = False


game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_screen.fill(WHITE_COLOR)

while not is_game_over:
	pygame.display.update()
	clock.tick(TICK_RATE)
	