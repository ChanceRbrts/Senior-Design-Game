import pygame
from pygame.locals import*
from Controls import*
from os import walk
files = []
'''for (dirpath, dirnames, filenames) in walk("Default/"):
	files.extend(filenames)
	break
for i in range(0,len(files)):
	fileOpen = open("Default/"+files[i],'r')
	tempStr = ""
	for j in range(8,len(files[i])):
		tempStr += files[i][j]
	tempStr = files[i]
	try:
		fileWrite = open("Game/"+files[i],'w')
		for line in fileOpen:
			fileWrite.write(line)
		fileWrite.close()
		fileOpen.close()
	except IOError:
		print files[i]'''
from Game.ObjectManager import*
from Coding_Bar.Coding_Bar import*
import thread
import sys
import time
pygame.init()
nextFrame = pygame.time.Clock()
rightEdge = 1020
screenUpdate = True
Window = pygame.display.set_mode((rightEdge,480))
pygame.display.set_caption("Project Code")
controls = Controls()
controlsPressed = []
controlsHold = []
codingBar = Coding_Bar()
codingBar.setString([""]);
mousePressed = False
mousePos = False
gameLoop = True
OBJMAN = ObjectManager()
OBJMAN.setUpRoom()
#Get Everything back to Normal
while (gameLoop):
	for e in pygame.event.get():
		controls.controlEvents(e)
	controlsPressed = controls.getControlsPressed()
	controlsHold = controls.getControlsHold()
	mousePos = controls.getMousePos()
	mousePressed = controls.getMousePressed()
	#Do a bunch of updating stuff in here...
	if (mousePressed):
		if (mousePos[0] < 640):
			screenUpdate = True
		else:
			screenUpdate = False
	if (screenUpdate):
		OBJMAN.update(controlsPressed,controlsHold, mousePressed, mousePos, codingBar)
	else:
		codingBar.update(controlsPressed, controlsHold,mousePressed, mousePos, OBJMAN)
	OBJMAN.draw(Window)
	codingBar.draw(Window,rightEdge)
	pygame.display.flip()
    #Finish the update
	controls.endFrame()
	nextFrame.tick(60)
