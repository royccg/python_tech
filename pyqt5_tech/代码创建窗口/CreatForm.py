# QDesktopWidget
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget

# 添加图标
# from PyQt5.QtGui import QIcon


# 面向对象编程，编写类
class CenterForm(QMainWindow):
    #  初始化，
    def __init__(self, parent=None):
        # 定义父类
        super(CenterForm, self).__init__(parent)

        # 设置主窗口的标题
        self.setWindowTitle("让窗口居中")

        # 设置主窗口的尺寸
        self.resize(400, 300)

    # 居中的方法
    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width())/2
        newTop = (screen.height() - size.height())/2
        self.move(newLeft, newTop)
        # 状态栏
        # self.status = self.statusBar()
        # self.status.showMessage("只存在5秒的消息",5000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置程序的图标
    # app.setWindowIcon(QIcon("lufei.ico"))

    main = CenterForm()
    main.show()

    sys.exit(app.exec_())
