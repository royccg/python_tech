from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        bar = self.menuBar()  # 获取菜单栏

        file = bar.addMenu("文件")
        file.addAction('新建')

        save =QAction('保存', self)
        save.setShortcut('Ctrl + S') # 快捷键
        file.addAction(save)

        save.triggered.connect(self.process)

        edit = bar.addMenu('Edit')
        edit.addAction('copy')
        edit.addAction('paste')
        quit = QAction("退出", self)
        file.addAction(quit)

    def process(self):
        print(self.sender().text())
        print('save')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Menu()
    main.show()
    sys.exit(app.exec_())
