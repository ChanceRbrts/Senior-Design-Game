from Player import*
from Solid import*
from Door import*
import SolidPuzzle1
import SolidPuzzle2
import SolidPuzzle3
import SolidPuzzle3Assist
import TheirRacer
import YourRacer
import RaceAssist
import GenericMonster1
import ProjectilePuzzle
import ProjectileForPuzzle
import Conditional_Puzzle_1
import SafeSpot
import NotSafeSpot
import TintTheWalkway
import Laser_Catcher
import Laser
import Conditional_Puzzle_3
import Laser_Emitter
import Conditional_Puzzle_4
import Conditional_Puzzle_5
import DoorPart1
import Monster2
import CondPuzzle4Block
import Cond4Enemy
import For_Loops
import ForLoop1Square
import ForLoop1BlockMove
import ForLoop3
import Array_Puzzle
import TintTheWalkway2
import DNA_Puzzle
import FunctionPuzzle1
import FunctionPuzzle2
import FunctionPuzzle3
import FunctionPuzzle4
import FunctionPuzzle4Block
import RecursionPuzzle1
import RecursionPuzzle1Square
import RecursionPuzzle1BlockMove
import ClassPuzzle1
import ClassPuzzle2
import ClassPuzzle3
import ClassPuzzle3Block
import pygame
from pygame.locals import*
import py_compile
import os
import sys
import math
import random
import Save_File
import Load_File
import random

