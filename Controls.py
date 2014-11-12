import pygame
import pygame.mouse
import pygame.event
from pygame.locals import*
class Controls:
	def __init__(self):
		self.controlsPressed = []
		self.controlsHold = []
		self.mousePos = []
		self.mousePressed = False
	def controlEvents(self, e):
		if e.type == KEYDOWN:
			self.controlsPressed.append(e.key)
			self.controlsHold.append(e.key)
		if e.type == KEYUP:
			copyList = self.controlsHold
			copy = 0
		 	for i in range(0,len(self.controlsHold)):
				if (len(self.controlsHold) > i):
					if (self.controlsHold[i] == e.key):
						copyList.remove(e.key)
			self.controlsHold = copyList
		if e.type == MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0] == True:
				self.mousePressed = True
				self.mousePos = pygame.mouse.get_pos()
	def endFrame(self):
		self.controlsPressed = []
		self.mousePressed = False
	def getControlsPressed(self):
		return(self.controlsPressed)
	def getControlsHold(self):
		return(self.controlsHold)
	def getMousePos(self):
		return(self.mousePos)
	def getMousePressed(self):
		return(self.mousePressed)
