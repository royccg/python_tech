from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class CellTextAlignment(QWidget):
    def __init__(self):
        super(CellTextAlignment, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('按列排序')
        self.resize(430, 230)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])

        newItem = QTableWidgetItem('雷神')
        newItem.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)
        tableWidget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem('男')
        newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
        tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem('190')
        newItem.setTextAlignment(Qt.AlignRight)
        tableWidget.setItem(0, 2, newItem)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = CellTextAlignment()
    main.show()

    sys.exit(app.exec_())
