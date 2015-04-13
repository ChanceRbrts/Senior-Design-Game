from Solid import*
class SolidPuzzle2(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "SolidPuzzle2"
		self.codingStartVisible = [9,]
		self.codingEndVisible = [11,]
		self.image = pygame.image.load('Game/Sprites/AsymetricStoneBlock.png');
	def finishUpdate(self):
		self.x = 19*32
		self.y = 3*32
	def draw(self,Window,viewX,viewY):
		for i in range(0,self.xSpace):
						for j in range(0,self.ySpace):
								Window.blit(self.image,(self.x-viewX+i*32,self.y-viewY+j*32))

