#!/usr/bin/env python
from Solid import*
class ClassPuzzle3Block(Solid):
	def __init__(self,oX=0,oY=0,oW=1,oH=1):
		Solid.__init__(self,oX,oY,oW,oH)
		self.name = "ClassPuzzle3Block"
	def checkObjects(self,objects):
		if (len(objects) >= 10):
			self.x = 0
