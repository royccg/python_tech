# -*- coding: utf-8 -*-
# @Author: royccg
# @Email:roy778555479@gmail.com
# @Date:   2020-04-20 10:43:06
# @Last Modified time: 2020-04-21 21:46:40


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
# from PyQt5 import  QtGui
import sys,os
from UIDesigned_V01 import Ui_MainWindow, loginWindow

class MyWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MyWindow, self).__init__(parent)
		self.setupUi(self)
	def initUI(self):
		pass

class MyloginWindow(QDialog, loginWindow):
	def __init__(self, parent=None):
		super(MyloginWindow, self).__init__(parent)
		self.setupUi(self)
		''' 此处有问题
		if os.path.exists('data/pass.ini'):
			with open('data/pass.ini','r',encoding='utf-8') as frlines:
				for line in frlines:
					line = line.strip('\n')
					if line.split(':')[0] == 'username':
						self.lineName.setText = line.split(':')[-1]
					else:
						self.linePassword.setText = line.split(':')[-1]
			self.accept()
			'''
		self.OkPushButton.clicked.connect(self.loginfunction)
		self.VisitorLogin.clicked.connect(self.visitorLogin)

	def loginfunction(self):
		# global Current_user
		Current_user = str(self.lineName.text())
		password_input = str(self.linePassword.text())
		passwd_check = False
		username_check = False
		if password_input == '123' and Current_user == '123' :
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
				strline = 'username: '+Current_user +'\npassword:' + password_input
				fw =  open('data/pass.ini','w+', encoding = 'utf-8 ' )
				fw.write(strline )
				fw.close()
			self.accept()

	def visitorLogin(self):
		self.accept()


if __name__ == "__main__":
	global passok
	passok = 0
	app = QApplication(sys.argv)
	# 设置程序的图标
	# app.setWindowIcon(QIcon("lufei.ico"))
	dialog =  MyloginWindow()
	# dialog.show()
	if dialog.exec_()  == QDialog.Accepted:
		main  =  MyWindow()
		main.show()
    # 登陆设置
    # mainLogin =  MyloginWindow()
    # mainLogin.show()
	sys.exit(app.exec_())