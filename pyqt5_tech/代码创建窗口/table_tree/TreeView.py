from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)

    model = QDirModel()
    tree = QTreeView()
    tree.setModel(model)

    tree.setWindowTitle('QTreeView')
    tree.resize(600, 400)
    tree.show()

    sys.exit(app.exec_())
