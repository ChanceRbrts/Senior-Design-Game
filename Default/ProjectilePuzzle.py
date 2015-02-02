#So I guess you won the race? :)
#Great! Here's what I want you to do now...
#You know the item that you clicked on?
#It will move as you touch it. 
#When it hits the wall, it will shoot out projectiles.
#Make sure both the projectile type and the radius is okay!
from Solid import*
class ProjectilePuzzle(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "ProjectilePuzzle"
		self.codingStartVisible = [0,13]
		self.codingEndVisible = [6,15]
		self.radius = 1
		self.projType = "Harmless"
	def getProjType(self):
		return(self.projType)
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(0,50,255),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
#Fin.