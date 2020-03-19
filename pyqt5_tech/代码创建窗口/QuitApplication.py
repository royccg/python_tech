import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(300, 120)
        self.setWindowTitle("退出应用程序")

        # 添加BUtton
        self.button1 = QPushButton("退出程序")
        # 信号绑定
        self.button1.clicked.connect(self.onClick_Button)

        # 水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    # 按钮单击时间的方法
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + "按钮被按下")
        app = QApplication.instance()
        # 退出应用程序
        app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())
