
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys,math

class MyComboxBox(QComboBox):  #下拉列表
    def __init__(self):
        super(MyComboxBox, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.addItem(e.mimeData().text())

class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo, self).__init__()
        formLayout = QFormLayout()
        formLayout.addRow(QLabel('请将左边的文本拖拽到右边的下拉列表中'))
        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)  # 让控件 可拖动

        comba  = MyComboxBox()
        formLayout.addRow(lineEdit,comba)

        self.setLayout(formLayout)
        self.setWindowTitle('拖拽案例')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DrapDropDemo()
    main.show()

    sys.exit(app.exec_())
