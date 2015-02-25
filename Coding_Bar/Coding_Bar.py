import pygame
from pygame.locals import*
import sys
from os import walk
class Coding_Bar:
	def __init__(self):
		self.col = 0
		self.row = 0
		self.downCol = 0
		self.str = [""]
		self.realCode = [""]
		self.name = ""
		self.leftPressed = False
		self.rightPressed = False
		self.upPressed = False
		self.downPressed = False
		self.shift = False
		self.codeStarts = [0]
		self.codeEnds = [999999]
		self.keys = [K_TAB, K_SPACE, K_EXCLAIM, K_HASH, K_DOLLAR, K_AMPERSAND, K_QUOTE,
			K_LEFTPAREN, K_RIGHTPAREN, K_ASTERISK, K_PLUS, K_COMMA, K_MINUS, K_PERIOD,
			K_SLASH, K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_COLON, 
			K_SEMICOLON, K_LESS, K_EQUALS, K_GREATER, K_QUESTION, K_AT, K_LEFTBRACKET,
			K_RIGHTBRACKET, K_BACKSLASH, K_CARET, K_UNDERSCORE, K_BACKQUOTE, K_a, K_b,
			K_c, K_d, K_e, K_f, K_g, K_h, K_i, K_j, K_k, K_l, K_m, K_n, K_o, K_p, K_q,
			K_r, K_s, K_t, K_u, K_v, K_w, K_x, K_y, K_z, K_KP0, K_KP1, K_KP2, K_KP3,
			K_KP4, K_KP5, K_KP6, K_KP7, K_KP8, K_KP9, K_KP_PERIOD, K_KP_DIVIDE, 
			K_KP_MULTIPLY, K_KP_MINUS, K_KP_PLUS, K_KP_EQUALS] 
		self.lowerCase = ["\t", " ", "!", "#", "$", "&", "\'",
			"(", ")", "*", "+", ",", "-", ".",
			"/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":",
			";", "<", "=", ">", "?", "@", "[", 
			"]", "\\", "^", "_", "`", "a", "b",
			"c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
			"r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", 
			"4", "5", "6", "7", "8", "9", ".", "/",
			"*", "-", "+", "="]
		self.upperCase = ["\t", " ", "!", "#", "$", "&", "\"",
			"(", ")", "*", "+", "<", "_", ">", 
			"?", ")", "!", "@", "#", "$", "%", "^", "&", "*", "(", ":",
			":", "<", "+", ">", "?", "@", "{", 
			"}", "|", "^", "_", "~", "A", "B",
			"C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
			"R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3",
			"4", "5", "6", "7", "8", "9", ".", "/", 
			"*", "-", "+", "="]
		self.fileName = ""
	def setString(self,Set,codeStarts=[0],codeEnds=[999999]):
		self.realCode = Set
		settingString = []
		if (codeStarts[0] > 0):
			settingString.append("...")
		for i in range(0,len(codeStarts)):
			for line in range(codeStarts[i],codeEnds[i]):
				if (len(self.realCode) > line):
					settingString.append(self.realCode[line])
				else:
					break
			if (codeEnds[i] < 999999):
				settingString.append("...")
		self.codeStarts = codeStarts
		self.codeEnds = codeEnds
		self.str = settingString
	def getString(self):
		return(self.str)
	def setName(self,Set):
		self.fileName = Set
	def getName(self):
		return(self.fileName)
	def update(self, controlsPressed, controlsHold, mousePressed, mousePos, OBJMAN, rightedge):
		for i in range(0,len(controlsHold)):
		    if controlsHold[i] == K_RSHIFT or controlsHold[i] == K_LSHIFT:
		        self.shift = True
		for i in range(0,len(controlsPressed)):
			if controlsPressed[i] == K_LEFT:
				self.leftPressed = True
			if controlsPressed[i] == K_RIGHT:
				self.rightPressed = True
			if controlsPressed[i] == K_UP:
				self.upPressed = True
			if controlsPressed[i] == K_DOWN:
				self.downPressed = True
			if (controlsPressed[i] == K_LEFT) == False and (controlsPressed[i] == K_RIGHT) == False and (controlsPressed[i] == K_UP) == False and (controlsPressed[i] == K_DOWN) == False:
				if (controlsPressed[i] == K_RETURN or controlsPressed[i] == K_KP_ENTER):
					tempStr = ""
					tempStr2 = ""
					for j in range(0,self.col):
						tempStr += self.str[self.row][j]
					for j in range(self.col, len(self.str[self.row])):
						tempStr2 += self.str[self.row][j]
					self.str[self.row] = tempStr
					self.str.insert(self.row+1,tempStr2)
					self.row += 1
					self.col = 0
				elif controlsPressed[i] == K_BACKSPACE or controlsPressed[i] == K_DELETE:
					if self.col > 0:
						tempStr = ""
						for k in range(0,self.col-1):
							tempStr += self.str[self.row][k]
						for k in range(self.col,len(self.str[self.row])):
							tempStr += self.str[self.row][k]
						self.str[self.row] = tempStr
						self.col -= 1
					elif self.row > 0:
						tempStr = str[self.row]
						self.str.pop(self.row)
						self.row -= 1
						self.str[self.row] = self.str[self.row]+tempStr
				elif controlsPressed[i] is not K_RSHIFT and controlsPressed[i] is not K_LSHIFT:
					tempStr = ""
					moveTheCol = False
					for k in range(0,self.col):
						tempStr += self.str[self.row][k]
					for k in range(0,len(self.keys)):
						if (controlsPressed[i] == self.keys[k]):
							if (self.shift):
								tempStr += self.upperCase[k]
							else:
								tempStr += self.lowerCase[k]
							moveTheCol = True
					for k in range(self.col,len(self.str[self.row])):
						tempStr += self.str[self.row][k]
					if moveTheCol:
						self.col += 1
					self.str[self.row] = tempStr
		if self.leftPressed and not self.rightPressed:
			self.col -= 1;
			if (self.col < 0):
				if (self.row > 0):
					self.row -= 1
					self.col = len(self.str[self.row])
				else:
					self.col = 0
			self.downCol = self.col
		elif self.rightPressed and not self.leftPressed:
			self.col += 1;
			if self.col > len(self.str[self.row]):
				if self.row < len(self.str):
					self.row += 1
					self.col = 0
				else:
					self.col = len(self.str[self.row])
			self.downCol = self.col
		elif self.upPressed and not self.downPressed:
			self.row -= 1
			self.col = self.downCol
			if self.row < 0:
				self.row = 0
				self.col = 0
			if self.col > len(self.str[self.row]):
				self.col = len(self.str[self.row])
		elif self.downPressed and not self.upPressed:
			self.row += 1
			self.col = self.downCol
			if self.row > len(self.str)-1:
				self.row = len(self.str)-1
				self.col = len(self.str[self.row])
			if self.col > len(self.str[self.row]):
				self.col = len(self.str[self.row])
		self.leftPressed = False
		self.rightPressed = False
		self.upPressed = False
		self.downPressed = False
		self.shift = False
		if (mousePressed and mousePos[1] >= 450):
			strings = []
			codeStarts = [0]
			codeEnds = []
			currentCodeEnd = 0
			for i in range(0,len(self.str)):
				if (self.str[i] == "..."):
					if (i == 0):
						for i in range(0, self.codeStarts[0]):
							strings.append(self.realCode[i])
						codeStarts = [len(strings)]
					else:
						codeEnds.append(len(strings))
						if (currentCodeEnd+1 < len(self.codeEnds)):
							for i in range(self.codeEnds[currentCodeEnd],self.codeStarts[currentCodeEnd+1]):
								strings.append(self.realCode[i])
							codeStarts.append(len(strings))
						else:
							for i in range(self.codeEnds[currentCodeEnd],len(self.realCode)):
								strings.append(self.realCode[i])
						currentCodeEnd += 1
				else:
					strings.append(self.str[i])
			for i in range(0,len(strings)):
				#Concept
				if (strings[i][:25] == "\t\tself.codingStartVisible"):
					replaceStr = "\t\tself.codingStartVisible = ["
					for j in range(0,len(codeStarts)):
						replaceStr += str(codeStarts[j])
						replaceStr += ","
					replaceStr += "]"
					strings[i] = replaceStr
				if (strings[i][:23] == "\t\tself.codingEndVisible"):
					replaceStr = "\t\tself.codingEndVisible = ["
					for j in range(0,len(codeEnds)):
						replaceStr += str(codeEnds[j])
						replaceStr += ","
					replaceStr += "]"
					strings[i] = replaceStr
			OBJMAN.setStrings(strings,self.fileName)
		if (mousePressed and mousePos[0] >= rightedge-40 and mousePos[1] < 20):
			files = []
			for (dirpath, dirnames, filenames) in walk("Default/"):
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
					print files[i]
			fileWrite = open("save.txt",'w')
			fileWrite.write("0\n")
			fileWrite.write("-1\n")
			fileWrite.write("-1\n")
			fileWrite.write("1 ")
			fileWrite.close()
			sys.exit()
		elif (mousePressed and mousePos[0] >= rightedge-40 and mousePos[1] < 40):
				sys.exit()
	def draw(self,Window,rightedge):
		pygame.draw.rect(Window,(255,255,255),(640,0,rightedge-640,450))
		pygame.draw.rect(Window, (0,0,255),(640,440,rightedge-640,450))
		pygame.draw.rect(Window, (0,255,0),(rightedge-40,0,40,20))
		pygame.draw.rect(Window, (255,0,0),(rightedge-40,20,40,20))
		text = pygame.font.Font(None,16)
		Window.blit(text.render("Default",0,(0,0,0)),(rightedge-40,4))
		Window.blit(text.render("RESET",0,(0,0,0)),(rightedge-40,24))
		text = pygame.font.Font(None,32)
		Window.blit(text.render("COMPILE",0,(0,0,0)),(640+((rightedge-640)/2)-48,450))
		text = pygame.font.SysFont("monospace",12)
		pygame.draw.rect(Window, (0,0,0),(640+self.col*7,self.row*12,2,16))
		for i in range(0,len(self.str)):
			Window.blit(text.render(self.str[i],0,(0,0,0)),(640,i*12))
