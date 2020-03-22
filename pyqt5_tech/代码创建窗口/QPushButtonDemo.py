from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton Demo')

        layout = QVBoxLayout()

        self.button1 = QPushButton('第1个按钮')
        self.button1.setText("First Button1")

        # 默认选中的状态
        self.button1.setCheckable(True)
        self.button1.toggle() # 设定未选中的状态

        # 调用lambda表达式
        self.button1.clicked.connect(lambda:self.whichButton(self.button1))
        self.button1.clicked.connect(self.buttonState)

        layout = QVBoxLayout()
        layout.addWidget(self.button1)

        # 在文本前面显示图像
        self.button2 = QPushButton("图像显示")
        self.button2.setIcon(QIcon(QPixmap('lufei.ico')))
        self.button2.clicked.connect(lambda :self.whichButton(self.button2))
        layout.addWidget(self.button2)

        self.button3 = QPushButton("不可用的按钮")
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        # 设置默认按钮,在窗口 按 回车键 就能自动调用
        self.button4 = QPushButton('&MyButton')
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda: self.whichButton(self.button4))
        layout.addWidget(self.button4)

        self.setLayout(layout)
        self.resize(400,300)

#  查看那个按钮被单击了，此处通过传参数的方式
    def whichButton(self, btn):
        print('被单击的按钮是<' + btn.text() +'>')

    def buttonState(self):
        if self.button1.isChecked():
            print('按钮1已经被选中')
        else:
            print('按钮1未被选中')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()

    sys.exit(app.exec_())
