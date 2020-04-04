from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class TreeEvent(QMainWindow):
    def __init__(self):
        super(TreeEvent, self).__init__()
        self.setWindowTitle('为树节点添加响应事件')

        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['Key', 'Value'])

        # 设定根节点
        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'root')
        root.setText(1, '0')

        # 设定子节点1
        child1 = QTreeWidgetItem(root)  # 属于根节点的 子节点
        child1.setText(0, 'child1')
        child1.setText(1, '1')

        # 设定子节点2
        child2 = QTreeWidgetItem(root)  # 属于根节点的 子节点
        child2.setText(0, 'child2')
        child2.setText(1, '2')

        # 设定子节点2的子节点
        child3 = QTreeWidgetItem(child2)  # 属于根节点的 子节点
        child3.setText(0, 'child3')
        child3.setText(1, '3')

        self.tree.clicked.connect(self.onTreeClicked)
        self.setCentralWidget(self.tree)

    def onTreeClicked(self, index):
        item = self.tree.currentItem()
        print(index.row())
        print('key = %s,value =%s' %(item.text(0),item.text(1)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TreeEvent()
    main.show()
    sys.exit(app.exec_())
