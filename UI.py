#implements functions to control the UI of the game

from PyQt5.QtGui import QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout
from ClickableQLabel import ClickableQLabel

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
		self.setFixedSize(300, 300)		#change for using on other screen resolutions
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
