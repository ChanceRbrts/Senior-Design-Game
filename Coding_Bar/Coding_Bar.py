import pygame
from pygame.locals import*
class Coding_Bar:
	def __init__(self):
		self.col = 0
		self.row = 0
		self.downCol = 0
		self.str = [""]
		self.name = ""
		self.leftPressed = False
		self.rightPressed = False
		self.upPressed = False
		self.downPressed = False
		self.shift = False
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
	def setString(self, Set):
		self.str = Set
	def getString(self):
		return(self.str)
	def setName(self, Set):
		self.fileName = Set
	def getName(self):
		return(self.fileName)
	def update(self, controlsPressed, controlsHold, mousePressed, mousePos, OBJMAN):
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
			if self.col > len(self.str[self.row])-1:
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
			OBJMAN.setStrings(self.str,self.fileName)
	def draw(self,Window,rightedge):
		pygame.draw.rect(Window,(255,255,255),(640,0,rightedge-640,450))
		pygame.draw.rect(Window, (0,0,255),(640,440,rightedge-640,450))
		text = pygame.font.Font(None,32)
		Window.blit(text.render("COMPILE",0,(0,0,0)),(640+((rightedge-640)/2)-48,450))
		text = pygame.font.Font(None,16)
		for i in range(0,len(self.str)):
			Window.blit(text.render(self.str[i],0,(0,0,0)),(640,i*12))
