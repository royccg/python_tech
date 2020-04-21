from PyQt5.QtWidgets import *
import sys, math


class Calc(QWidget):
    def __init__(self):
        super(Calc, self).__init__()
        self.setWindowTitle('绝对布局')

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Back', '', 'Close',
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+']

        positions = [(i,j) for i in range(5) for j in range(4)]
        # print(positions)
        # print(*(1, 2))  # 元组转换成单个值
        for position, name in zip(positions, names):
            '''
            zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
            然后返回由这些元组组成的列表。
            如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，
            利用 * 号操作符，可以将元组解压为列表。
            '''
            if name == '':
                continue

            button = QPushButton(name)
            grid.addWidget(button, *position)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Calc()
    main.show()
    sys.exit(app.exec_())
