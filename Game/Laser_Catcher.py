from Instance import*
import random
class Laser_Catcher(Instance):
	def __init__(self,oX=0,oY=0):
		Instance.__init__(self,oX,oY)
		self.caught = True
		self.name = "Laser_Catcher"
	def checkTheLaser(self,instance):
		if (instance.activate == self.caught):
			return(True)
		return(False)
	def update(self,controlPressed,controlHold):
		self.caught = random.choice([True,False])
	def draw(self,Window,viewX,viewY):
		if (self.caught):
			pygame.draw.rect(Window,(155,155,155),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
		else:
			pygame.draw.rect(Window,(50,50,50),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
