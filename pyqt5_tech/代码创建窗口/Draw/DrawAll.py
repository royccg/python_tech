
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys,math

class DrawAll(QWidget):
    def __init__(self):
        super(DrawAll, self).__init__()
        self.resize(300, 600)
        self.setWindowTitle('绘制各种图形')

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)

        pen = QPen(Qt.blue)
        qp.setPen(pen)

        # 绘制弧
        rect = QRect(0,10,100,100)  #设定绘制区域  初始坐标，宽，高
        # alen: 1 个alen 等于 1/16 度   45度 = 45* 16 alen
        qp.drawArc(rect, 0, 50*16)  # 初始角度   终止角度

        # 通过弧 绘制圆
        qp.setPen(Qt.red)
        qp.drawArc(120, 10, 100, 100, 0, 360*16)

        # 绘制带 弦的弧
        qp.drawChord(10, 120, 100, 100, 12, 130*16)

        # 绘制扇形
        qp.drawPie(10, 240, 100, 100, 12, 130*16)

        # 绘制椭圆
        qp.drawEllipse(120, 120, 150, 100)  # 宽和高不同

        # 绘制 5边形
        point1 = QPoint(140,380)
        point2 = QPoint(270,420)
        point3 = QPoint(290,512)
        point4 = QPoint(290,588)
        point5 = QPoint(200,533)

        polygon = QPolygon([point1, point2, point3, point4, point5])
        qp.drawPolygon(polygon)

        # 绘制图像
        image = QImage('icons-python.png')
        rect = QRect(10, 400, image.width()/0.2, image.height()/0.2)
        qp.drawImage(rect, image)
        # image.save('../image/icons-p.png')
        qp.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DrawAll()
    main.show()

    sys.exit(app.exec_())
