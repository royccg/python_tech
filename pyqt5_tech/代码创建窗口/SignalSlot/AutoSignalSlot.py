from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
import sys

'''
信号与槽 自动连接
'''


class AutoSignalSlot(QWidget):
	def __init__(self):
		super(AutoSignalSlot, self).__init__()

		self.okButton =QPushButton('ok', self)
		self.okButton.setObjectName('okButton')

		self.okButton1 =QPushButton('cancel', self)
		self.okButton1.setObjectName('cancelButton')

		layout = QHBoxLayout()
		layout.addWidget(self.okButton)
		self.setLayout(layout)
		# self.okButton.clicked.connect(self.on_okButton_clicked)  # 原先的方式
		QtCore.QMetaObject.connectSlotsByName(self)

	@QtCore.pyqtSlot()  # 修饰一下
	def on_okButton_clicked(self):
		print('点击了OK按钮')

	@QtCore.pyqtSlot()  
	def on_cancelButton_clicked(self):
		print('点击了Cancel按钮')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = AutoSignalSlot()
    main.show()
    sys.exit(app.exec_())