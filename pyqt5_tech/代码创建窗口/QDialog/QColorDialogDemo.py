import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QColorDialog Demo')
        layout =QVBoxLayout()
        # 设置文本颜色
        self.colorButton1 = QPushButton('设置文字颜色')
        self.colorButton1.clicked.connect(self.getColor)
        layout.addWidget(self.colorButton1)
        # 设置文字背景色
        self.colorButton2 = QPushButton('设置背景色')
        self.colorButton2.clicked.connect(self.getBGColor)
        layout.addWidget(self.colorButton2)

        self.colorLabel = QLabel('Hello，测试字体颜色')
        layout.addWidget(self.colorLabel)

        self.setLayout(layout)
    # 设置文字颜色
    def getColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.WindowText,color)
        self.colorLabel.setPalette(p)
    # 设置文字背景色
    def getBGColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window,color)
        self.colorLabel.setAutoFillBackground(True)
        self.colorLabel.setPalette(p)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = QColorDialogDemo()
    main.show()

    sys.exit(app.exec_())
