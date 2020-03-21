import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
```
窗口的setWindowIcon方法 用于设置窗口的图标，只能在window上可用

QApplicaton 中的setWindowIcon方法用于设置主窗口的图标和应用程序的图标，但调用了窗口的setWindowIcon方法
QApplicaton 中的setWindowIcon方法就只能用于设置应用程序图标了
```

# 添加图标
from PyQt5.QtGui import QIcon

# 面向对象编程，编写类
class IconForm(QMainWindow):
    #  初始化，
    def __init__(self):
        # 定义父类
        super(IconForm,self).__init__()
        # 合并控件的设置
        self.initUI()

    def initUI(self):
        # 同时设置窗口的尺寸和位置
        self.setGeometry(300,300,250,250)
        # 设置主窗口的标题
        self.setWindowTitle("设置窗口图标")
        # 设置窗口图标
        self.setWindowIcon(QIcon("lufei.ico"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置程序的图标
    # app.setWindowIcon(QIcon("lufei.ico"))
    main = IconForm()
    main.show()

    sys.exit(app.exec_())
