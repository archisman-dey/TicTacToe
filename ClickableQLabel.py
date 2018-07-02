#implement a clickable QLabel used for showing the circle and crosses as a QPixelMap

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ClickableQLabel (QLabel):

	clicked = pyqtSignal()	#must be declared here, not inside init

	def __init__ (self, parent = None):
		super().__init__(parent)

	def mousePressEvent (self, event):
		self.clicked.emit()

	def mouseDoubleClickEvent (self, event):		
		self.clicked.emit()
