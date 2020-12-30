# -*- coding: utf-8 -*-
# @Author: royccg
# @Email:roy778555479@gmail.com
# @Date:   2020-04-24 18:51:44
# @Last Modified time: 2020-04-24 18:55:09

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
	def setupUi(self, mainWindow):
		mainWindow.setobjectName('mainWindow')
		mainWindow.setEnabled(True)
		mainWindow.resize(200,480)

		self.centralWidget = QtWidgets.QWidget(mainWindow)
		self.centralWidget.setobjectName('centralWidget')

		# 设定一个主的竖向布局
		self.VBoxMain = QtWidgets.QVBoxLayout(self.centralWidget)
		self.VBoxMain.setobjectName('VBoxMain')

		
