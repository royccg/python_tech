
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class TableWidgetDemo(QWidget):
    def __init__(self, arg =None):
        super(TableWidgetDemo, self).__init__(arg)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTableWidget Demo')
        self.resize(430, 230)

        layout = QHBoxLayout()
        tablewidget = QTableWidget()
        tablewidget.setRowCount(4) # 设置行
        tablewidget.setColumnCount(3)

        layout.addWidget(tablewidget)
        tablewidget.setHorizontalHeaderLabels(['姓名', '年龄', '籍贯'])

        nameItem = QTableWidgetItem('小明')
        tablewidget.setItem(0, 0, nameItem)

        ageItem = QTableWidgetItem('24')
        tablewidget.setItem(0, 1, ageItem)

        jgItem = QTableWidgetItem('北京')
        tablewidget.setItem(0, 2, jgItem)

        # 禁止编辑
        tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 整行选择
        tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 行和列的大小根据内容进行调整
        tablewidget.resizeColumnsToContents()
        tablewidget.resizeRowsToContents()

        # 隐藏表头
        tablewidget.horizontalHeader().setVisible(False)
        # tablewidget.verticalHeader().setVisible(False)

        # 设置头标签
        tablewidget.setVerticalHeaderLabels(['a','b'])

        # 隐藏表格线
        tablewidget.setShowGrid(False)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TableWidgetDemo()
    main.show()

    sys.exit(app.exec_())
