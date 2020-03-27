from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QIcon
import sys

class BasicTreeWidget(QMainWindow):
    def __init__(self):
        super(BasicTreeWidget, self).__init__()
        self.setWindowTitle('树控件（QTreeWidget）的基本用法')

        self.tree = QTreeWidget()
        # 为树控件指定列数
        self.tree.setColumnCount(2)

        # 指定列标签
        self.tree.setHeaderLabels(['Key', 'Value'])

        # 设定根节点
        root = QTreeWidgetItem(self.tree)
        root.setText(0, '根节点')
        root.setIcon(0, QIcon('new.png'))
        self.tree.setColumnWidth(0, 160)

        # 设定子节点1
        child1 = QTreeWidgetItem(root)  # 属于根节点的 子节点
        child1.setText(0, '子节点1')
        child1.setText(1, '子节点1的数据')
        child1.setIcon(0, QIcon('new.png'))
        child1.setCheckState(0, Qt.Checked) # 添加复选框

        # 设定子节点2
        child2 = QTreeWidgetItem(root)  # 属于根节点的 子节点
        child2.setText(0, '子节点2')
        child2.setIcon(0, QIcon('new.png'))
        child2.setCheckState(0, Qt.Checked) # 添加复选框

        # 设定子节点2的子节点
        child3 = QTreeWidgetItem(child2)  # 属于根节点的 子节点
        child3.setText(0, '子节点2-1')
        child3.setText(1, '子节点2-1的数据')
        child3.setIcon(0, QIcon('new.png'))
        child3.setCheckState(0, Qt.Checked) # 添加复选框

        self.tree.expandAll()

        self.setCentralWidget(self.tree)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = BasicTreeWidget()
    main.show()

    sys.exit(app.exec_())
