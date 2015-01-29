#Note: This is the basic instance class. This is intended to only be a class to extend upon.
import pygame
from pygame.locals import*
class Instance():
	def __init__(self,oX=0,oY=0):
		self.x = oX*32
		self.y = oY*32
		self.dX = 0
		self.dY = 0
		self.xSpace = 1
		self.ySpace = 1
		self.collision = "Full"
		self.codeToChange = "Instance.py"
		self.ramEverythingDown = False
		self.name = ""
		self.codingStartVisible = [0]
		self.codingEndVisible = [999999]
	def update(self,controlPressed,controlHold):
		return(0)
	def finishUpdate(self):
		self.x += self.dX;
		self.y += self.dY;
	def draw(self, Window, viewX, viewY):
		pygame.draw.rect(Window,(0,0,0),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
	def getCollisionType(self):
		return(self.collision)
	def collideWithSolid(self, oX, oY, oW, oH):
		if self.collision == "Full":
			if (self.x+self.dX < oX+oW and self.x+self.xSpace*32+self.dX > oX and
					self.y+self.dY+self.ySpace*32 > oY and self.y+self.ySpace*32 <= oY):
				self.y = oY-self.ySpace*32
				self.dY = 0
			if (self.x+self.dX < oX+oW and self.x+self.xSpace*32+self.dX > oX and
					self.y+self.dY < oY+oH and self.y >= oY+oH):
				self.y = oY+oH
				self.dY = 0
			if (self.y+self.dY < oY+oH and self.y+self.ySpace*32+self.dY > oY and
					self.x+self.dX+self.xSpace*32 > oX and self.x+self.xSpace*32 <= oX):
				self.x = oX-self.xSpace*32
				self.dX = 0
			if (self.y+self.dY < oY+oH and self.y+self.ySpace*32+self.dY > oY and
					self.x+self.dX < oX+oW and self.x >= oX+oW):
				self.x = oX+oW
				self.dX = 0
	def collideWithMonster(self, oX, oY, oW, oH, oDX=0, oDY=0):
		if (self.x+self.dX < oX+oW+oDX and self.x+self.dX > oX+oDX and self.y+self.dY < oY+oH+oDY and self.y+self.dY > oY+oDY):
			return(True)
		return(False)
	
