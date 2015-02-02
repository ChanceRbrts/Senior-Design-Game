from Monster import*
import math
class ProjectileForPuzzle(Monster):
	def __init__(self,oX=-1,oY=-1,oDX=-1,oDY=-1,oR=1,oN="Projec"):
		Monster.__init__(self,oX,oY,1,1)
		self.name = oN
		self.startX = self.x
		self.startY = self.y
		self.radius = oR
		self.dX = oDX
		self.dY = oDY
	def update(self,controlPressed,controlHold):
		if self.x < 0:
			self.x = -12800
		elif (math.hypot(self.x-self.startX,self.y-self.startY) > self.radius*32):
			self.x = -12800-self.dX
			self.y = -12800-self.dY
			self.name = "Projec"
	def finishUpdate(self):
		self.y += self.dY
		self.x += self.dX
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(255,50,0),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))