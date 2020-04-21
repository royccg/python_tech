from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys, math


class SignalSlotDemo(QWidget):
    def __init__(self):
        super(SignalSlotDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('信号（Signal）与槽（Slot）')
        self.setGeometry(300, 300, 500, 400)
        self.btn = QPushButton('我的按钮', self)
        self.btn.clicked.connect(self.onClick)

    def onClick(self):
        self.btn.setText('信号已经发出')
        self.btn.setStyleSheet('QPushButton(max-width:200px;min-width:200px)')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = SignalSlotDemo()
    main.show()
    sys.exit(app.exec_())
