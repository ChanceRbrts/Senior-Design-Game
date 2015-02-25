from Solid import*
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
		self.dX = 1
		self.codingStartVisible = [5,15,19,]
		self.codingEndVisible = [12,16,20,]
	def update(self,controlPressed,controlHold):
		self.dX *= 2
		if (self.dX > 101010):
			self.dX = 101010
	def finishUpdate(self):
		self.x += self.dX
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(0,0,100),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
