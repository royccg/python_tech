"""
窗口、绘图与特效：设计窗口风格
QApplication.setStyle(...)
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *

# print(QStyleFactory.keys())

class WindowStyle(QWidget):
	"""docstring for WindowStyle"""
	def __init__(self):
		super(WindowStyle, self).__init__()
		self.setWindowTitle('设置窗口风格')
		horizontalLayout = QHBoxLayout()
		self.styleLabel = QLabel('设置窗口风格')
		self.styleComboBox = QComboBox()
		self.styleComboBox.addItems(QStyleFactory.keys())

		# 获取当前窗口的风格
		# print(QApplication.style().objectName())
		index = self.styleComboBox.findText(QApplication.style().objectName(), QtCore.Qt.MatchFixedString)

		self.styleComboBox.setCurrentIndex(index)

		self.styleComboBox.activated[str].connect(self.handleStyleChanged)
		horizontalLayout.addWidget(self.styleLabel)
		horizontalLayout.addWidget(self.styleComboBox)
		self.setLayout(horizontalLayout)

	def handleStyleChanged(self, style):
		QApplication.setStyle(style)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = WindowStyle()
    main.show()
    sys.exit(app.exec_())		



