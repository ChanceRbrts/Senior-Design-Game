#Note: This is the basic instance class. This is intended to only be a class to extend upon.
import pygame
from pygame.locals import*
import sys
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
		self.color = [0,0,0]
	def update(self,controlPressed,controlHold):
		return(0)
	def finishUpdate(self):
		self.x += self.dX;
		self.y += self.dY;
	def draw(self, Window, viewX, viewY):
		pygame.draw.rect(Window,(0,0,0),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
	def getCollisionType(self):
		return(self.collision)
	def collideWithSolid(self, oX, oY, oW, oH, oDX=0, oDY=0, instance=[]):
		if self.collision == "Full":
				x = self.x
				y = self.y
				dY = self.dY
				dX = self.dX
				checkOtherCollision = False
				if (self.x+self.dX < oX+oW+oDX and self.x+self.xSpace*32+self.dX > oX+oDX and
						self.y+self.dY+self.ySpace*32 > oY+oDY and self.y+self.ySpace*32 <= oY):
					y = oY-self.ySpace*32+oDY
					dY = 0
					if (oDX != 0 or oDY != 0):
						checkOtherCollision = True
				if (self.x+self.dX < oX+oW+oDX and self.x+self.xSpace*32+self.dX > oX+oDX and
						self.y+self.dY < oY+oH+oDY and self.y >= oY+oH):
					y = oY+oH+oDY
					dY = 0
					if (oDX != 0 or oDY != 0):
						checkOtherCollision = True
				if (self.y+self.dY < oY+oH+oDY and self.y+self.ySpace*32+self.dY > oY+oDY and
						self.x+self.dX+self.xSpace*32 > oX+oDX and self.x+self.xSpace*32 <= oX):
					x = oX-self.xSpace*32+oDX
					dX = 0
					if (oDX != 0 or oDY != 0):
						checkOtherCollision = True
				if (self.y+self.dY < oY+oH+oDY and self.y+self.ySpace*32+self.dY > oY+oDY and
						self.x+self.dX < oX+oW+oDX and self.x >= oX+oW):
					x = oX+oW+oDX
					dX = 0
					if (oDX != 0 or oDY != 0):
						checkOtherCollision = True
				if (checkOtherCollision):
						for i in range(0,len(instance)):
								if (x+dX <= instance[i].x+instance[i].xSpace*32+instance[i].dX and x+self.xSpace*32+dX >= instance[i].x+instance[i].dX
									and y+dY <= instance[i].y+instance[i].ySpace*32+instance[i].dY and y+self.ySpace*32+dY >= instance[i].y+instance[i].dY
										and (oX+oDX != instance[i].x+instance[i].dX and oY+oDY != instance[i].y+instance[i].dY)
										and (self.x != instance[i].x and self.y != instance[i].y)):
										sys.exit()
				self.x = x
				self.y = y
				self.dX = dX
				self.dY = dY
	def collideWithMonster(self, oX, oY, oW, oH, oDX=0, oDY=0):
		if (self.x+self.dX <= oX+oW+oDX and self.x+self.dX >= oX+oDX and self.y+self.dY <= oY+oH+oDY and self.y+self.dY >= oY+oDY):
			return(True)
		return(False)
	
