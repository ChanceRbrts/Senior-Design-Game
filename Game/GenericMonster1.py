from Monster import*
class GenericMonster1(Monster):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Monster.__init__(self,oX,oY,oW,oH)
		self.name = "GenericMonster1"
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(255,0,0),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))