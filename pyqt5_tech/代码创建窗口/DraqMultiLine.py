
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys,math

class DrawMultiLine(QWidget):
    def __init__(self):
        super(DrawMultiLine, self).__init__()
        self.resize(300, 300)
        self.setWindowTitle('设置Pen的样式')

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)

        pen = QPen(Qt.red, 3, Qt.SolidLine) # 实线
        painter.setPen(pen)
        painter.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine) # 虚线
        painter.setPen(pen) # 需要重新设置的
        painter.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotLine) # 点划线
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)  #坐标点


        pen.setStyle(Qt.DotLine) # 点线
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine) # 点点划线
        painter.setPen(pen)
        painter.drawLine(20, 200, 250, 200)

        # 使用自定义线
        pen.setStyle(Qt.CustomDashLine) # 使用自定义线
        pen.setDashPattern([1, 10, 5, 8])
        painter.setPen(pen)
        painter.drawLine(20, 240, 250, 240)

        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DrawMultiLine()
    main.show()

    sys.exit(app.exec_())
