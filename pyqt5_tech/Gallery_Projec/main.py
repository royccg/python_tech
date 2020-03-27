from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

from MainWindowInitUI import Ui_mainWindow

class MyWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, parent =None):
        super(MyWindow, self).__init__(parent)
        # pyqt5中的界面设置
        self.setupUi(self)
        self.initUI()

    # 自己添加的内容
    def initUI(self):
        # pass
        # 添加状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # 设定10行2列
        self.imagePutTableWidget.setRowCount(10)
        self.imagePutTableWidget.setColumnCount(2)
        # 设定图片的尺寸
        self.imagePutTableWidget.setIconSize(QSize(250, 200))

        # 设定单元格的尺寸
        for i in range(2):
            self.imagePutTableWidget.setColumnWidth(i, 250)

        for i in range(10):
            if i%2 == 0 :
                self.imagePutTableWidget.setRowHeight(i, 200)
            else:
                self.imagePutTableWidget.setRowHeight(i, 10)

        # 隐藏表头
        self.imagePutTableWidget.horizontalHeader().setVisible(False)
        self.imagePutTableWidget.verticalHeader().setVisible(False)
        # 隐藏表格线
        # self.imagePutTableWidget.setShowGrid(False)

        # 添加图片并展示在 中间窗口
        self.loadImagePushButton.clicked.connect(lambda: self.loadImage(0, 0))

    def loadImage(self, rowIndex, columnIndex):
        # print('press importPicture')
        fname, _= QFileDialog.getOpenFileName(self,'打开文件','.','图像文件(*.jpg *.png )')
        # print(type(fname))
        item = QTableWidgetItem()
        item.setIcon(QIcon(fname))
        item.setTextAlignment(Qt.AlignCenter)
        self.imagePutTableWidget.setItem(rowIndex, columnIndex, item)
        # print(fname)
        itemName = QTableWidgetItem(fname.split('/')[-1])
        self.imagePutTableWidget.setItem(rowIndex+1, columnIndex,itemName)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置程序的图标
    # app.setWindowIcon(QIcon("lufei.ico"))
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())
