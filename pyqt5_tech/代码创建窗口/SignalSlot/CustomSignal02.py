from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys, math


class MyTypeSignal(QObject):
    # 定义一个信号
    sendmsg = pyqtSignal(object)

    # 发送3哥参数的信号
    sendmsg1 = pyqtSignal(str, int, int)

    def run(self):
        self.sendmsg.emit('Hello PyQt5')

    def run1(self):
        self.sendmsg1.emit('hello', 3, 4)

class MySlot(QObject):
    def get(self, msg):
        print('信息' +msg)

    def get1(self, msg, a, b):
        print(msg)
        print(a+b)

if __name__ == "__main__":
    send = MyTypeSignal()
    slot = MySlot()
    send.sendmsg.connect(slot.get)
    send.sendmsg1.connect(slot.get1)
    send.run()
    send.run1()
