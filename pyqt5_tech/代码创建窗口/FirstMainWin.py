import sys
from PyQt5.QtWidgets import QMainWindow,QApplication

# 添加图标
from PyQt5.QtGui import QIcon

# 面向对象编程，编写类
class FirstMainWin(QMainWindow):
    #  初始化，
    def __init__(self,parent =None):
        # 定义父类
        super(FirstMainWin,self).__init__(parent)

        # 设置主窗口的标题
        self.setWindowTitle("第一个主窗口应用")

        # 设置主窗口的尺寸
        self.resize(500,300)
        # 状态栏
        self.status = self.statusBar()

        self.status.showMessage("只存在5秒的消息",5000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置程序的图标
    app.setWindowIcon(QIcon("lufei.ico"))
    main = FirstMainWin()
    main.show()

    sys.exit(app.exec_())
