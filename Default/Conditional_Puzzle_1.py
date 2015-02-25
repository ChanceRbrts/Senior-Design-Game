#Hey! You made it through Variables! Awesome!
#This next part is all about conditional
#statements. They usually look kind of
#like this:
#if x:
#	doSomeStatement
#	doAnotherStatement
#continueOnWithCode
#To make the rectangle appear, just simply hit
#the 'tab' key!
#Try it out by clearing a path!
from Solid import*
from Instance import*
class Conditional_Puzzle_1(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "Conditional_Puzzle_1"
		self.ramEverythingDown = True
		self.codingStartVisible = [0,24,]
		self.codingEndVisible = [11,26,]
		self.keepIfStatementGoing = True
	def ifStatement(self,instances = []):
		if (self.keepIfStatementGoing):
			for i in range(0,len(instances)):
				if instances[i].y/32==0 and instances[i].x/32==19:
					instances[i].x = 0
					self.keepIfStatementGoing = False
	
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(0,0,100),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
