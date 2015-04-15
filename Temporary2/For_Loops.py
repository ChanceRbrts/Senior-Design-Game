#This object can not move faster than 16 a step.
#Try to figure this one out!
from Solid import*
class For_Loops(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "For_Loops"
		self.codingStartVisible = [0,13,]
		self.codingEndVisible = [2,15,]
		self.forLoop = 0
		self.image = pygame.image.load('Game/Sprites/AsymetricStoneBlock.png')
		self.startX = self.x
	def doTheForLoop(self):
		for i in range(0,2):
			self.x += 16
			self.forLoop += 1
	def correctThisObject(self):
		if (self.x > self.startX+self.forLoop*16):
			self.x = self.startX+self.forLoop*16
