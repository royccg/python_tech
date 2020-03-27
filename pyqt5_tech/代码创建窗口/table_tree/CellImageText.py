# 图文混排
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class CellImageText(QWidget):
    def __init__(self):
        super(CellImageText, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('在单元格中实现图文混排的效果')
        self.resize(500, 300)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(5)
        tableWidget.setColumnCount(4)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重', '显示图片'])

        newItem = QTableWidgetItem('李宁')

        tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem('男')
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem('160')
        tableWidget.setItem(0, 2, newItem)

        newItem = QTableWidgetItem(QIcon('new.png'), '打开')
        tableWidget.setItem(0, 3, newItem)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = CellImageText()
    main.show()

    sys.exit(app.exec_())
