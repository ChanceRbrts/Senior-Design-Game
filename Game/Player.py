import Instance
import pygame
from pygame.locals import*
class Player(Instance.Instance):
	def __init__(self,oX=0,oY=0):
		Instance.Instance.__init__(self,oX,oY)
		self.rightHold = False
		self.leftHold = False
		self.upHold = False
		self.downHold = False
		self.xSpace = 1
		self.ySpace = 1
		self.name = ""
	def update(self,controlPressed,controlHold):
		for i in range(0,len(controlHold)):
			if controlHold[i] == K_LEFT:
				self.leftHold = True
			if controlHold[i] == K_RIGHT:
				self.rightHold = True
			if controlHold[i] == K_UP:
				self.upHold = True
			if controlHold[i] == K_DOWN:
				self.downHold = True
		if (self.rightHold and self.leftHold == False):
			self.dX = 4
		elif (self.leftHold and self.rightHold == False):
			self.dX = -4
		else:
			self.dX = 0
		if (self.downHold and self.upHold == False):
			self.dY = 4
		elif (self.upHold and self.downHold == False):
			self.dY = -4
		else:
			self.dY = 0
		self.rightHold = False
		self.leftHold = False
		self.upHold = False
		self.downHold = False
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(255,255,255),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
