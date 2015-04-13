from Solid import*
class SolidPuzzle1(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "SolidPuzzle1"
		self.codingStartVisible = [9,11,]
		self.codingEndVisible = [10,12,]
		self.image = pygame.image.load('Game/Sprites/AsymetricStoneBlock.png');
	def update(self,controlPressed,controlHold):
		self.dY = 0
	def finishUpdate(self):
		self.y += self.dY
	def draw(self,Window,viewX,viewY):
		for i in range(0,self.xSpace):
						for j in range(0,self.ySpace):
								Window.blit(self.image,(self.x-viewX+i*32,self.y-viewY+j*32))


