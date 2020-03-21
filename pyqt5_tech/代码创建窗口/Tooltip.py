# 显示控件提示信息
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout
from PyQt5.QtWidgets import QToolTip, QPushButton, QWidget
from PyQt5.QtGui import QFont


# 面向对象编程，编写类
class TooltipForm(QMainWindow):
    def __init__(self):
        super().__init__()
        # 合并控件的设置
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("SansSerif",12))
        self.setToolTip("今天<b>星期五</b>")
        # 同时设置窗口的尺寸和位置
        self.setGeometry(300,300,200,300)
        self.setWindowTitle("设置控件提示信息")

        # 添加BUtton
        self.button1 = QPushButton("我的按钮")
        self.button1.setToolTip('这是一个按钮，Are you OK?')
        # 水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置程序的图标
    # app.setWindowIcon(QIcon("lufei.ico"))
    main = TooltipForm()
    main.show()

    sys.exit(app.exec_())
