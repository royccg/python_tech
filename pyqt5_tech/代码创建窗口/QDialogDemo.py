import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QDialogDemo(QMainWindow):
    #  初始化，
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QDialogDemo')
        self.resize(300, 200)

        self.button = QPushButton(self)
        self.button.setText('弹出对话框')
        self.button.move(50, 50)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        button = QPushButton('确定', dialog)
        button.clicked.connect(dialog.close)
        button.move(50, 50)
        dialog.setWindowTitle('对话框')
        #  模式调用，打开对话框后，主体的窗口不可用
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = QDialogDemo()
    main.show()

    sys.exit(app.exec_())
