# -*- coding: utf-8 -*-
# @Author: royccg
# @Email:roy778555479@gmail.com
# @Date:   2020-04-13 00:14:42
# @Last Modified time: 2020-04-21 21:07:41

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import Qt



class Ui_MainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName('mainWindow')
        mainWindow.setEnabled(True)
        mainWindow.resize(950, 480)

        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        # 设置最小尺寸
        mainWindow.setMinimumSize(QtCore.QSize(1000, 800))
        mainWindow.setMaximumSize(QtCore.QSize(100000, 100000))

        # 设置主窗口
        self.centralWidget = QtWidgets.QWidget(mainWindow)
        self.centralWidget.setObjectName("centralWidget")

        # 设定一个主的横向布局
        self.HVBoxMain = QtWidgets.QHBoxLayout(self.centralWidget)
        self.HVBoxMain.setObjectName('HVBoxMain')

        # 设置两个竖向布局
        self.vboxLeft = QtWidgets.QVBoxLayout()
        self.vboxRight = QtWidgets.QVBoxLayout()

        # 中间分割线
        self.MiddleLine = QtWidgets.QFrame(self.centralWidget)
        self.MiddleLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.MiddleLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.MiddleLine.setObjectName('MiddleLine')

        # vboxLeft
        self.label_leftTopNamexiaoguotu = QtWidgets.QLabel()

        self.label_leftTopNamexiaoguotu.setObjectName('xiaoguotu')

        self.MainPictrueTable = QtWidgets.QTableWidget(self.centralWidget)
        self.MainPictrueTable.setColumnCount(0)
        self.MainPictrueTable.setRowCount(0)
        self.MainPictrueTable.setObjectName('MainPictrueTable')
        # self.MainPictrueTable.setMinimumSize(QtCore.QSize(730, 500))

        # 左边区域分割线
        self.LeftLine = QtWidgets.QFrame(self.centralWidget)
        self.LeftLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.LeftLine.setFrameShadow(QtWidgets.QFrame.Sunken)

        # 下方的信息输入框
        self.imageInfTableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.imageInfTableWidget.setColumnCount(0)
        self.imageInfTableWidget.setRowCount(0)
        self.imageInfTableWidget.setObjectName('imageInfTableWidget')
        # self.imageInfTableWidget.setMinimumSize(QtCore.QSize(730, 200))

        self.vboxLeft.addStretch(0)
        self.vboxLeft.addWidget(self.label_leftTopNamexiaoguotu, 0, Qt.AlignLeft)  # LeftTop
        self.vboxLeft.addWidget(self.MainPictrueTable, 6)
        self.vboxLeft.addWidget(self.LeftLine, 0)
        self.vboxLeft.addWidget(self.imageInfTableWidget, 3)
        # self.vboxLeft.addStretch(0)

        # 右边的功能区
        self.Mainlabel1 = QtWidgets.QLabel()
        self.label2 = QtWidgets.QLabel()

        # 右边分割线1
        self.RightLine1 = QtWidgets.QFrame(self.centralWidget)
        self.RightLine1.setFrameShape(QtWidgets.QFrame.HLine)
        self.RightLine1.setFrameShadow(QtWidgets.QFrame.Sunken)

        # 右边功能区的 上部的 水平布局
        self.rightMainSettingHbox = QtWidgets.QHBoxLayout()

        self.ZLSetting = QtWidgets.QPushButton()
        self.BQSetting = QtWidgets.QPushButton()

        self.rightMainSettingHbox.addWidget(self.ZLSetting)
        self.rightMainSettingHbox.addWidget(self.BQSetting)

        # 添加功能块
        self.GNTabWidget = QtWidgets.QTabWidget()
        self.GNTabWidget.setObjectName('GNTabWidget')

        self.tab_input = QtWidgets.QWidget()
        self.tab_input.setObjectName('tab_input')
        self.tab_demand = QtWidgets.QWidget()
        self.tab_demand.setObjectName('tab_demand')

        self.GNTabWidget.addTab(self.tab_input, "")
        self.GNTabWidget.addTab(self.tab_demand, "")

        # 添加 界面
        self.gridForm = QtWidgets.QGridLayout(self.tab_input)
        self.loadImagePushButton = QtWidgets.QPushButton()
        self.importFolderPushButton = QtWidgets.QPushButton()
        self.savePicturePushButton = QtWidgets.QPushButton()
        self.waitingPushButton = QtWidgets.QPushButton()

        self.waitingPushButton.setEnabled(False)

        self.gridForm.addWidget(self.loadImagePushButton, 0, 0)
        self.gridForm.addWidget(self.importFolderPushButton, 0, 1)
        self.gridForm.addWidget(self.savePicturePushButton, 1, 0)
        self.gridForm.addWidget(self.waitingPushButton, 1, 1)
        # 填充空隙
        self.gridForm.addWidget(QtWidgets.QLabel(), 2, 0)

        # 查询界面
        self.searchVboxLayout = QtWidgets.QVBoxLayout(self.tab_demand)
        # self.searchGridForm = QtWidgets.QGridLayout(self.tab_demand)

        self.labelAdvancedSearch = QtWidgets.QLabel()
        self.MiddleLine02 = QtWidgets.QFrame()
        self.MiddleLine02.setFrameShape(QtWidgets.QFrame.VLine)
        self.MiddleLine02.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.MiddleLine02.setObjectName('MiddleLine02')
        self.labelAdvancedHelp = QtWidgets.QLabel()
        self.searchTopHBoxLayout = QtWidgets.QHBoxLayout()
        self.searchTopHBoxLayout.addStretch(0)
        self.searchTopHBoxLayout.addWidget(self.labelAdvancedSearch)
        self.searchTopHBoxLayout.addWidget(self.MiddleLine02)
        self.searchTopHBoxLayout.addWidget(self.labelAdvancedHelp)

        self.searchInputHBoxLayout = QtWidgets.QHBoxLayout()
        self.SearchCombBox = QtWidgets.QComboBox()
        self.SearchLineEdit = QtWidgets.QLineEdit()
        self.SearchPushButton = QtWidgets.QPushButton()
        self.searchInputHBoxLayout.addWidget(self.SearchCombBox, 2)
        self.searchInputHBoxLayout.addWidget(self.SearchLineEdit,5)
        self.searchInputHBoxLayout.addWidget(self.SearchPushButton, 2)

        #  增加 条目
        self.SearchCombBox.addItem('')
        self.SearchCombBox.addItem('')

        self.searchVboxLayout.addStretch(0)
        self.searchVboxLayout.addLayout(self.searchTopHBoxLayout)
        self.searchVboxLayout.addLayout(self.searchInputHBoxLayout)
        # self.searchVboxLayout.addWidget(self)
        self.searchVboxLayout.addStretch(1)
        self.searchVboxLayout.addWidget(QtWidgets.QLabel('asdad'))
        self.searchVboxLayout.setSpacing(1)


        # 右边功能区添加控件
        self.vboxRight.addWidget(self.Mainlabel1, 0, Qt.AlignTop | Qt.AlignLeft)
        self.vboxRight.addWidget(self.label2, 0, Qt.AlignTop | Qt.AlignLeft)
        self.vboxRight.addWidget(self.RightLine1, 0)
        self.vboxRight.addLayout(self.rightMainSettingHbox, 1)
        self.vboxRight.addWidget(self.GNTabWidget, 5)

        # 左右两个的布局的比例是  4：1
        self.HVBoxMain.addLayout(self.vboxLeft, 5)
        self.HVBoxMain.addWidget(self.MiddleLine, 0)
        self.HVBoxMain.addLayout(self.vboxRight, 3)

        mainWindow.setCentralWidget(self.centralWidget)

        # 状态栏和 菜单栏
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 955, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuImport = QtWidgets.QMenu(self.menuFile)
        self.menuImport.setObjectName("menuImport")
        self.menuabout = QtWidgets.QMenu(self.menubar)
        self.menuabout.setObjectName("menuabout")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionProject = QtWidgets.QAction(mainWindow)
        self.actionProject.setObjectName("actionProject")
        self.actionRegistered = QtWidgets.QAction(mainWindow)
        self.actionRegistered.setObjectName("actionRegistered")
        self.actionOpen = QtWidgets.QAction(mainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(mainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionimport_file = QtWidgets.QAction(mainWindow)
        self.actionimport_file.setObjectName("actionimport_file")
        self.actionimport_folder = QtWidgets.QAction(mainWindow)
        self.actionimport_folder.setObjectName("actionimport_folder")
        self.menuImport.addAction(self.actionimport_file)
        self.menuImport.addAction(self.actionimport_folder)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuImport.menuAction())
        self.menuabout.addAction(self.actionProject)
        self.menuabout.addAction(self.actionRegistered)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuabout.menuAction())

        self.retranslateUi(mainWindow)
        self.GNTabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        #  set myWindow
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate('mainWindow', '效果图库'))
        self.label_leftTopNamexiaoguotu.setText(_translate('mainWindow', '效果图'))
        self.Mainlabel1.setText(_translate(
            'mainWindow', '<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">我的归档图库</span></p></body></html>'))
        self.label2.setText(_translate(
            'mainWindow', '<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">管理</span></p></body></html>'))
        self.ZLSetting.setText(_translate('mainWindow', '资料库配置'))
        self.BQSetting.setText(_translate('mainWindow', '标签库配置'))
        self.GNTabWidget.setTabText(self.GNTabWidget.indexOf(self.tab_input), _translate('mainWindow', '添加图库'))
        self.GNTabWidget.setTabEnabled(self.GNTabWidget.indexOf(self.tab_input),False)
        self.GNTabWidget.setTabText(self.GNTabWidget.indexOf(self.tab_demand), _translate('mainWindow', '查询'))
        self.loadImagePushButton.setText(_translate('mainWindow', '添加图片'))
        self.importFolderPushButton.setText(_translate('mainWindow', '添加文件夹'))
        self.savePicturePushButton.setText(_translate('mainWindow', '保存'))
        self.waitingPushButton.setText(_translate('mainWindow', '待添加'))

        # comboBox 添加内容  setItemText
        self.SearchCombBox.setItemText(0, _translate('mainWindow', '桥梁'))
        self.SearchCombBox.setItemText(1, _translate('mainWindow', '道路'))

        self.SearchLineEdit.setPlaceholderText(_translate('mainWindow', '输入关键字开始搜索'))
        self.SearchPushButton.setText(_translate('mainWindow','开始搜索'))
        self.labelAdvancedHelp.setText(_translate('mainWindow', '帮助'))

        self.labelAdvancedSearch.setText(_translate('mainWindow', '高级搜索'))


        # 状态栏 和菜单栏
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.menuImport.setTitle(_translate("mainWindow", "Import "))
        self.menuabout.setTitle(_translate("mainWindow", "About"))
        self.menuHelp.setTitle(_translate("mainWindow", "Help"))
        self.actionProject.setText(_translate("mainWindow", "Project"))
        self.actionRegistered.setText(_translate("mainWindow", "Registered"))
        self.actionOpen.setText(_translate("mainWindow", "Open Data"))
        self.actionSave.setText(_translate("mainWindow", "Save Data"))
        self.actionSave.setShortcut(_translate("mainWindow", "Ctrl+S"))
        self.actionimport_file.setText(_translate("mainWindow", "import file"))
        self.actionimport_folder.setText(_translate("mainWindow", "import folder"))

        # 设置查询区的控件
        # self.searchGridForm.addItem(_translate('mainWindow', '普通搜索'))



