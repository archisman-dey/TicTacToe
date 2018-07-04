#implements functions used for controlling the UI

from PyQt5.QtGui import QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout
from ClickableQLabel import ClickableQLabel

winSize = 299	#change this to suit your screen resolution
labelSize = (int)(winSize*3/10)

class MainWindow (QMainWindow):

	def __init__ (self, parent = None):
		super().__init__(parent)	#this line initialises QMainWindow

		#pixmaps to be used later
		self.cross = self.generatePix("Red-Cross.png")
		self.circle = self.generatePix("red-circle.png")
		self.crossGreen = self.generatePix("Red-Cross-Green.png")
		self.circleGreen = self.generatePix("red-circle-green.png")

		self.labels = [[], [], []] #this will store the 9 labels
		
		self.setupUI()
		self.show()

	def setupUI(self):
		self.setFixedSize(winSize, winSize)		#revise later for using on HiDPI
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

		pix = QPixmap(labelSize, labelSize)
		pix.fill(backgroundColor)

		label.setPixmap(pix)
		return label

	def generatePix (self, filename):
		#loads a labelSize pixmap from filename
		pix = QPixmap()
		pix.load(filename)
		pix = pix.scaled(labelSize, labelSize)
		return pix

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
