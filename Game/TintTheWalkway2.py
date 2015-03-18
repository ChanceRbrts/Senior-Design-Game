#Remember how to do this one?
#Now, do it with for loops!
#Remember that the .name for all objects
#should either be "Safe Spot" or
#"Not Safe Spot".
#The .color should be [R,G,B].
from Solid import*
class TintTheWalkway2(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.codingStartVisible = [0,14,]
		self.codingEndVisible = [6,17,]
		self.name = "TintTheWalkway2"
	def tint(self,instance):
		for i in range(0,len(instance)):
			if (instance[i].name == "Not Safe Spot"):
				instance[i].color = [255,0,0]
		return(instance)
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(0,0,100),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
