#See if you can reverse the emit using if statements!
from Solid import*
class Laser_Emitter(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "Laser_Emitter"
		self.activate = False
		self.codingStartVisible = [0,10,]
		self.codingEndVisible = [1,11,]
	def setEmit(self,activated):
		self.activate = activated
	def getEmit(self):
		if (self.activate):
			return(False)
		return(True)
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(0,0,100),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
