
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class TableView(QWidget):
    def __init__(self, arg =None):
        super(TableView, self).__init__(arg)
        self.setWindowTitle('QTableView表格视图控件演示')
        self.resize(500, 300)

        self.model = QStandardItemModel(4, 3) # 4行3列
        self.model.setHorizontalHeaderLabels(['id', '姓名', '年龄'])

        self.tableview = QTableView()
        # 关联QTabelView控件和Model
        self.tableview.setModel(self.model)

        # 添加数据
        item11 = QStandardItem('10')
        item12 = QStandardItem('雷神')
        item13 = QStandardItem('2000')
        self.model.setItem(0, 0 ,item11)
        self.model.setItem(0, 1 ,item12)
        self.model.setItem(0, 2 ,item13)

        item21 = QStandardItem('30')
        item22 = QStandardItem('女神')
        item23 = QStandardItem('3000')
        self.model.setItem(1, 0 ,item21)
        self.model.setItem(1, 1 ,item22)
        self.model.setItem(1, 2 ,item23)

        layout = QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TableView()
    main.show()

    sys.exit(app.exec_())
