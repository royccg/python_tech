from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class MyCalener(QWidget):
    def __init__(self):
        super(MyCalener, self).__init__()
        self.initUI()

    def initUI(self):
        self.cal = QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1988,1,1))
        self.cal.setMaximumDate(QDate(2088,1,1))

        self.cal.setGridVisible(True) # 设置网格
        self.cal.move(20, 20)
        self.cal.clicked.connect(self.showDate)


        self.label =QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(date.toString('yyyy-MM-dd dddd'))
        self.label.move(20,300)

        self.setWindowTitle('日历演示')
        self.resize(300,350)

    def showDate(self, date):
        # self.label.setText((date.toString('yyyy-MM-dd dddd')))
        self.label.setText((self.cal.selectedDate().toString('yyyy-MM-dd dddd')))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyCalener()
    main.show()

    sys.exit(app.exec_())
