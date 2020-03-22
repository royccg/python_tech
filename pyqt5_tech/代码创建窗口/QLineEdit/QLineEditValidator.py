
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys

class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('校验器')

        # 创建表单布局
        formLayout = QFormLayout()

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        formLayout.addRow('整数类型', intLineEdit)
        formLayout.addRow('浮点类型', doubleLineEdit)
        formLayout.addRow('数值和字母', validatorLineEdit)

        intLineEdit.setPlaceholderText("整数")
        doubleLineEdit.setPlaceholderText('浮点数')
        validatorLineEdit.setPlaceholderText('字母和数字')

        # 整数校验器 [1,99]
        intValidator = QIntValidator(self)
        intValidator.setRange(1,99)

        # 浮点校验器 [-360,360],精度：小数点后两位
        doubleValidator =  QDoubleValidator(self)
        doubleValidator.setRange(-360,360)
        # 标准的表示方式
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # 设置精度，小数点后两位
        doubleValidator.setDecimals(2)

        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        # 设置校验器
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置程序的图标
    # app.setWindowIcon(QIcon("lufei.ico"))
    main = QLineEditValidator()
    main.show()

    sys.exit(app.exec_())
