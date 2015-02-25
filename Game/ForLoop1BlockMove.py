from Solid import*
class ForLoop1BlockMove(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "ForLoop1BlockMove"
		self.image = pygame.image.load('Game/Sprites/SolidWall.png');
	def check(self,condition):
		if (condition == True):
			self.x = 0
	def draw(self, Window, viewX, viewY):
		for i in range(0,self.xSpace):
			for j in range(0,self.ySpace):
				Window.blit(self.image,(self.x-viewX+i*32,self.y-viewY+j*32))
