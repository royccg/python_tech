
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys,math

class FillRect(QWidget):
    def __init__(self):
        super(FillRect, self).__init__()
        self.resize(600, 600)
        self.setWindowTitle('用画刷填充区域')

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)

        brush = QBrush(Qt.SolidPattern)  # 实心的模式
        qp.setBrush(brush)
        qp.drawRect(10, 15, 90, 60)

        brush = QBrush(Qt.Dense1Pattern)  #替换掉之前
        qp.setBrush(brush)
        qp.drawRect(130, 15, 90, 60)

        brush = QBrush(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 15, 90, 60)

        brush = QBrush(Qt.Dense3Pattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush = QBrush(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 105, 90, 60)
        qp.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = FillRect()
    main.show()

    sys.exit(app.exec_())
