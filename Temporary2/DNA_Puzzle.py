#From a X-Number DNA Strand, DNAStrand,
#create the other DNA Strand to
#get through.
from Solid import*
class DNA_Puzzle(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "DNA_Puzzle"
		self.codingStartVisible = [0,12,]
		self.codingEndVisible = [3,13,]
		self.image = pygame.image.load('Game/Sprites/AsymetricStoneBlock.png');
	def getDNAStrand(self,DNAStrand):
		DNAStrand = "" #Not the answer...
		return(DNAStrand)
	def draw(self,Window,viewX,viewY):
		for i in range(0,self.xSpace):
			for j in range(0,self.ySpace):
				Window.blit(self.image,(self.x-viewX+i*32,self.y-viewY+j*32))
