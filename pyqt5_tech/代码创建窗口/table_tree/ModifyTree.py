from PyQt5.QtWidgets import *
import sys

class ModifyTree(QWidget):
    def __init__(self, parent = None):
        super(ModifyTree, self).__init__(parent)
        self.setWindowTitle('TreeWidget 例子')

        operatorLayout = QHBoxLayout()
        addBtn = QPushButton('添加节点')
        updateBtn = QPushButton('修改节点')
        deleteBtn = QPushButton('删除节点')

        operatorLayout.addWidget(addBtn)
        operatorLayout.addWidget(updateBtn)
        operatorLayout.addWidget(deleteBtn)

        addBtn.clicked.connect(self.addNode)
        updateBtn.clicked.connect(self.updateNode)
        deleteBtn.clicked.connect(self.deleteNode)

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

        mainLayout = QVBoxLayout(self)
        mainLayout.addLayout(operatorLayout)
        mainLayout.addWidget(self.tree)
        self.setLayout(mainLayout)

    def addNode(self): # 添加节点
        print('添加节点')
        item = self.tree.currentItem()
        print(item)
        node = QTreeWidgetItem(item)
        node.setText(0, '新节点')
        node.setText(1, '新值')
        # pass

    def updateNode(self):
        print('修改节点')
        item = self.tree.currentItem()
        item.setText(0, '修改节点')
        item.setText(1, '值已经被修改')

    def deleteNode(self):
        print('删除节点')
        item =self.tree.currentItem()
        root = self.tree.invisibleRootItem() # 根是不可见的
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)

    def onTreeClicked(self, index):
        item = self.tree.currentItem()
        print(index.row())
        print('key = %s,value =%s' %(item.text(0),item.text(1)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ModifyTree()
    main.show()
    sys.exit(app.exec_())
