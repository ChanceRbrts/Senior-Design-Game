#If you have to check for multiple conditions,
#like if a variable is 1, 2, 3, or 4,
#then you can use elif condition: as
#another if statement if the previous conditions
#are considered false.
#Why don't you try it with this puzzle?
#The enemy's position is either L,M, or R,
#while the block's positions are 0, 1, and 2
from Solid import*
class Conditional_Puzzle_4(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "Conditional_Puzzle_4"
		self.codingStartVisible = [0,17,]
		self.codingEndVisible = [8,19,]
	def getPos(self,enemyPos):
		blockPos = 0
		if (enemyPos == "L"):
			blockPos = 0
		return(blockPos)
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(0,0,100),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
