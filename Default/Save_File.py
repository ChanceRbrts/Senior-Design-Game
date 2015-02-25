from Instance import*
class Save_File(Instance):
	def __init__(self,oX=0,oY=0):
		Instance.__init__(self)
		self.codingStartVisible = [7,]
		self.codingEndVisible = [8,]
		self.name = "Save_File"
		self.saveFile = "Untitled"
	def changePos(self,viewX,viewY):
		self.x = viewX
		self.y = viewY
	def draw(self,Window,viewX,viewY):
		self.x = viewX
		self.y = viewY
		pygame.draw.rect(Window,(100,100,100),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
		text = pygame.font.Font(None,16)
		Window.blit(text.render("Save",0,(0,0,0)),(0,4))