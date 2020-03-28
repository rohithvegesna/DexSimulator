import sys
import time
import threading
import serial
from uicontroller import *

global serialport
serialport = serial.Serial("COM2", 19200, timeout=0.5)


def hello():
    global myapp
    global serialport
    c = serialport.read()
    print(c)
    threading.Timer(0.5, hello).start()


if __name__ == "__main__":
    global myapp
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    hello()
    app.exec_()
