#This object can not move faster than 16 a step.
#Try to figure this one out!
from Solid import*
class For_Loops(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "For_Loops"
		self.codingStartVisible = [0,12,]
		self.codingEndVisible = [2,14,]
		self.forLoop = 0
		self.startX = self.x
	def doTheForLoop(self):
		for i in range(0,16):
			self.x += 16
			self.forLoop += 1
	def correctThisObject(self):
		if (self.x > self.startX+self.forLoop*16):
			self.x = self.startX+self.forLoop*16
