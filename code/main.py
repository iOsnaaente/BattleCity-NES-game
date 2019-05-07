import pygame
import random

screen_Dimension=[32*13,32*13]

pygame.init()

screen = pygame.display.set_mode(screen_Dimension)

pygame.display.set_caption("My_Poor_NES_Batlle_City")

clock = pygame.time.Clock()


rec = pygame.Rect((100,100), [30,30])


def readKeyboard(event):
	if event.key == pygame.K_ESCAPE:
		pygame.quit()

	if event.key == pygame.K_w:
		rec.move_ip(0,-30)

	if event.key == pygame.K_a:
		rec.move_ip(-30,0)

	if event.key == pygame.K_s:
		rec.move_ip(0,30)

	if event.key == pygame.K_d:
		rec.move_ip(30,0)



while True:

	screen.fill([0,0,0])

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			readKeyboard(event)

	pygame.draw.rect(screen,[250,250,250], rec)

	pygame.display.update()

	clock.tick(60)

