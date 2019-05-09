#! usr/bin/dev python

<<<<<<< HEAD
from stage_interpreter import Stages	#Le as fases
from tanks_ import PlayerTank 			#Responsável pelos tanques do player
from imagens import *					#imagens do jogo

=======
from images import *
from tanks_ import PlayerTank
>>>>>>> 35e89f9b98e05f111441d240cf7589fc456fce76
import pygame
import random


<<<<<<< HEAD
screen_Dimension=[32*20,32*20]
=======
screen_Dimension=[32*13,32*13]
>>>>>>> 35e89f9b98e05f111441d240cf7589fc456fce76

pygame.init()

screen = pygame.display.set_mode(screen_Dimension)

pygame.display.set_caption("My_Poor_NES_Batlle_City")

clock = pygame.time.Clock()


<<<<<<< HEAD
Fase_1 = Stages(screen)
Fase_1.readStage(1)
=======

def plotWalls():
	for i in range(0,screen_Dimension[0],32):
		screen.blit(bricks,[i,0])
		screen.blit(bricks,[i,screen_Dimension[1]-32])
	for j in range(0,screen_Dimension[1],32):
		screen.blit(bricks,[0,j])
		screen.blit(bricks,[screen_Dimension[0]-32,j])
>>>>>>> 35e89f9b98e05f111441d240cf7589fc456fce76


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


<<<<<<< HEAD

	Fase_1.plotStage()
	Tank.plot()
	pygame.display.update()


=======
	Tank.plot()
	plotWalls()
	pygame.display.update()

>>>>>>> 35e89f9b98e05f111441d240cf7589fc456fce76
	clock.tick(60)



