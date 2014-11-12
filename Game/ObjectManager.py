from Player import*
from Solid import*
from SolidPuzzle1 import*
import pygame
from pygame.locals import*
import py_compile
class ObjectManager:
	def __init__(self):
		self.instance = [Player(5,5),Solid(2,2)]
		self.bg = (123,123,123)
		self.name = ["SolidPuzzle1"]
		self.directory = ["SolidPuzzle1.py"]
		self.tempDirectory = ["../Temporary/SolidPuzzle1.py"]
        self.maps = ["Maps/TestMap"]
        self.room = 0
    def setupRoom():
        self.instance = []
        map = open(self.maps[self.room],'r')
        for i in range(0,len(map)):
            for j in range(0,len(map[i])):
                if (map[i][j] == "P"):
                    self.instance.append(Player(j,i))
                if (map[i][j] == "S"):
                    self.instance.append(Solid(j,i))
	def update(self,controlsPressed, controlsHold, mousePressed, mousePos, codingBar, viewX=0, viewY=0):
		for i in range(0,len(self.instance)):
			self.instance[i].update(controlsPressed,controlsHold)
			for j in range(0,len(self.instance)):
				if self.instance[j].collision  == "Solid":
					self.instance[i].collideWithSolid(self.instance[j].x,self.instance[j].y,self.instance[j].xSpace*32,self.instance[j].ySpace*32)
            if (mousePressed && mousePos[0] >= self.instance[i].x-viewX && mousePos[0] < self.instance[i].x+self.instance[i].xSpace*32-viewX
            		&& mousePos[2] >= self.instance[i].y-viewY && mousePos[1] < self.instance[i].y+self.instance[i].ySpace*32-viewY):
            	if (self.instance[i].name == ""):
            		#Do nothing.
            		codingBar.setString(codingBar.getString)
            		codingBar.setName(codingBar.getName)
            	else:
            		codingBar.setName(self.instance[i].name)
            		for j in range(0,len(self.name)):
            			if (self.instance[i].name = self.name[j]):
            				str = []
            				file = open(self.directory[j],'r')
							for line in file:
								tempStr = ""
								for k in range(0,len(line)-1): #Make it so \n does not appear!
									tempStr = tempStr+line[k]
								str.append(tempStr)
							codingBar.setString(str)
							file.close()
		for i in range(0,len(self.instance)):
			self.instance[i].finishUpdate()
	def draw(self,Window,viewX=0,viewY=0):
		pygame.draw.rect(Window,self.bg,(0,0,640,480))
		for i in range(0,len(self.instance)):
			self.instance[i].draw(Window,viewX,viewY)
    def setStrings(self,str,name):
        #This is for setting the code of the other things.
        for i in range(0,len(self.name)):
            if (self.name[i] == name):
                file = open(directory[i],'w')
                for j in range(0,len(str)):
                    file.write(str[j]+"\n")
                file.close()
                try:
                    py_compile.compile(self.directory[i],self.directory[i]+"c",self.directory[i],True)
                    if (self.name[i] == "SolidPuzzle1"):
                        from SolidPuzzle1 import*
                    file = open(tempDirectory[i],'w')
                    file2 = open(directory[i],'r')
                    for line in file2:
                        file.write(file2[line])
                    file.close()
                    file2.close
                except py_compile.PyCompileError:
                    #Have it so the Temporary Directory is the new directory
                    file = open(tempDirectory[i],'r')
                    file2 = open(directory[i],'w')
                    for line in file:
                        file2.write(file[line])
                    file.close()
                    file2.close()
