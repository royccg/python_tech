from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DateDialog(QDialog):
	"""docstring for DateDialog"""
	def __init__(self, parent= None):
		super(DateDialog, self).__init__(parent)
		self.setWindowTitle('DateDialog')

		layout = QVBoxLayout(self)
		self.datetime = QDateTimeEdit(self)
		self.datetime.setCalendarPopup(True) # 弹出
		self.datetime.setDateTime(QDateTime.currentDateTime()) # 显示当前日期

		layout.addWidget(self.datetime)

		buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self) # 按钮盒子
		buttons.accepted.connect(self.accept)  # ok
		buttons.rejected.connect(self.reject)  # cancel

		layout.addWidget(buttons)

	def dateTime(self): #获得当前日期
		return self.datetime.dateTime()

	@staticmethod
	def getDateTime(parent =None):
		dialog = DateDialog(parent)
		result = dialog.exec()
		date = dialog.dateTime()
		return(date.date(), date.time(), result == QDialog.Accepted)

