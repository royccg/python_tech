from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class DockDemo(QMainWindow):
    def __init__(self, parent=None):
        super(DockDemo, self).__init__(parent)
        self.setWindowTitle('停靠控件（QDockWidget）')

        layout =QHBoxLayout()
        self.items = QDockWidget('Dockable', self)
        self.listWidget = QListWidget()
        self.listWidget.addItem('item1')
        self.listWidget.addItem('item2')
        self.listWidget.addItem('item3')

        #  默认 右边停靠
        self.items.setWidget(self.listWidget)
        self.setCentralWidget(QLineEdit())

        #  默认 右边停靠，设定为 悬浮
        self.items.setFloating(True)
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DockDemo()
    main.show()
    sys.exit(app.exec_())
