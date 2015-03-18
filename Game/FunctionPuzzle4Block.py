from Solid import*
class FunctionPuzzle4Block(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "FunctionPuzzle4Block"
	def verifyValue(self, value):
		if value == [0,True]:
			self.x = 0
	

