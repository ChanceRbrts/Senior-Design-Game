from Instance import*
class DoorPart1(Instance):
	def __init__(self,oX=0,oY=0):
		Instance.__init__(self,oX,oY)
		self.name = "DoorPart1"
		self.collision = "Not Even Full"
	def update(self,controlPressed,controlHold):
		self.dY = -2
	def finishUpdate(self):
		self.y += self.dY
		if (self.y < 256):
			self.y = 256
			self.dY = 0
	def draw(self, Window, viewX, viewY):
		pygame.draw.rect(Window,(155,0,155),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))

class DoorPart2(Instance):
	def __init__(self,oX=0,oY=0):
		Instance.__init__(self,oX,oY)
		self.name = "DoorPart2"
		self.collision = "Not Even Full"
	def update(self,controlPressed,controlHold):
		self.dY = -2
	def finishUpdate(self):
		self.y += self.dY
		if (self.y < 256):
			self.y = 256
			self.dY = 0
	def draw(self, Window, viewX, viewY):
		pygame.draw.rect(Window,(155,0,155),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
