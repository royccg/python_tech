
from PyQt5.QtWidgets import *
import sys

class ListWidgetDemo(QMainWindow):
    def __init__(self, parent =None):
        super(ListWidgetDemo, self).__init__(parent)
        self.setWindowTitle('QListWidget Demo')
        self.resize(300, 270)

        self.listwidget = QListWidget()
        self.listwidget.resize(300, 120)
        self.listwidget.addItem("item1")
        self.listwidget.addItem("item2")
        self.listwidget.addItem("item3")
        self.listwidget.addItem("item4")
        self.listwidget.addItem("item5")

        self.listwidget.itemClicked.connect(self.clicked)

        # self.listwidget.setWindowTitle('demo')

        self.setCentralWidget(self.listwidget)

    def clicked(self, Index):
        QMessageBox.information(self, "QListWidget", '您选择了：' + self.listwidget.item(self.listwidget.row(Index)).text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ListWidgetDemo()
    main.show()

    sys.exit(app.exec_())
