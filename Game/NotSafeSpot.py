from Monster import*
class NotSafeSpot(Monster):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Monster.__init__(self,oX,oY,oW,oH)
		self.name = "Not Safe Spot"
		self.color = [0,0,0]
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(self.color[0],self.color[1],self.color[2]),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))