#This is a while loop.
#It is kind of like a for loop, but it
#loops if the conditions set are true.
#So, if you are not careful, you can
#(and probably will) break the program. :|
#The condition in this case is the number
#of characters in a string, or len(string)
#Let's see if you can get it to say 16 As
#in a row! (Using while loops, and not just
#changing what is added to the string!)
from Solid import*
class ForLoop3(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.codingStartVisible = [0,20,]
		self.codingEndVisible = [10,22,]
		self.name = "ForLoop3"
		self.justInCaseTheyLoopForever = 0
	def whileString(self):
		string = ""
		while len(string) < 0:
			string += "A"
			self.justInCaseTheyLoopForever += 1
			if (self.justInCaseTheyLoopForever > 9999):
				break
		if (self.justInCaseTheyLoopForever <= 1):
			string = "."
		if string == "":
			string = "."
		return(string)
	def draw(self,Window,viewX,viewY):
		pygame.draw.rect(Window,(0,0,100),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
