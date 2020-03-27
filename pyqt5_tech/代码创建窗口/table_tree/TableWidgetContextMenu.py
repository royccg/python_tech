from PyQt5.QtWidgets import (QMenu, QPushButton, QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QHeaderView)
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtGui import QColor, QBrush, QFont
import sys

class TableWidgetContextMenu(QWidget):
    def __init__(self):
        super(TableWidgetContextMenu, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('在表格中显示上下文菜单')
        self.resize(500, 300)
        layout = QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        layout.addWidget(self.tableWidget)

        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重'])

        newItem = QTableWidgetItem('张三')
        self.tableWidget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem('165')
        self.tableWidget.setItem(0, 2, newItem)

        newItem = QTableWidgetItem('李四')
        self.tableWidget.setItem(1, 0, newItem)
        newItem = QTableWidgetItem('女')
        self.tableWidget.setItem(1, 1, newItem)
        newItem = QTableWidgetItem('160')
        self.tableWidget.setItem(1, 2, newItem)

        newItem = QTableWidgetItem('王五')
        self.tableWidget.setItem(2, 0, newItem)
        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(2, 1, newItem)
        newItem = QTableWidgetItem('170')
        self.tableWidget.setItem(2, 2, newItem)

        # 允许使用上下文菜单
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)

        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)

        self.setLayout(layout)

    def generateMenu(self, pos):
        print(pos)
        for i in self.tableWidget.selectionModel().selection().indexes():
            rowNum = i.row()  # 所选行的行数（是否多选）

        # 如果选择的行小于2，填出菜单
        if rowNum <2:
            menu = QMenu()
            item1 = menu.addAction('菜单项1')
            item2 = menu.addAction('菜单项2')
            item3 = menu.addAction('菜单项3')
            # 将窗口内的坐标位置 映射到 全局的
            screenPos = self.tableWidget.mapToGlobal(pos)
            print(screenPos)
            #  被阻塞
            action = menu.exec(screenPos)

            if action == item1:
                print('选择了第1个菜单项', self.tableWidget.item(rowNum, 0).text(),
                                            self.tableWidget.item(rowNum, 1).text(),
                                            self.tableWidget.item(rowNum, 2).text())
            elif action == item2:
                print('选择了第2个菜单项', self.tableWidget.item(rowNum, 0).text(),
                                            self.tableWidget.item(rowNum, 1).text(),
                                            self.tableWidget.item(rowNum, 2).text())
            elif action == item3:
                print('选择了第3个菜单项', self.tableWidget.item(rowNum, 0).text(),
                                            self.tableWidget.item(rowNum, 1).text(),
                                            self.tableWidget.item(rowNum, 2).text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TableWidgetContextMenu()
    main.show()

    sys.exit(app.exec_())
