from Instance import*
class Monster(Instance):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Instance.__init__(self,oX,oY)
		self.xSpace = oW
		self.ySpace = oH
		self.width = oW*32
		self.height = oH*32
		self.collision = "Monster"
		self.codeToChange = "Monster.py"