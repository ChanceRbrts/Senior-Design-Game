from Instance import*
class SafeSpot(Instance):
	def __init__(self,oX=0,oY=0):
		Instance.__init__(self,oX,oY)
		self.color = [0,0,0]
		self.name = "Safe Spot"
		self.image = [pygame.image.load('Game/Sprites/WarningBlock/1.png'),
					  pygame.image.load('Game/Sprites/WarningBlock/2.png'),
					  pygame.image.load('Game/Sprites/WarningBlock/3.png'),
					  pygame.image.load('Game/Sprites/WarningBlock/4.png'),
					  pygame.image.load('Game/Sprites/WarningBlock/5.png'),
					  pygame.image.load('Game/Sprites/WarningBlock/6.png'),
					  pygame.image.load('Game/Sprites/WarningBlock/7.png'),
					  pygame.image.load('Game/Sprites/WarningBlock/8.png')]
		self.imageToDraw = 0
		
	def draw(self, Window, viewX, viewY):
		for i in range(0,self.xSpace):
			for j in range(0,self.ySpace):
				Window.blit(self.image[self.imageToDraw],(self.x-viewX+i*32,self.y-viewY+j*32))
		self.imageToDraw += 1
		if (self.imageToDraw > 7):
			self.imageToDraw = 0
		s = pygame.Surface((32*self.xSpace,32*self.ySpace))
		s.set_alpha(100)
		s.fill((self.color[0],self.color[1],self.color[2]))
		Window.blit(s, (self.x-viewX,self.y-viewY)) 
		#pygame.draw.rect(Window,(self.color[0],self.color[1],self.color[2],50),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))