from Solid import*
class Conditional_Puzzle_3(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "Conditional_Puzzle_3"
		self.thisY = self.y
		self.thatY = self.y-32
	def getYPosition(self, conditions):
		if conditions == True:
			self.y = self.thatY
		else:
			self.y = self.thisY
	
