"""
QSS基础：
	QSS(Qt style sheets)
	Qt样式表
用于设置控件的方格、样式

类似于CSS

"""

import sys
from PyQt5.QtWidgets import *


class BasicQSS(QWidget):
	"""docstring for BasicQSS"""
	def __init__(self, parent= None):
		super(BasicQSS, self).__init__(parent)
		self.setWindowTitle('QSS样式')

		btn1 = QPushButton(self)
		btn1.setText('按钮1')
		btn2 = QPushButton(self)
		btn2.setText('按钮2')
		vbox = QVBoxLayout()
		vbox.addWidget(btn1)
		vbox.addWidget(btn2)

		self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = BasicQSS()
    # 设置 控件的风格
    # 选择器
    qssStyle = '''
    	QPushButton  {
    		background-color: red
    	}
    '''
    main.setStyleSheet(qssStyle)
    main.show()
    sys.exit(app.exec_())		



