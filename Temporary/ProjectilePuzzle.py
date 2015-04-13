#So I guess you won the race? :)
#Great! Here's what I want you to do now...
#You know the item that you clicked on?
#It will move as you touch it. 
#When it hits the wall, it will shoot out projectiles.
#Make sure both the projectile is Harmful and the radius
#is okay!
from Solid import*
class ProjectilePuzzle(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "ProjectilePuzzle"
		self.codingStartVisible = [0,14,]
		self.codingEndVisible = [6,16,]
		self.radius = 1
		self.projType = "Harmless"
		self.image = pygame.image.load('Game/Sprites/AsymetricStoneBlock.png');
	def getProjType(self):
		return(self.projType)
	def draw(self,Window,viewX,viewY):
		for i in range(0,self.xSpace):
						for j in range(0,self.ySpace):
								Window.blit(self.image,(self.x-viewX+i*32,self.y-viewY+j*32))
#Fin.
