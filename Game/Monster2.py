from Monster import*
import random
class Monster2(Monster):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Monster.__init__(self,oX,oY,oW,oH)
		self.name = "Monster2"
	def update(self,controlPressed,controlHold):
		self.name = ""
		for i in range(0,9):
			self.name += random.choice(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
										"S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i",'j','k','l','m',
										'n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8',
										'9','0'])
		self.dY = -2
	def finishUpdate(self):
		self.y += self.dY
		if (self.y < 256):
			self.y = 256
			self.dY = 0