class ObjectManager:
		def __init__(self):
				self.instance = [Player(5,5),Solid(2,2)]
				self.bg = (123,123,123)
				self.name = ["SolidPuzzle1","SolidPuzzle2","SolidPuzzle3","YourRacer","ProjectilePuzzle",
							 "Conditional_Puzzle_1","TintTheWalkway","Laser_Emitter","Save_File","Load_File",
							 "Conditional_Puzzle_4","For_Loops","Array_Puzzle","TintTheWalkway2","ForLoop3",
							 "FunctionPuzzle1","FunctionPuzzle2","FunctionPuzzle3","FunctionPuzzle4","RecursionPuzzle1",
							 "ClassPuzzle1","ClassPuzzle2","Conditional_Puzzle_5","DNA_Puzzle","ClassPuzzle3"]
				self.directory = ["Game/SolidPuzzle1.py","Game/SolidPuzzle2.py","Game/SolidPuzzle3.py",
						  "Game/YourRacer.py","Game/ProjectilePuzzle.py","Game/Conditional_Puzzle_1.py",
						  "Game/TintTheWalkway.py","Game/Laser_Emitter.py","Game/Save_File.py",
						  "Game/Load_File.py","Game/Conditional_Puzzle_4.py","Game/For_Loops.py",
						  "Game/Array_Puzzle.py","Game/TintTheWalkway2.py","Game/ForLoop3.py",
						  "Game/FunctionPuzzle1.py","Game/FunctionPuzzle2.py","Game/FunctionPuzzle3.py",
						  "Game/FunctionPuzzle4.py","Game/RecursionPuzzle1.py","Game/ClassPuzzle1.py",
						  "Game/ClassPuzzle2.py","Game/Conditional_Puzzle_5.py","Game/DNA_Puzzle.py",
						  "Game/ClassPuzzle3.py"]
				self.tempDirectory = ["Temporary/SolidPuzzle1.py","Temporary/SolidPuzzle2.py","Temporary/SolidPuzzle3.py",
						      "Temporary/YourRacer.py","Temporary/ProjectilePuzzle.py","Temporary/Conditional_Puzzle_1.py",
						      "Temporary/TintTheWalkway.py","Temporary/Laser_Emitter.py","Temporary/Save_File.py",
						      "Temporary/Load_File.py","Temporary/Conditional_Puzzle_4.py","Temporary/For_Loops.py",
						      "Temporary/Array_Puzzle.py","Temporary/TintTheWalkway2.py","Temporary/ForLoop3.py",
							  "Temporary/FunctionPuzzle1.py","Temporary/FunctionPuzzle2.py","Temporary/FunctionPuzzle3.py",
							  "Temporary/FunctionPuzzle4.py","Temporary/RecursionPuzzle1.py","Temporary/ClassPuzzle1.py",
							  "Temporary/ClassPuzzle2.py","Temporary/Conditional_Puzzle_5.py","Temporary/DNA_Puzzle.py",
							  "Temporary/ClassPUzzle3.py"]
				self.maps = ["Game/Maps/TestMap.txt","Game/Maps/Conditionals.txt","Game/Maps/Loops.txt","Game/Maps/Functions.txt",
							 "Game/Maps/Classes.txt"]
				self.room = 0
				self.SP1 = SolidPuzzle1.SolidPuzzle1
				self.SP2 = SolidPuzzle2.SolidPuzzle2
				self.SP3 = SolidPuzzle3.SolidPuzzle3
				self.SP3A = SolidPuzzle3Assist.SolidPuzzle3Assist
				self.YR = YourRacer.YourRacer
				self.TR = TheirRacer.TheirRacer
				self.GM1 = GenericMonster1.GenericMonster1
				self.RA = RaceAssist.RaceAssist
				self.sDX = 0
				self.PP = ProjectilePuzzle.ProjectilePuzzle
				self.PFP = ProjectileForPuzzle.ProjectileForPuzzle
				self.CP1 = Conditional_Puzzle_1.Conditional_Puzzle_1
				self.SS = SafeSpot.SafeSpot
				self.NSS = NotSafeSpot.NotSafeSpot
				self.TTW = TintTheWalkway.TintTheWalkway
				self.LC = Laser_Catcher.Laser_Catcher
				self.L = Laser.Laser
				self.CP3 = Conditional_Puzzle_3.Conditional_Puzzle_3
				self.LE = Laser_Emitter.Laser_Emitter
				self.CP4 = Conditional_Puzzle_4.Conditional_Puzzle_4
				self.CP4B = CondPuzzle4Block.CondPuzzle4Block
				self.C4E = Cond4Enemy.Cond4Enemy
				self.CP5 = Conditional_Puzzle_5.Conditional_Puzzle_5
				self.DP1 = DoorPart1.DoorPart1
				self.DP2 = DoorPart1.DoorPart2
				self.M2 = Monster2.Monster2
				self.FL = For_Loops.For_Loops
				self.FL1S = ForLoop1Square.ForLoop1Square
				self.FL1BM = ForLoop1BlockMove.ForLoop1BlockMove
				self.AP = Array_Puzzle.Array_Puzzle
				self.FL3 = ForLoop3.ForLoop3
				self.TTW2 = TintTheWalkway2.TintTheWalkway2
				self.DNA = DNA_Puzzle.DNA_Puzzle
				self.FP1 = FunctionPuzzle1.FunctionPuzzle1
				self.FP2 = FunctionPuzzle2.FunctionPuzzle2
				self.FP3 = FunctionPuzzle3.FunctionPuzzle3
				self.FP4 = FunctionPuzzle4.FunctionPuzzle4
				self.FP4B = FunctionPuzzle4Block.FunctionPuzzle4Block
				self.RP1 = RecursionPuzzle1.RecursionPuzzle1
				self.RP1S = RecursionPuzzle1Square.RecursionPuzzle1Square
				self.RP1BM = RecursionPuzzle1BlockMove.RecursionPuzzle1BlockMove
				self.ClP1 = ClassPuzzle1.ClassPuzzle1
				self.ClP2 = ClassPuzzle2.ClassPuzzle2
				self.ClP3 = ClassPuzzle3.ClassPuzzle3
				self.ClP3B = ClassPuzzle3Block.ClassPuzzle3Block
				self.SF = Save_File.Save_File
				self.LF = Load_File.Load_File
				self.theRaces = True
				self.cheatTheRace = True
				self.hasNotBumped = True
				self.hasNotProjectiled = True
				self.exit = False
				self.oInstance = []
				self.sInstance = []
				self.sFInstance = []
				self.sSInstance = []
				self.viewX = 0
				self.viewY = 0
				self.roomW = 0
				self.roomH = 0
				self.numForCP3 = -1
				self.numForCP4 = -1
				self.numForCP5 = -1
				self.numForFP1 = -1
				self.goto = -1
				self.bgImage = pygame.image.load('Game/BGs/ForegroundishFade.png')
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
								if (self.room == 3 and j >= 57	and j < 72):
										self.sFInstance.append(Solid(j,i))	
								else:
										self.instance.append(Solid(j,i))
						if (j >= 40 and j < 57 and self.room == 1):
								if (line[j] == "0"):
										self.instance.append(self.NSS(j,i))
								if (line[j] == "1"):
										self.oInstance.append(self.SS(j,i))
						if (j >= 94 and j < 113 and self.room == 2):
								if (line[j] == "0"):
										self.sSInstance.append(self.NSS(j,i))
								if (line[j] == "1"):
										self.sSInstance.append(self.SS(j,i))
					i += 1
				self.roomH = i*32
				try:
						if (self.room == 0):
							#self.instance.append(Player(1,1))
								self.instance.append(self.SP2(19,3))
								self.instance.append(self.SP1(45,10))
								self.instance.append(self.SP3(62,8))
								self.instance.append(self.SP3A(77,8))
								self.instance.append(self.YR(92,5))
								self.instance.append(self.TR(92,9))
								self.instance.append(self.RA(108,5))
								self.instance.append(self.RA(108,9))
								for i in range(92,109):
									self.instance.append(self.GM1(i,1))
								for i in range(0,45):
										self.instance.append(self.PFP())
								self.instance.append(self.PP(127,5))
								self.instance.append(Transporter(141,5,1))
						if (self.room == 1):
								self.instance.append(self.CP1(5,5))
								self.instance.append(self.TTW(38,3))
								for i in range(len(self.instance)):
										if self.instance[i].name == "Not Safe Spot":
												self.instance[i] = self.instance[len(self.instance)-1].tint(self.instance[i])
								for i in range(len(self.oInstance)):
										if self.oInstance[i].name == "Safe Spot":
												self.oInstance[i] = self.instance[len(self.instance)-1].tint(self.oInstance[i])
								self.numForCP3 = len(self.instance)
								self.instance.append(self.LE(89,7))
								self.instance.append(self.L(89,8))
								self.instance.append(self.LC(89,14))
								self.instance.append(self.CP3(96,7))
								self.numForCP4 = len(self.instance)
								self.instance.append(self.CP4(108,5))
								self.instance.append(self.CP4B(117,3))
								self.instance.append(self.C4E(117,0))
								self.numForCP5 = len(self.instance)
								self.instance.append(self.CP5(150,10))
								self.instance.append(Transporter(-1,-1,2))
								self.instance.append(self.DP1(150,11))
								self.instance.append(self.DP2(150,13))
								self.instance.append(self.M2(150,12))
								self.instance.append(self.M2(150,14))
						if (self.room == 2):
								self.bg = (0,0,255)
								self.numForFP1 = len(self.instance)
								self.instance.append(self.FL(10,5))
								self.instance[len(self.instance)-1].doTheForLoop()
								self.instance[len(self.instance)-1].correctThisObject()
								self.instance.append(self.FL1S(18,5))
								self.instance.append(self.FL1BM(19,11))
								self.instance.append(self.AP(45,7))
								for i in range(0,15):
										self.sInstance.append(Solid(57,i))
								self.instance[len(self.instance)-1].checkSolid(self.sInstance)
								for i in range(0,len(self.sInstance)):
										self.instance.append(self.sInstance[i])
								self.instance.append(self.TTW2(90,8))
								self.sSInstace = self.instance[len(self.instance)-1].tint(self.sSInstance)
								for i in range(0,len(self.sSInstance)):
										if (self.sSInstance[i].name == "Safe Spot"):
												self.oInstance.append(self.sSInstance[i])
										if (self.sSInstance[i].name == "Not Safe Spot"):
												self.instance.append(self.sSInstance[i])
								self.instance.append(self.FL3(87,9))
								stri = self.instance[len(self.instance)-1].whileString()
								os.system("say "+stri)
								if (stri == "AAAAAAAAAAAAAAAA"):
										self.instance[len(self.instance)-1].x = 0
								self.instance.append(self.DNA(139,7))
								dnaStrand = ""
								for i in range(0,random.randrange(1,10)):
										dnaStrand += random.choice(["A","T","C","G"])
								checkStrand = self.instance[len(self.instance)-1].getDNAStrand(dnaStrand)
								newDNAStrand = ""
								for i in range(0,len(dnaStrand)):
										if (dnaStrand[i] == "A"):
												newDNAStrand += "T"
										if (dnaStrand[i] == "T"):
												newDNAStrand += "A"
										if (dnaStrand[i] == "C"):
												newDNAStrand += "G"
										if (dnaStrand[i] == "G"):
												newDNAStrand += "C"
								if checkStrand == newDNAStrand:
										self.instance[len(self.instance)-1].x = 0
								self.instance.append(Transporter(140,7,3))
						if (self.room == 3):
								self.bg = (0,255,100)
								self.instance.append(self.FP1(19,7))
								self.instance.append(Solid(48,6))
								self.instance.append(self.FP2(37,8))
								self.instance[len(self.instance)-2] = self.instance[len(self.instance)-1].function(self.instance[len(self.instance)-2])
								xS = []
								yS = []
								for i in range(0,len(self.sFInstance)):
										xS.append(self.sFInstance[i].x-57*32)
										yS.append(self.sFInstance[i].y)
								self.instance.append(self.FP3(56,5))
								b = self.instance[len(self.instance)-1].moveSolidObjects(xS,yS)
								xS = b[0]
								yS = b[1]
								for i in range(0,len(self.sFInstance)):
										self.sFInstance[i].x = xS[i]+57*32
										self.sFInstance[i].y = yS[i]
										self.instance.append(self.sFInstance[i])
								self.instance.append(self.FP4(86,3))
								self.instance.append(self.FP4B(90,7))
								self.instance[len(self.instance)-1].verifyValue(self.instance[len(self.instance)-2].valueForOtherObject(0))
								self.instance.append(self.RP1S(107,1))
								self.instance.append(self.RP1(100,1))
								self.instance.append(self.RP1BM(106,13))
								self.instance[len(self.instance)-2].recursion(self.instance[len(self.instance)-3])
								tmpI = self.instance[len(self.instance)-2]
								self.instance[len(self.instance)-1].check(self.instance[len(self.instance)-3].isInstanceCollide(tmpI.x,tmpI.y,tmpI.xSpace*32,tmpI.ySpace*32))
								self.instance.append(Transporter(108,13,4))
						if (self.room == 4):
								self.bg = (255,100,0)
								self.instance.append(self.ClP1(11,14))
								self.instance.append(self.ClP2(19,21))
								self.instance[len(self.instance)-1].checkType()
								self.instance.append(self.ClP3(30,20))
								self.instance.append(self.ClP3B(31,15))
								self.instance[len(self.instance)-1].checkObjects(self.instance[len(self.instance)-2].objects)
				except Exception:
						self.backToTemp()
				self.instance.append(self.SF())
				self.instance.append(self.LF())
				
				
				
		
		def update(self,controlsPressed, controlsHold, mousePressed, mousePos, codingBar):
				self.goto = -1
				try:
						for i in range(0,len(self.instance)):
								if (self.instance[i].name == "Save_File" or self.instance[i].name == "Load_File"):
										self.instance[i].changePos(self.viewX,self.viewY)
								if (self.instance[i].name == "Conditional_Puzzle_1"):
										self.instance[i].ifStatement(self.instance)
								if (self.instance[i].name == "SolidPuzzle3Assist"):
									for j in range(0,len(self.instance)):
										if (self.instance[j].name == "SolidPuzzle3"):
											self.instance[i].update(self.instance[j].x,self.instance[j].y,self.instance[j].xSpace,
														self.instance[j].ySpace,self.instance[j].dX,self.instance[j].ramEverythingDown)
								elif (self.instance[i].name == "RaceAssist" and self.theRaces):
									for j in range(0,len(self.instance)):
											a = self.instance[i].update(self.instance[j].x,self.instance[j].y,self.instance[j].xSpace,
														self.instance[j].ySpace,self.instance[j].dX,self.instance[j].name)
											if (a == 2):
												self.theRaces = False
											elif (a == 1):
												for k in range(0,len(self.instance)):
													if (self.instance[k].name == "GenericMonster1"):
														self.instance[k].dY = 4
								elif (self.instance[i].name == "TheirRacer" and self.cheatTheRace):
									for j in range(0,len(self.instance)):
											if (self.instance[j].name == "YourRacer" and self.instance[j].dX > 0):	
												self.instance[i].dX = self.instance[j].dX+2
												self.cheatTheRace = False
								elif (self.instance[i].name == "ProjectilePuzzle" and self.hasNotBumped):
										for j in range(0,len(self.instance)):
												if (self.instance[j].name == "Player"):
														if (self.instance[j].x+self.instance[j].dX+self.instance[j].xSpace*32 >= self.instance[i].x and self.instance[j].x+self.instance[j].xSpace*32 < self.instance[i].x
															and self.instance[j].y+self.instance[j].dY <= self.instance[i].y+self.instance[i].ySpace*32 and self.instance[j].y+self.instance[j].dY+self.instance[j].ySpace*32 >= self.instance[i].y):
																self.instance[i].dX = 8
																self.hasNotBumped = False
								elif (self.instance[i].name == "ProjectilePuzzle" and self.hasNotProjectiled):
										for j in range(0,len(self.instance)):
												if (self.instance[j].name == "Solid"):
														if (self.instance[i].x+self.instance[i].dX+self.instance[i].xSpace*32 >= self.instance[j].x and self.instance[i].x+self.instance[i].xSpace*32 < self.instance[j].x
															and self.instance[i].y+self.instance[i].dY <= self.instance[j].y+self.instance[j].ySpace*32 and self.instance[i].y+self.instance[i].dY+self.instance[i].ySpace*32 >= self.instance[j].y):
																degrees = 0
																for k in range(0,len(self.instance)):
																		if (self.instance[k].name == "Projec"):
																				self.instance[k] = self.PFP(self.instance[i].x/32,self.instance[i].y/32,
																						math.cos(degrees*math.pi/180.0)*4.0,math.sin(degrees*math.pi/180.0)*4.0,self.instance[i].radius,self.instance[i].projType)
																				degrees += 8
																
																self.hasNotProjectiled = False
								elif (self.instance[i].name == "Harmful"):
										for j in range(0,len(self.instance)):
												if (self.instance[j].name == "Solid"):
														if (math.fabs(self.instance[j].x-self.instance[i].x) < 64):
																x = self.instance[i].x
																y = self.instance[i].y
																dX = self.instance[i].dX
																dY = self.instance[i].dY
																xSpace = self.instance[i].xSpace
																ySpace = self.instance[i].ySpace
																oX = self.instance[j].x
																oY = self.instance[j].y
																oDX = self.instance[j].dX
																oDY = self.instance[j].dY
																oW = self.instance[j].xSpace*32
																oH = self.instance[j].ySpace*32
																if ((x+dX < oX+oW and x+xSpace*32+dX > oX and
																		y+dY+ySpace*32 > oY and y+ySpace*32 <= oY)
																		or (x+dX < oX+oW and x+xSpace*32+dX > oX and
																				y+dY < oY+oH and y >= oY+oH)
																		or (y+dY < oY+oH and y+ySpace*32+dY > oY and
																				x+dX+xSpace*32 > oX and x+xSpace*32 <= oX)
																		or (y+dY < oY+oH and y+ySpace*32+dY > oY and
																				x+dX < oX+oW and x >= oX+oW)):
																		self.instance[j].x = -64;
										self.instance[i].update(controlsPressed,controlsHold)
								elif (i > self.numForCP5 and i < self.numForCP5+5) and self.numForCP5 > 0 and self.viewX > 4160:
										pass
								else:
									self.instance[i].update(controlsPressed,controlsHold)
								if i == self.numForCP3:
										self.instance[i].setEmit(self.instance[i+2].caught)
										self.instance[i+1].getActivate(self.instance[i].getEmit())
										a = self.instance[i+2].checkTheLaser(self.instance[i])
										self.instance[i+3].getYPosition(a)
								if i == self.numForCP4:
										self.instance[i+1].getPos(self.instance[i].getPos(self.instance[i+2].pos))
										if (self.instance[i+1].isInstanceCollide(self.instance[i+2].x,self.instance[i+2].y,
																				 self.instance[i+2].xSpace*32,self.instance[i+2].ySpace*32)):
												self.instance[i+2].restartPos()
								if i == self.numForCP5:
										if (self.instance[i+2].y == 256 and self.instance[i+3].y == 256):
												self.instance[i+1].x = 4800
												self.instance[i+1].y = 256
								if ((i >= self.numForCP5+1 and i <= self.numForCP5+5) and self.numForCP5 > 0 and self.viewX > 4160):
										arrayO = self.instance[self.numForCP5].collideWithSolid(self.instance[i].x, self.instance[i].y, self.instance[i].xSpace*32, self.instance[i].ySpace*32, self.instance[i].dX, self.instance[i].dY, self.instance[i].name)
										self.instance[i].x = arrayO[0]
										self.instance[i].y = arrayO[1]
										self.instance[i].dX = arrayO[2]
										self.instance[i].dY = arrayO[3]
								if i == self.numForFP1:
										self.instance[i+2].check(self.instance[i+1].isInstanceCollide(self.instance[i].x,self.instance[i].y,self.instance[i].xSpace*32,self.instance[i].ySpace*32))
								if self.instance[i].collision == "Full":
									for j in range(0,len(self.instance)):
										if self.instance[j].collision  == "Solid":
											self.instance[i].collideWithSolid(self.instance[j].x,self.instance[j].y,self.instance[j].xSpace*32,self.instance[j].ySpace*32,self.instance[j].dX,self.instance[j].dY,self.instance)
										if self.instance[j].collision == "Monster" and self.instance[i].name == "Player":
											if (self.instance[i].collideWithMonster(self.instance[j].x,self.instance[j].y,self.instance[j].xSpace*32,self.instance[j].ySpace*32,self.instance[j].dX,self.instance[j].dY)):
												sys.exit()
										if self.instance[j].collision == "Transporter" and self.instance[i].name == "Player":
												if (self.instance[i].collideWithMonster(self.instance[j].x,self.instance[j].y,self.instance[j].xSpace*32,self.instance[j].ySpace*32)):
														self.room = self.instance[j].room
														self.goto = 0
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
				except Exception:
						self.backToTemp()
				if (self.goto > -1):
						self.setUpRoom()
				self.goto = -1
		def setStrings(self,stri,name):
				#This is for setting the code of the other things.
				for i in range(0,len(self.name)):
						if (self.name[i] == name and name != "Save_File" and name != "Load_File"):
								file = open(self.directory[i],'w')
								for j in range(0,len(stri)):
										file.write(stri[j]+"\n")
								file.close()
								try:
										py_compile.compile(self.directory[i],self.directory[i]+"c",self.directory[i],True)
										tempStr = ""
										for j in range(0,len(self.tempDirectory[i])):
												if (self.tempDirectory[i][j] == '/'):
														tempStr += '2/'
												else:
														tempStr += self.tempDirectory[i][j]
										file = open(self.tempDirectory[i],'r')
										file2 = open(tempStr,'w')
										for line in file:
												file2.write(line)
										file.close()
										file2.close()
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
										file = open(self.tempDirectory[i],'r')
										file2 = open(self.directory[i],'w')
										for line in file:
										    file2.write(line)
										file.close()
										file2.close()
						elif (self.name[i] == name and name == "Save_File"):
								savFile = ""
								for line in open(self.tempDirectory[i],'r'):
										run = 0
										for j in range(0,len(line)):
												if (line[j:j+13] == "self.saveFile" and run == 0):
														run = 1
												if (run == 1 and line[j] == "\""):
														run = 2
												elif (run == 2):
														if (line[j] == "\""):
																run = 3
														else:
																savFile += line[j]
								if (savFile == ""):
										savFile = "GenericSaveFile"
								if not os.path.exists(savFile+"/"):
										os.makedirs(savFile+"/")
								for j in range(0,len(self.tempDirectory)):
										file = open(self.tempDirectory[j],'r')
										file2 = open(savFile+"/"+self.tempDirectory[j][10:],'w')
										for line in file:
												file2.write(line)
										file.close()
										file2.close()
								savOpen = open("save.txt","r")
								savWrite = open(savFile+"/save.txt","w")
								for line in savOpen:
										savWrite.write(line)
								savOpen.close()
								savWrite.close()
						elif (self.name[i] == name and name == "Load_File"):
								loaFile = ""
								for line in open(self.tempDirectory[i],'r'):
										run = 0
										for j in range(0,len(line)):
												if (line[j:j+13] == "self.loadFile" and run == 0):
														run = 1
												if (run == 1 and line[j] == "\""):
														run = 2
												elif (run == 2):
														if (line[j] == "\""):
																run = 3
														else:
																loaFile += line[j]
								if (loaFile == ""):
										loaFile = "GenericSaveFile"
								if os.path.exists(loaFile+"/"):
										for j in range(0,len(self.tempDirectory)):
												tempDir = open(self.tempDirectory[j],'w')
												gameDir = open(self.directory[j],'w')
												readDir = open(loaFile+"/"+self.tempDirectory[j][10:],'r')
												for line in readDir:
														tempDir.write(line)
														gameDir.write(line)
												tempDir.close()
												gameDir.close()
												readDir.close()
												py_compile.compile(self.directory[j],self.directory[j]+"c",self.directory[j],True)
										savOpen = open(loaFile+"/save.txt","r")
										savWrite = open("save.txt","w")
										for line in savOpen:
												savWrite.write(line)
										savOpen.close()
										savWrite.close()
										sys.exit()
								else:
										print("The save file " + loaFile + " does not exist.")
		def backToTemp(self):
				for i in range(0,len(self.tempDirectory)):
						tempStr = ""
						for j in range(0,len(self.tempDirectory[i])):
								if (self.tempDirectory[i][j] == '/'):
										tempStr += '2/'
								else:
										tempStr += self.tempDirectory[i][j]
						tempDir = open(tempStr,'r')
						gameDir = open(self.directory[i],'w')
						gameDir2 = open(self.tempDirectory[i],'w')
						for line in tempDir:
								gameDir.write(line)
								gameDir2.write(line)
						gameDir.close()
						gameDir2.close()
						tempDir.close()
				sys.exit()
						
				
		
		def draw(self,Window):
				pygame.draw.rect(Window,self.bg,(0,0,640,480))
				Window.blit(self.bgImage,(0,0))
				for i in range(0,len(self.oInstance)):
						if (self.oInstance[i].x-self.viewX > -self.oInstance[i].xSpace*32
							and self.oInstance[i].x-self.viewX < 640
							and self.oInstance[i].y-self.viewY > -self.oInstance[i].ySpace*32
							and self.oInstance[i].y-self.viewY < 480):
								self.oInstance[i].draw(Window,self.viewX,self.viewY)
				for i in range(0,len(self.instance)):
						if (self.instance[i].x-self.viewX > -self.instance[i].xSpace*32
							and self.instance[i].x-self.viewX < 640
							and self.instance[i].y-self.viewY > -self.instance[i].ySpace*32
							and self.instance[i].y-self.viewY < 480):
								self.instance[i].draw(Window,self.viewX,self.viewY)