# 编辑登陆界面
class loginWindow(object):
    def setupUi(self, mainWindow):
        self.setWindowTitle('用户名认证')
        self.resize(350,100)
        # mainWindow.setEnabled(True)
        # self.centralWidget = QtWidgets.QWidget(mainWindow)
        self.LabelName = QtWidgets.QLabel('用户名：')
        self.LabelPassword = QtWidgets.QLabel('密码：')
        self.lineName = QtWidgets.QLineEdit()
        self.lineName.setPlaceholderText('输入Ekp账号')
        self.linePassword = QtWidgets.QLineEdit()
        self.linePassword.setPlaceholderText ('输入Ekp密码')
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.Password)

        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.addRow(self.LabelName,self.lineName)
        self.formLayout.addRow(self.LabelPassword,self.linePassword)

        self.OkPushButton = QtWidgets.QPushButton('管理员登陆')
        self.VisitorLogin = QtWidgets.QPushButton('不登录')
        self.RemeberPw = QtWidgets.QCheckBox('记住密码')

        self.hboxLayout = QtWidgets.QHBoxLayout()
        self.hboxLayout.addStretch(0)
        self.hboxLayout.addWidget(self.RemeberPw)
        self.hboxLayout.addWidget(self.OkPushButton)
        self.hboxLayout.addWidget(self.VisitorLogin)

        self.Vboxlayout = QtWidgets.QVBoxLayout()
        self.Vboxlayout.addLayout(self.formLayout)
        self.Vboxlayout.addLayout(self.hboxLayout)

        self.setLayout(self.Vboxlayout)

