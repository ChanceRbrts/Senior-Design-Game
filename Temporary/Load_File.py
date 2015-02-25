from Instance import*
class Load_File(Instance):
	def __init__(self,oX=0,oY=0):
		Instance.__init__(self)
		self.codingStartVisible = [7,]
		self.codingEndVisible = [8,]
		self.name = "Load_File"
		self.loadFile = "Untitled"
	def changePos(self,viewX,viewY):
		self.x = viewX
		self.y = viewY+32
	def draw(self,Window,viewX,viewY):
		self.x = viewX
		self.y = viewY+32
		pygame.draw.rect(Window,(0,120,100),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
		text = pygame.font.Font(None,16)
		Window.blit(text.render("Load",0,(0,0,0)),(0,36))