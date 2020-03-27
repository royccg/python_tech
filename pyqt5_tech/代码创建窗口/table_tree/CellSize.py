from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem)
from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QBrush, QFont
import sys

class ColumnSize(QWidget):
    def __init__(self):
        super(ColumnSize, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('代码改变单元格的大小')
        self.resize(530, 300)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])
        tableWidget.setRowHeight(0, 100) # 第0行的高度80
        tableWidget.setColumnWidth(2, 150)
        newItem = QTableWidgetItem('雷神')
        newItem.setFont(QFont('Times', 20, QFont.Black))
        newItem.setForeground(QBrush(QColor(255, 0, 0)))
        tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem('女')
        newItem.setForeground(QBrush(QColor(255, 255, 0)))
        newItem.setBackground(QBrush(QColor(0, 0, 255)))
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem('160')
        newItem.setFont(QFont('Times', 60, QFont.Black))
        newItem.setForeground(QBrush(QColor(0, 0, 255)))
        tableWidget.setItem(0, 2, newItem)

        self.setLayout(layout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ColumnSize()
    main.show()

    sys.exit(app.exec_())
