import pygame
from pygame.locals import*
from Controls import*
from os import walk
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
OBJMAN.room = int(sys.argv[1])
OBJMAN.setUpRoom()
if (int(sys.argv[2]) > -1):
	for i in range(0,len(OBJMAN.instance)):
		if (OBJMAN.instance[i].name == "Player"):
			OBJMAN.instance[i].x = int(sys.argv[2])
			OBJMAN.instance[i].y = int(sys.argv[3])
#Get Everything back to Normal
while (gameLoop):
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			fileWrite = open('save.txt','w')
			fileWrite.write(str(OBJMAN.room)+"\n")
			for i in range(0,len(OBJMAN.instance)):
				if (OBJMAN.instance[i].name == "Player"):
					fileWrite.write(str(OBJMAN.instance[i].x)+"\n")
					fileWrite.write(str(OBJMAN.instance[i].y)+"\n")
			fileWrite.write("0 ")
			fileWrite.close()
			sys.exit()
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
		codingBar.update(controlsPressed, controlsHold,mousePressed, mousePos, OBJMAN, rightEdge)
	OBJMAN.draw(Window)
	codingBar.draw(Window,rightEdge)
	pygame.display.flip()
    #Finish the update
	controls.endFrame()
	nextFrame.tick(60)
