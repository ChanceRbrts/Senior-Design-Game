from Solid import*
from pygame import*
class YourRacer(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "YourRacer"
		#Let's race the other block!
		#Some commands that might help you out!
		#* Multiplies a Variable
		#/ Divides a Variable
		#% Gives you the Remainder
		#- Subtracts Things
		self.dX = 0
		self.codingStartVisible = [6,17,21,]
		self.codingEndVisible = [13,18,22,]
		self.image = pygame.image.load('Game/Sprites/AsymetricStoneBlock.png');
	def update(self,controlPressed,controlHold):
		self.dX = 1
		if (self.dX > 101010):
			self.dX = 101010
	def finishUpdate(self):
		self.x += self.dX
	def draw(self,Window,viewX,viewY):
		for i in range(0,self.xSpace):
						for j in range(0,self.ySpace):
								Window.blit(self.image,(self.x-viewX+i*32,self.y-viewY+j*32))

