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
        self.setWindowTitle('改变单元格中图片的尺寸')
        self.resize(1000, 900)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        # 设定尺寸
        tableWidget.setIconSize(QSize(300, 200))
        tableWidget.setRowCount(5)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['图片1', '图片2', '图片3'])

        # 设定图片的宽度和列的宽度一致
        for i in range(3):
            tableWidget.setColumnWidth(i, 300)

        for i in range(5):
            tableWidget.setRowHeight(i, 200)

        for k in range(15):
            i = k/3 # 行
            j = k%3 # 列
            item =QTableWidgetItem()
            # item.setIcon(QIcon('./image/new%d.png' % k))
            item.setIcon(QIcon('./image/new.png'))
            tableWidget.setItem(i, j, item)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = CellImageText()
    main.show()

    sys.exit(app.exec_())
