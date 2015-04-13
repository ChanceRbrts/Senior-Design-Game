#!/usr/bin/env python
from Instance import*
class Transporter(Instance):
	def __init__(self,oX=0,oY=0,room=0):
		Instance.__init__(self,oX,oY)
		self.room = room
		self.collision = "Transporter"
	def draw(self, Window, viewX, viewY):
		pygame.draw.rect(Window,(155,0,155),(self.x-viewX,self.y-viewY,self.xSpace*32,self.ySpace*32))
	
	

