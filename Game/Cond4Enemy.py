from Monster import*
import random
class Cond4Enemy(Monster):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Monster.__init__(self,oX,oY,oW,oH)
		self.name = "Cond4Enemy"
		self.position = 2
		self.x = 117*32
		self.pos = "L"
		self.dY = 4
	def restartPos(self):
		self.y = 0
		pos = int(3*random.random())
		if (pos == 0):
			self.x = 117*32
			self.pos = "L"
		elif (pos == 1):
			self.y = 120*32
			self.pos = "M"
		elif (pos == 2):
			self.y = 123*32
			self.pos = "R"
	def update(self,controlPressed,controlHold):
		if (self.y >= 4*32):
			self.y = 4*32
			self.dY = 0
	