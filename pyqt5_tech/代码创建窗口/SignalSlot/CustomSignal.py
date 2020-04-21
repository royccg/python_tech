from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys, math


class MyTypeSignal(QObject):
    # 定义一个信号
    sendmsg = pyqtSignal(object)

    def run(self):
        self.sendmsg.emit('Hello PyQt5')

class MySlot(QObject):
    def get(self, msg):
        print('信息' +msg)

if __name__ == "__main__":
    send = MyTypeSignal()
    slot = MySlot()
    send.sendmsg.connect(slot.get)
    send.run()

    # 断开连接
    send.sendmsg.disconnect(slot.get)
    send.run()
