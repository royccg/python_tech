from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
import os

class WebEngineView(QMainWindow):
    def __init__(self):
        super(WebEngineView, self).__init__()
        self.setWindowTitle('显示嵌入Web页面')
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        self.browser.setHtml(
        '''
        <!DOCTYPE html>
        <html lang ='en'>
        <head>
            <meta charset="UTF-8">
            <title>测试页面</title>

        </head>
        <body>
            <h1> hello PyQt5</h1>
            <h2> hello PyQt5</h2>
            <h3> hello PyQt5</h3>
            <h4> hello PyQt5</h4>
        </body>
        </html>
        '''
        )
        # self.browser.load(QUrl.fromLocalFile(url))
        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = WebEngineView()
    main.show()
    sys.exit(app.exec_())
