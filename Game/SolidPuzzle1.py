from Solid import*
class SolidPuzzle1(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "SolidPuzzle1"
	def update(self,controlPressed,controlHold):
		self.dY = 4
	def finishUpdate(self):
		self.y += self.dY