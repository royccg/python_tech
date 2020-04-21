from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys, math


class Splitter(QWidget):
    def __init__(self):
        super(Splitter, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSplitter 例子')
        self.setGeometry(300, 300, 300, 200)

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 =QSplitter(Qt.Horizontal)
        textEdit = QTextEdit()
        splitter1.addWidget(topleft)
        splitter1.addWidget(textEdit)
        splitter1.setSizes([200, 100])

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox =QHBoxLayout(self)
        hbox.addWidget(splitter2)
        self.setLayout(hbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Splitter()
    main.show()
    sys.exit(app.exec_())
