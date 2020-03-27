
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSliderDemo')
        self.resize(300,500)

        layout = QVBoxLayout()
        self.label = QLabel('你好，PyQt5')
        self.label.setAlignment(Qt.AlignCenter) #居中显示

        layout.addWidget(self.label)

        self.slider = QSlider(Qt.Horizontal)  # 水平滑块

        # 设置最小值
        self.slider.setMinimum(12)
        # 设置最大值
        self.slider.setMaximum(48)
        # 设置步长
        self.slider.setSingleStep(3)
        # 设置当前值
        self.slider.setValue(18)
        # 设置刻度的位置，在下方
        self.slider.setTickPosition(QSlider.TicksBelow)
        # 设置刻度的间隔
        self.slider.setTickInterval(6)
        layout.addWidget(self.slider)

        self.slider.valueChanged.connect(self.valueChanged)

        self.slider1 = QSlider(Qt.Vertical)
        layout.addWidget(self.slider1)
        self.slider1.setMinimum(10)
        self.slider1.setMaximum(60)
        self.slider1.setSingleStep(5)
        self.slider1.setValue(18)
        self.slider1.setTickPosition(QSlider.TicksLeft)
        self.slider1.valueChanged.connect(self.valueChanged)

        self.setLayout(layout)

    def valueChanged(self):
        # sender  当前操作控件
        print('当前值：%s' % self.sender().value())
        size = self.sender().value()
        self.label.setFont(QFont('Arial',size))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()

    sys.exit(app.exec_())
