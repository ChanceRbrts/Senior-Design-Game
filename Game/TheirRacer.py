from Solid import*
class TheirRacer(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "TheirRacer"
	def finishUpdate(self):
		self.x += self.dX
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(100,0,50),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))