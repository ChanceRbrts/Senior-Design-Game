#Hey! You're almost done with the Conditional Puzzles!
#With the condition, you can use 'or' to have the code
#run if one out of X conditions are true.
#Pretty much, check with name
#if condition1 or condition2 or condition3 or...:
#Just make sure that 'DoorPart1' and 'DoorPart2' can
#get through this block, but not anything else.
from Solid import*
class Conditional_Puzzle_5(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.codingStartVisible = [0,16,]
		self.codingEndVisible = [7,19,]
		self.name = "Conditional_Puzzle_5"
		self.image = pygame.image.load('Game/Sprites/AsymetricStoneBlock.png')
	def collisionOfSolidObject(self,name):
		goThrough = False
		if (name == 'DoorPart1' or name == 'DoorPart2'):
			goThrough = True
		return(goThrough)
	def collideWithSolid(self, oX, oY, oW, oH, oDX=0, oDY=0, name=""):
		x = oX
		y = oY
		dY = oDY
		dX = oDX
		if (self.collisionOfSolidObject(name) == False):
			if (x+dX < self.x+self.xSpace*32+self.dX and x+oW+dX > self.x+self.dX and
				y+dY+oH > self.y+self.dY and y+oH <= self.y):
				y = self.y-oH+self.dY
				dY = 0
			if (x+dX < self.x+self.xSpace*32+self.dX and x+oW+dX > self.x+self.dX and
				y+dY < self.y+self.ySpace*32+self.dY and y >= self.y+self.ySpace*32):
				y = self.y+self.ySpace*32+self.dY
				dY = 0
			if (y+dY < self.y+self.ySpace*32+self.dY and y+oH+dY > self.y+self.dY and
				x+dX+oW > self.x+self.dX and x+oW <= self.x):
				x = self.x-oW+self.dX
				dX = 0
			if (y+dY < self.y+self.ySpace*32+self.dY and y+oH+dY > self.y+self.dY and
				x+dX < self.x+self.xSpace*32+self.dX and x >= self.x+self.xSpace*32):
				x = self.x+self.xSpace*32+self.dX
				dX = 0
		return([x,y,dX,dY])
	
