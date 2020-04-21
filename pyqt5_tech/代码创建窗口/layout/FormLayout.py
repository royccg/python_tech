from PyQt5.QtWidgets import *
import sys, math


class Formlayout(QWidget):
    def __init__(self):
        super(Formlayout, self).__init__()
        self.setWindowTitle('表单布局')

        formLayout = QFormLayout()

        titleLabel = QLabel('标题:')
        authorLabel = QLabel('作者:')
        contentLabel = QLabel('内容:')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        contentEdit = QTextEdit()

        formLayout.addRow(titleLabel, titleEdit)
        formLayout.addRow(authorLabel, authorEdit)
        formLayout.addRow(contentLabel, contentEdit)

        self.setLayout(formLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Formlayout()
    main.show()
    sys.exit(app.exec_())
