#Now, this passageway will not be
#opened unless this object has 10
#or more objects in its objects list.
#...Why don't you try to make your own?
#Remember: To add to a list, use list.append!
from Solid import*
class ClassPuzzle3(Solid):
	#Okay... Let's finally talk about what
	#__init__ does. __init__ creates a new
	#object of the class, and is called in
	#this case as ClassPuzzle3(xPos,yPos,1,1)
	#or something like that... The = means that
	#it is the default value if nothing is added,
	#so ClassPuzzle3() = ClassPuzzle3(0,0,1,1)
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "ClassPuzzle3"
		self.objects = []
		for i in range(0,10):
			self.objects.append(Solid())
		self.codingStartVisible = [0,]
		self.codingEndVisible = [26,]
		self.image = pygame.image.load('Game/Sprites/AsymetricStoneBlock.png');
	
#You can have more than 1 object in the .py file.
#...We just chose not to for some weird reason...

