from Instance import*
import pygame
from pygame.locals import*
import os
from os.path import*
class Solid(Instance):
		def __init__(self,oX=0,oY=0,oW=1,oH=1):
			Instance.__init__(self,oX,oY)
			self.xSpace = oW
			self.ySpace = oH
			self.width = oW*32
			self.height = oH*32
			self.collision = "Solid"
			self.name = "Solid"
			self.codeToChange = "Solid.py"
			self.image = pygame.image.load('Game/Sprites/SolidWall.png');
		def draw(self, Window, viewX, viewY):
				for i in range(0,self.xSpace):
						for j in range(0,self.ySpace):
								Window.blit(self.image,(self.x-viewX+i*32,self.y-viewY+j*32))