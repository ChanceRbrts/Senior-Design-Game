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
		self.codingStartVisible = [0,20,]
		self.codingEndVisible = [11,21,]
		self.name = "TintTheWalkway"
		self.image = pygame.image.load('Game/Sprites/AsymetricStoneBlock.png');
	def tint(self,instance):
		instance.color = [0,0,0]
		return(instance)
	def draw(self,Window,viewX,viewY):
		for i in range(0,self.xSpace):
			for j in range(0,self.ySpace):
				Window.blit(self.image,(self.x-viewX+i*32,self.y-viewY+j*32))
