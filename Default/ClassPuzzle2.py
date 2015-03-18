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
		self.codingStartVisible = [0,]
		self.codingEndVisible = [16,]
	def checkType(self):
		if (self.collision == "Solid"):
			pass
		elif (self.collision == "Monster"):
			self.dX = -1
	def finishUpdate(self):
		self.x += self.dX
	def draw(self,Window,viewX,viewY):
		if (self.collision == "Solid"):
			pygame.draw.rect(Window,(0,0,100),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
		else:
			super.draw(Window,viewX,viewY)
	
	