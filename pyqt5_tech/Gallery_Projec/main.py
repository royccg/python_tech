# -*- coding: UTF-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os
import math
from MyFunction import *
from MainWindowInitUI import Ui_mainWindow

#  set myWindow


class MyWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        # pyqt5中的界面设置
        self.setupUi(self)
        self.initUI()

     # add my iniUI
    def initUI(self):
        # add statusBar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # 设置左边区域的占比

        #  read data
        try:
            self.fp = 'data/base_data.json'
            if os.path.exists(self.fp):
                self.dataDict = readJson(self.fp)
                self.statusBar.showMessage('读取文件成功', 5000)
            else:
                self.dataDict = {}
                self.statusBar.showMessage('初始化储存文件', 3000)
        except IOError:
            self.statusBar.showMessage('Error: 没有找到文件或读取文件失败')
        # else:
        #     self.statusBar.showMessage('读取文件成功', 5000)

        # 隐藏表头
        self.imagePutTableWidget.horizontalHeader().setVisible(False)
        self.imagePutTableWidget.verticalHeader().setVisible(False)
        # 隐藏表格线
        self.imagePutTableWidget.setShowGrid(False)

        # setting the 2ed tabwiget
        self.imageInfTableWidget.setRowCount(0)
        self.imageInfTableWidget.setColumnCount(14)  # 暂定14行 信息
        self.tableHorizontalHeaderLabel = ['id', '项目编号', '项目名称', '文件名', '项目类型', '桥梁类型1', '桥梁类型2',
                                           '材料类型', '桥梁风格', '桥梁规模', '桥梁跨径', '建成状态', '文件本机地址', '文件指向储存地址']
        self.imageInfTableWidget.setHorizontalHeaderLabels(self.tableHorizontalHeaderLabel)
        # self.imageInfTableWidget.setColumnHidden(0, True)   # 隐藏列  id  文件本机地址  指向存储地址
        # self.imageInfTableWidget.setColumnHidden(12, True)
        # self.imageInfTableWidget.setColumnHidden(13, True)
        self.imageInfTableWidget.setShowGrid(True)

        # 添加图片并展示在 中间窗口,待修改
        self.loadImagePushButton.clicked.connect(self.loadImage)
        # print(data)

        # 添加图片并展示在 中间窗口,待修改
        # imageRow , imageColum = 0,0
        self.savePicturePushButton.clicked.connect(self.saveData)
        # 添加其他功能

    def loadImage(self):
        self.statusBar.showMessage('传入效果图')
        # print('press importPicture')
        # fname, _= QFileDialog.getOpenFileName(self, '打开文件', '.', '图像文件(*.jpg *.png )')
        fnames, _ = QFileDialog.getOpenFileNames(self, '打开文件', '.', '图像文件(*.jpg *.png )')  # 传入多个文件
        # print(type(fnames))  # <class 'list'>

        # 首先判断 输入的文件中有没有 文件名和库中文件冲突的
        tempLs = []
        idLs = []
        for i in fnames:
            id = creatUuid5(i.split('/')[-1])
            # print(self.dataDict)
            if str(id) in self.dataDict:
                self.statusBar.showMessage('Error: %s 文件名冲突，或文件已录入' % i.split('/')[-1])
                QMessageBox.critical(self, '错误', '文件名与库中图重复，或文件已录入', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                tempLs.append(i)
            else:
                idLs.append(id)
        # 删除 重叠的图片
        for i in fnames:
            if i in tempLs:
                fnames.remove(i)
        # '''
        # 如果展示窗口没有图形
        '''
        siganl:
            0 : 展示窗口没有文件 或偶数张图片
            1 ：展示窗口有奇数文件
            tempNum: 当前有的图片数量
        '''
        tempNum = self.imageInfTableWidget.rowCount()
        imageNowRow = self.imagePutTableWidget.rowCount()   # 可以优化
        try:
            if tempNum % 2 == 0:
                signal = 0
            else:
                signal = 1
        except:
            print('error,读取当前展示框的图片数量失败')
            self.statusBar.showMessage('Error: 读取当前展示框的图片数量失败')
        # '''
        #
        if signal == 1:
            import math
            imageAftRow = math.ceil((imageNowRow / 2 - 1 + len(fnames)) / 2) * 2
        else:
            import math
            imageAftRow = imageNowRow + math.ceil(len(fnames) / 2) * 2

        #  先设置 TableInfWidget内的设置
        nowInfRow = self.imageInfTableWidget.rowCount()
        self.imageInfTableWidget.setRowCount(nowInfRow + len(idLs))
        for i in range(len(idLs)):
            idItem = QTableWidgetItem(str(idLs[i]))
            self.imageInfTableWidget.setItem(nowInfRow + i, 0, idItem)
            #  提前设置每个 cell的空值，防止后面留空
            for m in range(len(self.tableHorizontalHeaderLabel) - 1):
                contextItem = QTableWidgetItem()
                self.imageInfTableWidget.setItem(nowInfRow + i, m + 1, contextItem)

        # 设置 imagePutWidget
        # 设定 fnameRow 行2列
        self.imagePutTableWidget.setRowCount(imageAftRow)
        self.imagePutTableWidget.setColumnCount(2)
        # 设定图片的尺寸
        self.imagePutTableWidget.setIconSize(QSize(250, 200))  # 尺寸可能后面调动
        # 设定单元格的尺寸
        for i in range(2):
            self.imagePutTableWidget.setColumnWidth(i, 250)
        for i in range(imageAftRow):
            if i % 2 == 0:
                self.imagePutTableWidget.setRowHeight(i, 200)
            else:
                self.imagePutTableWidget.setRowHeight(i, 10)

        #  设置  待补充
        if signal != 1:  # 展示框中原来没有图片或  偶数照片
            # item 从头开始
            for i in range(len(fnames)):
                itemName = QTableWidgetItem(fnames[i].split('/')[-1])
                itemName.setTextAlignment(Qt.AlignCenter)
                item = QTableWidgetItem()
                item.setIcon(QIcon(fnames[i]))
                item.setTextAlignment(Qt.AlignCenter)
                if (i + 1) % 2 == 0:
                    columnIndex = 1
                    self.imagePutTableWidget.setItem(imageNowRow + numQue(i) - 1, columnIndex, item)
                    self.imagePutTableWidget.setItem(imageNowRow + numQue(i), columnIndex, itemName)
                else:
                    columnIndex = 0
                    self.imagePutTableWidget.setItem(imageNowRow + numQue(i + 1) - 1, columnIndex, item)
                    self.imagePutTableWidget.setItem(imageNowRow + numQue(i + 1), columnIndex, itemName)

        elif signal == 1:
            for i in range(len(fnames)):
                itemName = QTableWidgetItem(fnames[i].split('/')[-1])
                itemName.setTextAlignment(Qt.AlignCenter)
                item = QTableWidgetItem()
                item.setIcon(QIcon(fnames[i]))
                item.setTextAlignment(Qt.AlignCenter)
                if (i + 1) % 2 != 0:
                    columnIndex = 1
                    self.imagePutTableWidget.setItem(imageNowRow + numQue(i), columnIndex, item)
                    self.imagePutTableWidget.setItem(imageNowRow + numQue(i) + 1, columnIndex, itemName)
                else:
                    columnIndex = 0
                    self.imagePutTableWidget.setItem(imageNowRow + numQue(i + 1), columnIndex, item)
                    self.imagePutTableWidget.setItem(imageNowRow + numQue(i + 1) + 1, columnIndex, itemName)

    def saveData(self):
        '''
        保存当前数据库
        '''
        #  加入缓存的 字典 dataTemp
        dataTemp = {}
        tempNum = self.imageInfTableWidget.rowCount()
        # s = self.imageInfTableWidget.item(0,0).text()
        tabelHHLabel = self.tableHorizontalHeaderLabel
        for i in range(tempNum):
            id = self.imageInfTableWidget.item(i, 0).text()
            dataTemp[id] = {}
            for j in range(len(tabelHHLabel)):
                context = self.imageInfTableWidget.item(i, j).text()
                dataTemp[id][tabelHHLabel[j]] = context
                # pass
        self.dataDict.update(dataTemp)
        dataWrite = self.dataDict
        import json

        class NpEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, np.integer):
                    return int(obj)
                elif isinstance(obj, np.floating):
                    return float(obj)
                elif isinstance(obj, np.ndarray):
                    return obj.tolist()
                else:
                    return super(NpEncoder, self).default(obj)
        try:
            jsobj = json.dumps(dataWrite, cls=NpEncoder, ensure_ascii=False, indent=4)
            fileobject = open(self.fp, "w+", encoding="utf-8")
            fileobject.write(jsobj)
            fileobject.close()
        except IOError:
            self.statusBar.showMessage('Error: 写入文件失败')

        # 清空掉 imageInf   imagePut
        self.imageInfTableWidget.setRowCount(0)
        self.imageInfTableWidget.setColumnCount(12)
        self.imagePutTableWidget.setRowCount(0)
        self.imagePutTableWidget.setColumnCount(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置程序的图标
    # app.setWindowIcon(QIcon("lufei.ico"))
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())
