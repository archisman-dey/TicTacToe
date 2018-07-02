#implement a clickable QLabel used for showing the circle and crosses as a QPixelMap

import PyQt5.QtCore
from PyQt5.QtWidgets import QLabel

class ClickableQLabel (QLabel):

	clicked = PyQt5.QtCore.pyqtSignal()	#must be declared here, not inside init

	def __init__ (self, parent = None):
		super().__init__(parent)

	def mousePressEvent (self, event):
		self.clicked.emit()

	def mouseDoubleClickEvent (self, event):		
		self.clicked.emit()
