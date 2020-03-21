# 显示控件提示信息
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout
from PyQt5.QtWidgets import  QLabel, QWidget, QToolTip
from PyQt5.QtGui import QPalette, QPixmap
# 导入常量
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    """docstring for QLabelDemo."""

    def __init__(self):
        super(QLabelDemo, self).__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color = yellow>这是一个文本标签<./font>")
        #  设置自动背景
        label1.setAutoFillBackground(True)
        # 创建一个 调色板
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)  #设置背景色
        label1.setPalette(palette)
        # 设置文本居中对齐
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href = '#'> 欢迎使用Python GUI程序</a>")

        label3.setAlignment(Qt.AlignCenter)
        # 设置提示文本
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap('../image/IMG_0180.JPG'))
        # 加入连接,如果设为 True，用浏览器打开网页
        # 如果设为False，调用 槽  函数
        label4.setOpenExternalLinks(True)
        label4.setText('<a href = "https://item.jd.com/12417265.html">感谢关注《Python 从菜鸟到高手》</a>')
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链接')

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)

        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle("Qlabel控件演示")

    def linkHovered(self):
        print('当鼠标滑过label2标签时，触发事件')

    def linkClicked(self):
        print("当鼠标单击label4标签时，触发事件")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置程序的图标
    # app.setWindowIcon(QIcon("lufei.ico"))
    main = QLabelDemo()
    main.show()

    sys.exit(app.exec_())
