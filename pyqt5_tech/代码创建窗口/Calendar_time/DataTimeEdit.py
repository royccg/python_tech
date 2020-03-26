from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class DateTimeEdit(QWidget):
    def __init__(self):
        super(DateTimeEdit, self).__init__()
        self.initUI()

    def initUI(self):
        vlayout = QVBoxLayout()
        dateTimeEdit1 =QDateTimeEdit()
        dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime())
        dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))
        dateTimeEdit1.setMaximumDate(QDate.currentDate().addDays(365))

        self.dateTimeEdit = dateTimeEdit1
        dateTimeEdit2.setCalendarPopup(True) # 变成下拉控件

        dateEdit = QDateTimeEdit(QDate.currentDate())
        timeEdit = QDateTimeEdit(QTime.currentTime())

        dateTimeEdit1.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        dateTimeEdit2.setDisplayFormat('yyyy/MM/dd HH-mm-ss')

        dateEdit.setDisplayFormat('yyyy.MM.dd')
        timeEdit.setDisplayFormat('HH:mm:ss')

        dateTimeEdit1.dateChanged.connect(self.onDateChanged)
        dateTimeEdit1.timeChanged.connect(self.onTimeChanged)
        dateTimeEdit1.dateTimeChanged.connect(self.onDateTimeChanged)

        vlayout.addWidget(dateTimeEdit1)
        vlayout.addWidget(dateTimeEdit2)
        vlayout.addWidget(dateEdit)
        vlayout.addWidget(timeEdit)

        btn = QPushButton('获取日期和时间')
        btn.clicked.connect(self.onButtonClick)
        vlayout.addWidget(btn)

        self.setLayout(vlayout)
        self.resize(300, 90)
        self.setWindowTitle('设置不同风格的日期和时间')

    #  日期变化
    def onDateChanged(self, date):
        print(date)

    def onTimeChanged(self, time):
        print(time)

    # 日期和时间变化
    def  onDateTimeChanged(self, dateTime):
        print(dateTime)

    def onButtonClick(self):
        datetime = self.dateTimeEdit.dateTime()
        print(datetime)

        # 最大日期
        print(self.dateTimeEdit.maximumDate())
        # 最大日期和时间
        print(self.dateTimeEdit.maximumDateTime)

        # 最小日期
        print(self.dateTimeEdit.minimumDate())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DateTimeEdit()
    main.show()

    sys.exit(app.exec_())
