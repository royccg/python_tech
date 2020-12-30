# -*- coding: utf-8 -*-
# @Author: royccg
# @Email:roy778555479@gmail.com
# @Date:   2020-04-20 10:43:06
# @Last Modified time: 2020-05-24 22:32:06

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
import sys
import os
from UIDesigned_V01 import Ui_MainWindow, loginWindow, folderInputWindow
from MyFunction import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        try:
            if os.path.exists('data'):
                pass
            else:
                os.mkdir('data')
        except:
            pass

            # read data
        try:
            self.fp = 'data/base_data.json'
            if os.path.exists(self.fp):
                self.dataDict = readJson(self.fp)
                self.statusbar.showMessage('读取文件成功', 5000)
            else:
                self.dataDict = {}
                self.statusbar.showMessage('初始化储存文件', 3000)
        except IOError:
            self.statusbar.showMessage('Error: 没有找到文件或读取文件失败')

        global adminlogin
        if adminlogin == 1:
            self.GNTabWidget.setTabEnabled(self.GNTabWidget.indexOf(self.tab_input), True)
        #   pass
        # self.GNTabWidget.setTabEnabled(self.GNTabWidget.indexOf(self.tab_input), True)

        self.MainPictrueTable.setColumnCount(3)
        self.MainPictrueTable.setHorizontalHeaderLabels(['名称', '扩展名', '大小'])
        self.MainPictrueTable.setColumnWidth(0, 300)
        # 隐藏表头
        # self.MainPictrueTable.horizontalHeader().setVisible(False)
        # self.MainPictrueTable.verticalHeader().setVisible(False)
        # 隐藏表格线
        # self.MainPictrueTable.setShowGrid(False)

        # setting the 2ed tabwiget
        self.imageInfTableWidget.setRowCount(0)
        self.imageInfTableWidget.setColumnCount(15)  # 暂定14行 信息
        tableHorizontalHeaderLabel = ['id', '序号', '项目编号', '项目名称', '文件名', '项目类型', '桥梁类型1', '桥梁类型2',
                                      '材料类型', '桥梁风格', '桥梁规模', '桥梁跨径', '建成状态', '文件本机地址', '文件指向储存地址']
        self.imageInfTableWidget.setHorizontalHeaderLabels(tableHorizontalHeaderLabel)
    # self.imageInfTableWidget.setColumnHidden(0, True)   # 隐藏列  id  文件本机地址  指向存储地址
    # self.imageInfTableWidget.setColumnHidden(12, True)
    # self.imageInfTableWidget.setColumnHidden(13, True)
        self.imageInfTableWidget.setShowGrid(True)

        # 添加图片并展示在 中间窗口,待修改
        self.loadImagePushButton.clicked.connect(self.loadImage)
        self.importFolderPushButton.clicked.connect(self.loadFolderImage)
        # print(data)

        # 效果展示 框内的 右击展示菜单 上下文菜单
        # 允许控件 响应事件
        self.MainPictrueTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.MainPictrueTable.customContextMenuRequested.connect(self.generateMenu)

    def generateMenu(self, pos):
        '''pos 鼠标点击的位置'''
        print(pos)

        # 判断单击的是第几行
        for i in self.MainPictrueTable.selectionModel().selection().indexes():
            rowNum = i.column()  # 当前选择的 行数
        # 如果选择的行索引小于2 ，跳出菜单
        if rowNum < 1:
            menu = QMenu()
            item1 = menu.addAction('放大')
            item2 = menu.addAction('菜单项2')

            screenPos = self.MainPictrueTable.mapToGlobal(pos)
            # 被阻塞
            action = menu.exec(screenPos)
            if action == item1:
                print('选择了菜单1')

    def loadImage(self):
        fnames, _ = QFileDialog.getOpenFileNames(self, '打开文件', '.', '图像文件(*.jpg *.png )')  # 传入多个文件
        if len(fnames) == 0:
            self.statusbar.showMessage('未传入效果图', 5000)
            # return
        else:
            # 判断 输入的文件中 有没有文件名和库中文件 冲突的
            tempLs = []
            idLs = []

            for i in fnames:
                id = getMd5(i)  # id 为文件的md5
                # print(id)
                if str(id) in self.dataDict:
                    self.statusbar.showMessage(u'Error: %s 文件名冲突，或文件已录入' % i.split('/')[-1])
                    QMessageBox.critical(self, '错误', '文件名与库中图重复，或文件已录入', QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.Yes)
                    tempLs.append(i)
                else:
                    idLs.append(id)
            for i in fnames:
                if i in tempLs:
                    fnames.remove(i)

            # 展示图片 显示单排的
            tempNum = self.imageInfTableWidget.rowCount()
            # imageNowRow = self.MainPictrueTable.rowCount()
            self.imageInfTableWidget.setRowCount(tempNum + len(fnames))
            self.MainPictrueTable.setRowCount(tempNum + len(fnames))
            for i in range(len(fnames)):
                # itemName = QTableWidgetItem(fnames[i].split('/')[-1])
                # itemName.setTextAlignment(Qt.AlignCenter)
                item = QTableWidgetItem(str(fnames[i].split('/')[-1]))
                item.setIcon(QIcon(fnames[i]))
                item.setTextAlignment(Qt.AlignLeft)
                self.MainPictrueTable.setItem(i + tempNum, 0, item)

                # print(fnames[i])
                filesize = get_FileSize(fnames[i])
                item = QTableWidgetItem(str(filesize) + 'Mb')
                self.MainPictrueTable.setItem(i + tempNum, 2, item)

                item = QTableWidgetItem(str(fnames[i].split('.')[-1]))
                self.MainPictrueTable.setItem(i + tempNum, 1, item)
            self.statusbar.showMessage('成功读取效果图', 5000)

    def loadFolderImage(self):
        # print('anniu biean')
        directoryOpen = QFileDialog.getExistingDirectory(self, '选取文件夹', './')
        if directoryOpen == '':
            self.statusbar.showMessage('未传入项目效果图', 5000)
            # return
        else:
            dialog = DirectoryInputWindow()
            if dialog.exec_() == QDialog.Accepted:
                self.statusbar.showMessage('保存项目组内效果图成功', 5000)
            else:
                self.statusbar.showMessage('项目组内效果图保存失败', 5000)
        # print(directoryOpen)


