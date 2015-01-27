from Player import*
from Solid import*
import SolidPuzzle1
import SolidPuzzle2
import pygame
from pygame.locals import*
import py_compile
import os
import sys

class ObjectManager:
	def __init__(self):
		self.instance = [Player(5,5),Solid(2,2)]
		self.bg = (123,123,123)
		self.name = ["SolidPuzzle1","SolidPuzzle2"]
		self.directory = ["Game/SolidPuzzle1.py","Game/SolidPuzzle2.py"]
		self.tempDirectory = ["Temporary/SolidPuzzle1.py","Temporary/SolidPuzzle2.py"]
		self.maps = ["Game/Maps/TestMap.txt"]
		self.room = 0
		self.SP1 = SolidPuzzle1.SolidPuzzle1
		self.SP2 = SolidPuzzle2.SolidPuzzle2
		self.exit = False
		self.viewX = 0
		self.viewY = 0
		self.roomW = 0
		self.roomH = 0
	def setUpRoom(self):
		self.instance = []
		map = open(self.maps[self.room],'r')
		i = 0
		for line in map:
			if i == 0:
				self.roomW = (len(line)-1)*32
			for j in range(0,len(line)):
				if (line[j] == "P"):
					self.instance.append(Player(j,i))
				if (line[j] == "S"):
					self.instance.append(Solid(j,i))
			i += 1
		self.roomH = i*32
		if (self.room == 0):
			#self.instance.append(Player(1,1))
			self.instance.append(self.SP2(19,3))
			self.instance.append(self.SP1(45,10))
	def update(self,controlsPressed, controlsHold, mousePressed, mousePos, codingBar):
		for i in range(0,len(self.instance)):
			self.instance[i].update(controlsPressed,controlsHold)
			if self.instance[i].collision == "Full":
				for j in range(0,len(self.instance)):
					if self.instance[j].collision  == "Solid":
						self.instance[i].collideWithSolid(self.instance[j].x,self.instance[j].y,self.instance[j].xSpace*32,self.instance[j].ySpace*32)
			if (mousePressed and mousePos[0] >= self.instance[i].x-self.viewX and mousePos[0] < self.instance[i].x+self.instance[i].xSpace*32-self.viewX and mousePos[1] >= self.instance[i].y-self.viewY and mousePos[1] < self.instance[i].y+self.instance[i].ySpace*32-self.viewY):
				if (self.instance[i].name == ""):
					#Do nothing.
					codingBar.setString(codingBar.getString())
					codingBar.setName(codingBar.getName())
				else:
					codingBar.setName(self.instance[i].name)
					for j in range(0,len(self.name)):
						if (self.instance[i].name == self.name[j]):
							stri = []
							file = open(self.directory[j],'r')
							for line in file:
								tempStr = ""
								for k in range(0,len(line)-1): #Make it so \n does not appear!
									tempStr = tempStr+line[k]
								stri.append(tempStr)
							codingBar.setString(stri,self.instance[i].codingStartVisible,self.instance[i].codingEndVisible)
							file.close()
		for i in range(0,len(self.instance)):
			self.instance[i].finishUpdate()
			if (self.instance[i].name == "Player"):
				self.viewX = self.instance[i].x+16*self.instance[i].xSpace-320
				if (self.viewX < 0):
					self.viewX = 0
				elif (self.viewX > self.roomW-640):
					self.viewX = self.roomW-640
				self.viewY = self.instance[i].y+16*self.instance[i].ySpace-240
				if (self.viewY < 0):
					self.viewY = 0
				elif (self.viewY > self.roomH-480):
					self.viewY = self.roomH-480
	def setStrings(self,stri,name):
		#This is for setting the code of the other things.
		for i in range(0,len(self.name)):
			if (self.name[i] == name):
			        file = open(self.directory[i],'w')
			        for j in range(0,len(stri)):
			            file.write(stri[j]+"\n")
			        file.close()
			        try:
					py_compile.compile(self.directory[i],self.directory[i]+"c",self.directory[i],True)
					file = open(self.tempDirectory[i],'w')
					file2 = open(self.directory[i],'r')
					for line in file2:
						file.write(line)
					file.close()
					file2.close()
					fileWrite = open("save.txt",'w')
					fileWrite.write(str(self.room)+"\n")
					for j in range(0,len(self.instance)):
						if (self.instance[j].name == "Player"):
							fileWrite.write(str(self.instance[j].x)+"\n")
							fileWrite.write(str(self.instance[j].y)+"\n")
					fileWrite.write("1 ")
					sys.exit()
			        except py_compile.PyCompileError:
					#Have it so the Temporary Directory is the new directory
					file = open(tempDirectory[i],'r')
					file2 = open(directory[i],'w')
					for line in file:
					    file2.write(line)
					file.close()
					file2.close()
	def draw(self,Window):
		pygame.draw.rect(Window,self.bg,(0,0,640,480))
		for i in range(0,len(self.instance)):
			self.instance[i].draw(Window,self.viewX,self.viewY)