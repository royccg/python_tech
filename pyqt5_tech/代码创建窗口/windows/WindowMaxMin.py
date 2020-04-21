"""
设置窗口的样式 （主要是窗口边框、标题栏以及窗口本身的特性）
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *


class WindowMaxMin(QWidget):
	"""docstring for WindowMaxMin"""
	def __init__(self, parent= None):
		super(WindowMaxMin, self).__init__(parent)
		self.setWindowTitle('用代码控制窗口的最大化和最小化')
		self.resize(300, 400)
		#                                                                            
		self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)  

		layout = QVBoxLayout()
		maxButton1 = QPushButton()
		maxButton1.setText('窗口最大化1')
		maxButton1.clicked.connect(self.maximized1)

		maxButton2 = QPushButton()
		maxButton2.setText('窗口最大化2')
		maxButton2.clicked.connect(self.showMaximized)  # 直接用内置函数

		minButton = QPushButton()
		minButton.setText('窗口最小化')
		minButton.clicked.connect(self.showMinimized)	

		layout.addWidget(maxButton1)
		layout.addWidget(maxButton2)
		layout.addWidget(minButton)
		self.setLayout(layout)

	def	maximized1(self):
		
		desktop = QApplication.desktop() # 获取桌面尺寸
		rect = desktop.availableGeometry() # 获取桌面可用尺寸

		# 设定程序尺寸 ：最大化
		self.setGeometry(rect)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = WindowMaxMin()
    main.show()
    sys.exit(app.exec_())		



