from PyQt5.QtWidgets import *
import sys

class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTextEdit控件演示')

        self.resize(300,320)

        self.textEdit = QTextEdit()
        self.buttonText = QPushButton('显示文本')
        self.buttonHTML = QPushButton('显示HTML')

        self.buttonTextToText = QPushButton('获取文本')
        self.buttonHTMLToHtml = QPushButton('获取HTML')

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHTML)
        layout.addWidget(self.buttonTextToText)
        layout.addWidget(self.buttonHTMLToHtml)

        self.setLayout(layout)

        self.buttonText.clicked.connect(self.onClick_ButtonText)
        self.buttonHTML.clicked.connect(self.onClick_ButtonHTML)

        self.buttonTextToText.clicked.connect(self.onClick_ButtonTextToText)
        self.buttonHTMLToHtml.clicked.connect(self.onClick_ButtonHTMLToHtml)



    def onClick_ButtonText(self):
        self.textEdit.setPlainText('Hello World，世界你好！')

    def onClick_ButtonHTML(self):
        self.textEdit.setHtml('<font color = "blue" size = "5">Hello World </font>')

    def onClick_ButtonTextToText(self):
        print(self.textEdit.toPlainText())

    def onClick_ButtonHTMLToHtml(self):
        print(self.textEdit.toHtml())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = QTextEditDemo()
    main.show()

    sys.exit(app.exec_())
