#Hey! You're almost done with the Conditional Puzzles!
#With the condition, you can use 'or' to have the code
#run if one out of X conditions are true.
#Pretty much,
#if condition1 or condition2 or condition3 or...:
#Just make sure that 'DoorPart1' and 'DoorPart2' can
#get through this block, but not anything else.
from Solid import*
class Conditional_Puzzle_5(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.codingStartVisible = [0,14,]
		self.codingEndVisible = [7,17,]
		self.name = "Conditional_Puzzle_5"
	def collisionOfSolidObject(self, oX,oY,oW):
		pass
	
