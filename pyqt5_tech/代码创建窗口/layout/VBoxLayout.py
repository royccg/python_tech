from PyQt5.QtWidgets import *
import sys, math


class VBoxLayout(QWidget):
    def __init__(self):
        super(VBoxLayout, self).__init__()
        self.setWindowTitle('垂直盒布局')

        vlayout = QVBoxLayout()
        vlayout.addWidget(QPushButton('按钮1'))
        vlayout.addWidget(QPushButton('按钮2'))
        vlayout.addWidget(QPushButton('按钮3'))
        vlayout.addWidget(QPushButton('按钮4'))
        vlayout.addWidget(QPushButton('按钮5'))
        vlayout.setSpacing(40) # 控制空间的间距
        self.setLayout(vlayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = VBoxLayout()
    main.show()
    sys.exit(app.exec_())
