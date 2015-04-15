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
		self.name = "Player"
		self.collision = "Full"
		self.direction = 180
		self.walkingFrame = 0
		self.maxWalkingFrame = 10
		self.pushingFrame = 0
		self.maxPushingFrame = 2
		self.prevDX = 0
		self.prevDY = 0
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
		self.prevDX = self.dX
		self.prevDY = self.dY
	def draw(self,Window,viewX,viewY):
		if ((self.dX != 0 or self.dY != 0) and self.walkingFrame == 0):
				self.walkingFrame = 1
		if (self.dX == 0):
				if (self.dY == 0):
						self.walkingFrame = 0
				elif (self.dY < 0):
						self.direction = 0
				elif (self.dY > 0):
						self.direction = 180
		elif (self.dX < 0):
				if (self.dY == 0):
						self.direction = 90
				elif (self.dY < 0):
						self.direction = 45
				elif (self.dY > 0):
						self.direction = 135
		elif (self.dX > 0):
				if (self.dY == 0):
						self.direction = 270
				elif (self.dY < 0):
						self.direction = 315
				elif (self.dY > 0):
						self.direction = 225
		imageToDraw = "Player"
		if (self.walkingFrame > 0):
				self.walkingFrame += 0.25
				if (self.walkingFrame >= self.maxWalkingFrame+1):
						self.walkingFrame = 1
				imageToDraw = "Step "+str(int(self.walkingFrame))+".png"
		else:
				if (self.prevDX == self.dX and self.prevDY == self.dY):
						imageToDraw = "Step 10.png"
						self.pushingFrame = 0
				else:
						if (self.prevDX == 0):
								if (self.prevDY < 0):
										self.direction = 0
								elif (self.prevDY > 0):
										self.direction = 180
						elif (self.prevDX < 0):
								if (self.prevDY == 0):
										self.direction = 90
								elif (self.prevDY < 0):
										self.direction = 45
								elif (self.prevDY > 0):
										self.direction = 135
						elif (self.prevDX > 0):
								if (self.prevDY == 0):
										self.direction = 270
								elif (self.prevDY < 0):
										self.direction = 315
								elif (self.prevDY > 0):
										self.direction = 225
						if (self.pushingFrame == 0):
								self.pushingFrame = 1
						else:
								self.pushingFrame += 0.25
								if (self.pushingFrame >= self.maxPushingFrame+1):
										self.pushingFrame = 1
						imageToDraw = "Push "+str(int(self.pushingFrame))+".png"
		image = pygame.image.load('Game/Sprites/Player/'+imageToDraw)
		Window.blit(pygame.transform.rotate(image, self.direction),(self.x-viewX,self.y-viewY))
		