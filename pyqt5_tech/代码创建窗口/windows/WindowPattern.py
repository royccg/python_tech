"""
设置窗口的样式 （主要是窗口边框、标题栏以及窗口本身的特性）
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *

# print(QStyleFactory.keys())

class WindowPattern(QMainWindow):
	"""docstring for WindowPattern"""
	def __init__(self):
		super(WindowPattern, self).__init__()
		self.setWindowTitle('设置窗口的样式')
		self.resize(500, 260)
		#                                                   无边框  | 窗口一直在最前端                          
		self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.FramelessWindowHint  | Qt.WindowStaysOnTopHint)  
		self.setObjectName('MainWindow')
		self.setStyleSheet('#MainWindow{border-image:url(IMG_0180.JPG);}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = WindowPattern()
    main.show()
    sys.exit(app.exec_())		



