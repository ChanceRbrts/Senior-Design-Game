#Now, as you can see, classes have a whole
#bunch of functions. The init function is
#one that is called to create the object.
#ClassPuzzle2 in this case is a subclass,
#or a class that builds off a "super" class.
#That's what (Solid) and Solid.__init__ does.
#Now, this object is stubborn as a Solid
#object, but as a Monster, it decides to finally move.
from Solid import*
from Monster import*
class ClassPuzzle2(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "ClassPuzzle2"
		if (self.collision == "Solid"):
			self.image = pygame.image.load("Game/Sprites/AsymetricStoneBlock.png")
		self.codingStartVisible = [0,]
		self.codingEndVisible = [14,]
	def checkType(self):
		if (self.collision == "Solid"):
			pass
		elif (self.collision == "Monster"):
			self.dX = -1
	def finishUpdate(self):
		self.x += self.dX
	