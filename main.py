#################################################################
#						  IMPORTAÇÕES	        				#
#################################################################
import pygame
import random


#################################################################
#						  VARIAVEIS		        				#
#################################################################

screen_Dimension=[1200,900]

cor = {
	"preto"   : [  0,  0,  0],
	"laranja" : [200,100, 50],
	"verde"   : [ 50,200, 50],
	"marrom"  : [200, 50,100]
}

#background = pygame.image.load("/home/brunosampaio/BattleCity/back.png")
background = pygame.Surface([16,16])
background.fill(cor["preto"])

brick      = pygame.image.load("/home/brunosampaio/BattleCity/brick.png")
leave      = pygame.image.load("/home/brunosampaio/BattleCity/leave.png")
dirt       = pygame.image.load("/home/brunosampaio/BattleCity/dirt.png")
iron       = pygame.image.load("/home/brunosampaio/BattleCity/iron.png")


Dir = {
	"Stopped" : [ 0, 0],
	"Up"      : [ 0,-1],
	"Down"    : [ 0, 1],
	"Right"   : [ 1, 0],
	"Left"    : [-1, 0]
}


#################################################################
#						DEFINIÇÕES		        				#
#################################################################

direcao  = Dir["Stopped"]


#################################################################
#						  FUNÇÕES		        				#
#################################################################

def key_Down(event_key):
	pass


#################################################################
#					  CÓDIGO AVULSO		        				#
#################################################################



#################################################################
#						  PYGAME		        				#
#################################################################

pygame.init()

screen = pygame.display.set_mode(screen_Dimension)

pygame.display.set_caption("My_Poor_NES_Batlle_City")

clock = pygame.time.Clock()

while True:

	screen.fill(cor["preto"])

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()

	screen.blit(leave, [0,0])
	screen.blit(brick, [60,0])
	screen.blit(iron, [40,0])
	screen.blit(dirt, [20,20])

	pygame.display.update()

	clock.tick(20)

