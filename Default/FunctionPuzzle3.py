#Can you solve this?
#HINT: PARAMETERS.
from Solid import*
class FunctionPuzzle3(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "FunctionPuzzle3"
		self.codingStartVisible = [0,9,]
		self.codingEndVisible = [2,12,]
	def moveSolidObjects(self,x=[],y=[]):
		for i in range(0,len(x)):
			a = self.doSomeStuffWith(x[i],y[i])
			print(a[0])
			x[i] = a[0]
			y[i] = a[1]
		return([x,y])
	def doSomeStuffWith(self,x,y):
		return([y,x])
