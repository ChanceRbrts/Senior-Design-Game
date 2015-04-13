from Monster import*
class GenericMonster1(Monster):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Monster.__init__(self,oX,oY,oW,oH)
		self.name = "GenericMonster1"
		