from Instance import*
class Laser(Instance):
	def __init__(self,oX=0,oY=0):
		Instance.__init__(self,oX,oY)
		self.ySpace = 6
		self.activate = False
		self.name = "Laser"
	def getActivate(self, caught):
		self.activate = caught
	def draw(self,Window,viewX,viewY):
		if (self.activate):
			pygame.draw.rect(Window,(255,0,0),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
	
	
