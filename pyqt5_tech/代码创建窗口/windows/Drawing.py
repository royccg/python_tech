"""
项目实战 ：实现绘图应用

需要解决三个核心内容
1.如何绘图
	在paintEvent方法中绘图，通过调用update方法paintEvent的调用

2.在哪里绘图
	在白色背景的QPixmap对象中绘图
3.如何通过移动鼠标绘图
	鼠标拥有3个事件：
		（1）鼠标按下: mousePressEvent
		（2）鼠标移动: mouseMoveEvent
		（3）鼠标抬起: mouseReleaseEvent

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPixmap


class Drawing(QWidget):
	"""docstring for Drawing"""
	def __init__(self, parent= None):
		super(Drawing, self).__init__(parent)
		self.setWindowTitle('绘图应用')
		self.pix = QPixmap()
		self.lastPoint = QPoint()
		self.endPoint = QPoint()

		self.initUI()

	def initUI(self):
		self.resize(600, 600)
		# 画布大小为400*400, 背景为白色
		self.pix = QPixmap(600, 600)
		self.pix.fill(Qt.white)

	def paintEvent(self, event):
		pp = QPainter(self.pix)
		# 根据鼠标指针前后两个位置绘制直线
		pp.drawLine(self.lastPoint, self.endPoint)
		# 让前一个坐标值等于后一个坐标值
		# 这样就能实现画出连续的线
		self.lastPoint = self.endPoint
		painter =QPainter(self)
		painter.drawPixmap(0, 0, self.pix)

	def mousePressEvent(self, event):
		if event.buttons() == Qt.LeftButton: # 鼠标左键按下
			self.lastPoint = event.pos()

	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.endPoint = event.pos()
			self.update()  # 触发  paintEvent 事件

	def mouseReleaseEvent(self,event):
		# 鼠标左键释放
		if event.buttons()  == Qt.LeftButton:
			self.endPoint = event.pos()
			# 进行重新绘制
			self.update() 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Drawing()
    main.show()
    sys.exit(app.exec_())		



