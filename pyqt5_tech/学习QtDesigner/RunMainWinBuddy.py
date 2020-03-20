import  sys
import MainWinBuddy

from PyQt5.QtWidgets import QApplication,QMainWindow

#  主程序调用
if __name__ == '__main__':
    #  整个程序
    app = QApplication(sys.argv)
    # 创建一个窗口
    mainWindow = QMainWindow()
    # 调用 demo中的ui
    ui =  MainWinBuddy.Ui_MainWindow()
    # 调用 setupUi 的布局
    ui.setupUi(mainWindow)
    # 窗口显示
    mainWindow.show()
    #  主循环，安全退出
    sys.exit(app.exec_())
