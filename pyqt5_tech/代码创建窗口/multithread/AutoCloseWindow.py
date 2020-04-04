from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel('<font color = red size =140><b>hello world, 窗口在5秒后自动关闭!</b></font>')
    label.setWindowFlags(Qt.SplashScreen  | Qt.FramelessWindowHint)
    label.show()
    QTimer.singleShot(5000, app.quit)

    sys.exit(app.exec_())
