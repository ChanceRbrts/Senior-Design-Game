#Try to make objective.x equal to self.x!
#The maximum distance this block can move is 16!
#Note: The for loop will no longer work...
from Solid import*
from pygame import*
class RecursionPuzzle1(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "RecursionPuzzle1"
		self.codingStartVisible = [0,14,]
		self.codingEndVisible = [3,20,]
		self.recursionTimes = 0
		self.startX = self.x
		self.image = pygame.image.load('Game/Sprites/AsymetricStoneBlock.png');
	def recursion(self, objective):
		self.x += 16
		if (self.x < objective.x):
			print("This is too far to the left!")
			#What happens if you call this function here?
		self.recursionTimes += 1
	def correctThisObject(self):
		if (self.x > self.startX+self.recursionTimes*16):
			self.x = self.startX+self.recursionTimes*16
	def draw(self,Window,viewX,viewY):
		for i in range(0,self.xSpace):
						for j in range(0,self.ySpace):
								Window.blit(self.image,(self.x-viewX+i*32,self.y-viewY+j*32))

	