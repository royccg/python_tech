from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, os, math
from MyFunction import *
from MainWindowInitUI import Ui_mainWindow

#  set myWindow
class MyWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, parent =None):
        super(MyWindow, self).__init__(parent)
        # pyqt5中的界面设置
        self.setupUi(self)

        self.initUI()

     # add my iniUI
    def initUI(self):
        # add statusBar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        #  read data
        try:
            fp = 'data/base_data.json'
            if os.path.exists(fp):
                dataDict = readJson(fp)
                self.statusBar.showMessage('读取文件成功', 5000)
            else:
                dataDict = {}
                self.statusBar.showMessage('初始化储存文件', 3000)
        except IOError:
            self.statusBar.showMessage('Error: 没有找到文件或读取文件失败')
        # else:
        #     self.statusBar.showMessage('读取文件成功', 5000)

        # 这些内容需要放入 function中
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
        self.imagePutTableWidget.setShowGrid(False)

        # setting the 2ed tabwiget
        self.imageInfTableWidget.setRowCount(1) 
        self.imageInfTableWidget.setColumnCount(12) # 暂定12行 信息
        tableHorizontalHeaderLabel = ['id', '项目编号', '项目名称', '文件名', '项目类型', '桥梁类型1', '桥梁类型2',
                                                                        '材料类型', '桥梁风格', '桥梁规模', '桥梁跨径', '建成状态']
        self.imageInfTableWidget.setHorizontalHeaderLabels(tableHorizontalHeaderLabel)
        # self.imageInfTableWidget.setColumnHidden(0, True)
        self.imageInfTableWidget.setShowGrid(True)

        # 添加图片并展示在 中间窗口,待修改
        # imageRow , imageColum = 0,0
        self.loadImagePushButton.clicked.connect( lambda  :  self.loadImage(0, 0))
        # print(data)

        # 添加图片并展示在 中间窗口,待修改
        # imageRow , imageColum = 0,0
        self.savePicturePushButton.clicked.connect( self.saveData)

    def loadImage(self, rowIndex, columnIndex):
        self.statusBar.showMessage('传入效果图')
        # print('press importPicture')
        # fname, _= QFileDialog.getOpenFileName(self, '打开文件', '.', '图像文件(*.jpg *.png )')
        fnames, _= QFileDialog.getOpenFileNames(self, '打开文件', '.', '图像文件(*.jpg *.png )') # 传入多个文件
        # print(type(fnames))  # <class 'list'>
        # '''

        imageNowRow = self.imagePutTableWidget.RowCount()
        # 如果展示窗口没有图形
        '''siganl
            0 : 展示窗口没有文件
            1 ：展示窗口有奇数文件
            2 ：有偶数文件
        '''
        try
            if self.imagePutTableWidget.RowCount() == 0:
                signal = 0
            elif   self.imagePutTableWidget.item(imageNowRow, 2).text() == '':
                signal = 1
            else:
                signal =2
        except:
            print('error,读取当前展示框的图片数量失败')
            self.statusBar.showMessage('Error: 读取当前展示框的图片数量失败')

        if signal == 1:
            import math
            imageAftRow = math.ceil((imageNowRow/2 -1 +len(fnames))/2)*2
        else:
            import math
            imageAftRow =  imageNowRow + math.ceil(len(fnames)/2)*2

        # 设定 fnameRow 行2列
        self.imagePutTableWidget.setRowCount(imageAftRow)
        self.imagePutTableWidget.setColumnCount(2) 
        # 设定图片的尺寸
        self.imagePutTableWidget.setIconSize(QSize(250, 200))  #尺寸可能后面调动
        # 设定单元格的尺寸
        for i in range(2):
            self.imagePutTableWidget.setColumnWidth(i, 250)
        for i in range(imageAftRow):
            if i%2 == 0 :
                self.imagePutTableWidget.setRowHeight(i, 200)
            else:
                self.imagePutTableWidget.setRowHeight(i, 10)

#  补充到这
        if self.imagePutTableWidget.item(imageNowRow, 2).text() == '':
            imageAftRow = math.ceil((imageNowRow/2 -1 +len(fnames))/2)*2
        else:
        item = QTableWidgetItem()
        item.setIcon(QIcon(fnames))
        item.setTextAlignment(Qt.AlignCenter)
        self.imagePutTableWidget.setItem(rowIndex, columnIndex, item)
        # print(fnames)
        itemName = QTableWidgetItem(fnames.split('/')[-1])
        itemName.setTextAlignment(Qt.AlignCenter)
        self.imagePutTableWidget.setItem(rowIndex+1, columnIndex, itemName)

        try:
            id = creatUuid5(itemName.text())
            idItem = QTableWidgetItem(str(id))
            self.imageInfTableWidget.setItem(0, 0, idItem)
        except :
            print('error')
        return str(fnames)








    def saveData(self):
        '''
        保存当前数据库
        '''
        #  加入缓存的 字典 dataTemp
        dataTemp = {}
        # numImage = self.
        # for i in range():
        #     id = creatUuid5(self.imagePutTableWidget)

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
        jsobj = json.dumps(dataDict , cls =NpEncoder ,ensure_ascii= False,indent = 4)
        fileobject = open(self.fp,"w+",encoding= "utf-8")
        fileobject.write(jsobj)
        fileobject.close()
        pass
        
        # 清空掉 imageInf   imagePut
        self.imageInfTableWidget.setRowCount(1) 
        self.imageInfTableWidget.setColumnCount(12) 
        self.imagePutTableWidget.setRowCount() 
        self.imagePutTableWidget.setColumnCount() 












if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置程序的图标
    # app.setWindowIcon(QIcon("lufei.ico"))
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())
