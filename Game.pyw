#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication
from UI import MainWindow

class Game(object):
	def __init__(self):
		
		#this stores a 3X3 matrix with values "empty" or "cross" or "circle"
		self.matrix = [["empty"]*3 for i in range(3)]
		self.turn = 1	#turn = 1 means Player 1 and 2 means Player 2

		self.app = QApplication(sys.argv)
		self.game = MainWindow()

		#DONT CHANGE THIS WITH A SIMPLE FOR LOOP
		#using a lambda is how methods with additional arguments not
		#provided by the signal is called
		self.game.labels[0][0].clicked.connect(lambda : self.update(0, 0))
		self.game.labels[0][1].clicked.connect(lambda : self.update(0, 1))
		self.game.labels[0][2].clicked.connect(lambda : self.update(0, 2))
		self.game.labels[1][0].clicked.connect(lambda : self.update(1, 0))
		self.game.labels[1][1].clicked.connect(lambda : self.update(1, 1))
		self.game.labels[1][2].clicked.connect(lambda : self.update(1, 2))
		self.game.labels[2][0].clicked.connect(lambda : self.update(2, 0))
		self.game.labels[2][1].clicked.connect(lambda : self.update(2, 1))
		self.game.labels[2][2].clicked.connect(lambda : self.update(2, 2))

		self.app.exec_()

	def update(self, i, j):	#this is used as a slot
		#updates the matrix and the UI on click and also updates the
		#labels when the game is won
		if self.matrix[i][j] == "empty":
			if self.checkWinner() == False :
				if self.turn == 1:
					self.matrix[i][j] = "cross"
					self.game.updateLabel(i, j, "cross")
					self.turn = 2
				else :
					self.matrix[i][j] = "circle"
					self.game.updateLabel(i, j, "circle")
					self.turn = 1

				if self.checkWinner() != False:
					result = self.checkWinner()
					for i in (1,2,3):
						self.game.updateLabel(result[i][0], result[i][1], "g" + result[4])

	def checkWinner(self):
		#returns False if game is not won and a tuple 
		#(True, the three labels to be greenified and the type of label)
		#checking rows and columns:
		for i in (0,1,2):
			if self.matrix[i][0] == self.matrix[i][1] == self.matrix[i][2] != "empty":
				return (True, (i,0), (i,1), (i,2), self.matrix[i][0])
			elif self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] != "empty":
				return (True, (0,i), (1,i), (2,i), self.matrix[0][i])
		#checking diagonals
		if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] != "empty":
				return (True, (0,0), (1,1), (2,2), self.matrix[1][1])
		elif self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] != "empty":
				return (True, (0,2), (1,1), (2,0), self.matrix[1][1])
		
		#these should be more readable
		return False

Game()
