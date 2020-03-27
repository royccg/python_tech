from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QBrush
import sys

class DataLocation(QWidget):
    def __init__(self):
        super(DataLocation, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('在单元格中放置控件')
        self.resize(600, 800)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(40)
        tableWidget.setColumnCount(4)

        layout.addWidget(tableWidget)

        for i in range(40):
            for j in range(4):
                itemContent = '(%d, %d)' %(i, j)
                tableWidget.setItem(i, j, QTableWidgetItem(itemContent))

        self.setLayout(layout)

        # 搜索满足条件的Cell
        # text = '(13, 1)'
        # # 精确搜索
        # items = tableWidget.findItems(text, QtCore.Qt.MatchExactly)

        text = '(12'
        # 精确搜索
        items = tableWidget.findItems(text, QtCore.Qt.MatchStartsWith)
        if len(items) > 0:
            item = items[0]
            item.setBackground(QBrush(QColor(0, 255, 0)))  # 背景色
            item.setForeground(QBrush(QColor(255, 0, 0)))  # 前景色

            row = item.row()

            # 滚动到指定的行
            tableWidget.verticalScrollBar().setSliderPosition(row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DataLocation()
    main.show()

    sys.exit(app.exec_())
