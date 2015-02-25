#Okay. Good! You have been exposed to an if statement!
#Now, let's see if you can make one yourself!
#The are two objects, one safe spot, and one
#non-safe spot, whose instance.name are
#"Safe Spot", and "Not Safe Spot".
#Each of them have a collection of values, which
#is set up for you below. Value 1 is Red, Value
#2 is Green, and Value 3 is Blue.
#If you need a reminder on how if statements work,
#just look at the first puzzle again.
#Good luck! :D
from Solid import*
class TintTheWalkway(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.codingStartVisible = [0,19,]
		self.codingEndVisible = [11,21,]
		self.name = "TintTheWalkway"
	def tint(self,instance):
		if instance.name == "Not Safe Spot":
			instance.color = [255,0,0]
		return(instance)
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(0,0,100),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
