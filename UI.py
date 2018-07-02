#implements functions to control the UI of the game

import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ClickableQLabel import ClickableQLabel

class MainWindow (QMainWindow):

	def __init__ (self, parent = None):
		super().__init__(parent)	#this line initialises QMainWindow

		#pixmaps to be used later
		self.cross = self.crossPixmap()
		self.circle = self.circlePixmap()
		self.crossGreen = self.crossPixmapGreen()
		self.circleGreen = self.circlePixmapGreen()

		self.labels = [[], [], []] #this will store the 9 labels
		
		self.setupUI()
		self.show()

	def setupUI(self):
		self.setFixedSize(300, 300)		#revise later for using on other screen resolutions
		self.setWindowTitle("TicTacToe")
		self.setWindowIcon(QIcon('window_icon.png'))

		centralWidget = QWidget()
		self.setCentralWidget(centralWidget)

		grid = QGridLayout()
		centralWidget.setLayout(grid)

		#initialize the 9 labels and put them into a grid
		for i in (0,1,2):
			for j in (0,1,2):
				self.labels[i].append(self.setupLabel())
				grid.addWidget(self.labels[i][j], i, j)

	def setupLabel(self):
		label = ClickableQLabel(parent = self.centralWidget())

		#Alpha = 255 means no transparency
		backgroundColor = QColor(255, 213, 179, 255) #RGBA values

		pix = QPixmap(90, 90)
		pix.fill(backgroundColor)

		label.setPixmap(pix)
		return label

	def generatePix (self, filename):
		#loads a 90*90 pixmap from filename
		pix = QPixmap()
		pix.load(filename)
		pix = pix.scaled(90, 90)
		return pix

	def crossPixmap (self):
		return self.generatePix("Red-Cross.png")

	def circlePixmap (self):
		return self.generatePix("red-circle.png")

	def crossPixmapGreen (self):
		return self.generatePix("Red-Cross-Green.png")

	def circlePixmapGreen (self):
		return self.generatePix("red-circle-green.png")

	def updateLabel (self, x, y, type):
		if type == "cross" :
			self.labels[x][y].setPixmap(self.cross)
		elif type == "circle" :
			self.labels[x][y].setPixmap(self.circle)
		elif type == "gcross" :
			self.labels[x][y].setPixmap(self.crossGreen)
		elif type == "gcircle" :
			self.labels[x][y].setPixmap(self.circleGreen)

		self.show()
