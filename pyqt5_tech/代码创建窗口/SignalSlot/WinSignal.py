from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class WinSignal(QWidget):
	button_clicked_signal = pyqtSignal()

	def __init__(self):
		super().__init__()
		self.setWindowTitle('为窗口类添加信号')
		self.resize(300, 100)

		btn =QPushButton('关闭窗口', self)

		btn.clicked.connect(self.btn_clicked)

		self.button_clicked_signal.connect(self.btn_close)

	def btn_clicked(self):
		self.button_clicked_signal.emit()
		# print('1')

	def btn_close(self):
		self.close()
		# print('2')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = WinSignal()
    main.show()

    sys.exit(app.exec_())