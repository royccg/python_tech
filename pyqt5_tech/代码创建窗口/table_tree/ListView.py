
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class TableView(QWidget):
    def __init__(self, arg =None):
        super(TableView, self).__init__(arg)
        self.setWindowTitle('QTableView表格视图控件演示')
        self.resize(300, 270)
        layout = QVBoxLayout()

        listview = QListView()
        listModel = QStringListModel()
        self.list = ['列表项1', '列表项2', '列表项3']

        listModel.setStringList(self.list)

        listview.setModel(listModel)
        listview.clicked.connect(self.clicked)
        layout.addWidget(listview)

        self.setLayout(layout)

    def clicked(self, item):
        QMessageBox.information(self, "QListView", "您选择了：" + self.list[item.row()])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TableView()
    main.show()

    sys.exit(app.exec_())
