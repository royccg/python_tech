from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class OverrideSlot(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Override (覆盖)槽函数')

	def keyPressEvent(self, e):
		if e.key() == Qt.Key_Escape:
			self.close()
		elif e.key() == Qt.Key_Alt:
			self.setWindowTitle('按下ALT键')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = OverrideSlot()
    main.show()
    sys.exit(app.exec_())