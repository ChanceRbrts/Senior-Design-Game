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
		self.codingStartVisible = [0,15,]
		self.codingEndVisible = [6,16,]
		self.name = "TintTheWalkway2"
		self.image = pygame.image.load('Game/Sprites/AsymetricStoneBlock.png')
	def tint(self,instance):
		instance[0].color = [0,0,0]
		return(instance)
