from Instance import*
class SafeSpot(Instance):
	def __init__(self,oX=0,oY=0):
		Instance.__init__(self,oX,oY)
		self.color = [0,0,0]
		self.name = "Safe Spot"
	def draw(self, Window, viewX, viewY):
		pygame.draw.rect(Window,(self.color[0],self.color[1],self.color[2]),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))