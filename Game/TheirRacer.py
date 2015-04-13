from Solid import*
class TheirRacer(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "TheirRacer"
		self.image = pygame.image.load('Game/Sprites/SmallStoneBlock.jpg');
	def finishUpdate(self):
		self.x += self.dX
	def draw(self,Window,viewX,viewY):
		for i in range(0,self.xSpace):
						for j in range(0,self.ySpace):
								Window.blit(self.image,(self.x-viewX+i*32,self.y-viewY+j*32))