class DirectoryInputWindow(QDialog, folderInputWindow):
    def __init__(self, parent=None):
        super(DirectoryInputWindow, self).__init__(parent)
        self.setupUi(self)


class MyloginWindow(QDialog, loginWindow):
    def __init__(self, parent=None):
        super(MyloginWindow, self).__init__(parent)
        self.setupUi(self)
        # self.lineName.setText('123')
        self.OkPushButton.clicked.connect(self.loginfunction)
        self.VisitorLogin.clicked.connect(self.visitorLogin)
        # ''' 此处有问题
        if os.path.exists('data/pass.ini'):
            with open('data/pass.ini', 'r', encoding='utf-8') as frlines:
                for line in frlines:
                    line = line.strip('\n')
                    if line.split(':')[0] == 'username':
                        self.lineName.setText(str(line.split(':')[-1]))
                    else:
                        self.linePassword.setText(str(line.split(':')[-1]))
            # Current_user = str(self.lineName.text())
            # password_input = str(self.linePassword.text())
            # if password_input == '123' and Current_user == '123' :
            #   passwd_check = True
            #   username_check = True
            #   self.accept()
            # '''

    def loginfunction(self):
        # global Current_user
        Current_user = str(self.lineName.text())
        password_input = str(self.linePassword.text())
        passwd_check = False
        username_check = False
        if password_input == '123' and Current_user == '123':
            passwd_check = True
            username_check = True
        else:
            QMessageBox.warning(self, "Error", u'您输入的账号或密码有误 ！！!',
                                buttons=QMessageBox.Ok, defaultButton=QMessageBox.Ok)
        if username_check and passwd_check:
            if self.RemeberPw.isChecked():
                # date = {}
                # data['username'] = str(Current_user)
                # data['Password'] = str(password_input)
                strline = 'username:' + Current_user + '\npassword:' + password_input
                fw = open('data/pass.ini', 'w+', encoding='utf-8 ')
                fw.write(strline)
                fw.close()
            global adminlogin
            adminlogin = 1
            self.accept()

    def visitorLogin(self):
        self.accept()


if __name__ == "__main__":

    # global adminlogin
    adminlogin = 0
    app = QApplication(sys.argv)
    # 设置程序的图标
    # app.setWindowIcon(QIcon("lufei.ico"))

    dialog = MyloginWindow()
    # dialog.show()
    if dialog.exec_() == QDialog.Accepted:
        main = MyWindow()
        main.show()
    # 登陆设置
    # mainLogin =  MyloginWindow()
    # mainLogin.show()
    sys.exit(app.exec_())
