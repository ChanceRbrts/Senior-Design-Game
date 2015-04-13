from Solid import*
import pygame
class RaceAssist(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "RaceAssist"
		self.image = pygame.image.load('Game/Sprites/CheckeredFlag.png');
	def update(self,oX=0,oY=0,oW=1,oH=1,oDX=0,oType=""):
		if (oY < self.y+self.ySpace*32 and oY+oH*32 > self.y and oX+oDX+oW*32 > self.x and oX+oW*32 <= self.x):
			if (oType == "YourRacer"):
				self.x = 0
				return(2)
			elif (oType == "TheirRacer"):
				return(1)
		return(0)
	def draw(self,Window,viewX,viewY):
		for i in range(0,self.xSpace):
			for j in range(0,self.ySpace):
				Window.blit(self.image,(self.x-viewX+i*32,self.y-viewY+j*32))