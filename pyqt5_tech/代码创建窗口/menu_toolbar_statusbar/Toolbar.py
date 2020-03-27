from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class Toolbar(QMainWindow):
    def __init__(self):
        super(Toolbar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('工具栏例子')
        self.resize(300, 200)

        tb1 = self.addToolBar('File')
        # 工具栏默认按钮：只显示图标，  将文本作为悬停提示
        new = QAction(QIcon('new.png'), 'new', self)
        tb1.addAction(new)
        open = QAction(QIcon('open.png'), 'open', self)
        tb1.addAction(open)

        save = QAction(QIcon('save.png'), 'save', self)
        tb1.addAction(save)

        tb1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        '''
        ToolButtonTextBesideIcon :文本在右侧显示
        ToolButtonIconOnly : 只显示图标
        ToolButtonTextOnly : 只显示文本
        ToolButtonTextUnderIcon: 底下显示文本
        ToolButtonFollowStyle: 跟随显示
        '''
        #  有的按钮显示文本 有的不显示，创建两个tools
        tb2 = self.addToolBar('File1')
        new1 = QAction(QIcon('new'), '新建', self)
        tb2.addAction(new1)

        tb2.setToolButtonStyle(Qt.ToolButtonTextOnly)

        tb1.actionTriggered.connect(self.toolbtnpressed)

    def toolbtnpressed(self, a):
        print('按下的工具栏按钮是', a.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Toolbar()
    main.show()
    sys.exit(app.exec_())
