#! usr/bin/dev python

from images import *
from tanks_ import PlayerTank
import pygame
import random


screen_Dimension=[32*13,32*13]

pygame.init()

screen = pygame.display.set_mode(screen_Dimension)

pygame.display.set_caption("My_Poor_NES_Batlle_City")

clock = pygame.time.Clock()



def plotWalls():
	for i in range(0,screen_Dimension[0],32):
		screen.blit(bricks,[i,0])
		screen.blit(bricks,[i,screen_Dimension[1]-32])
	for j in range(0,screen_Dimension[1],32):
		screen.blit(bricks,[0,j])
		screen.blit(bricks,[screen_Dimension[0]-32,j])


Tank = PlayerTank(blueTank, [64,64], screen)

while True:

	screen.fill([0,0,0])

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()

			Tank.move(event)


	Tank.plot()
	plotWalls()
	pygame.display.update()

	clock.tick(60)



