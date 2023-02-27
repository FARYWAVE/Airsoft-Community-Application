import socket
from threading import Thread
from PyQt5 import *
from PyQt5.QtWidgets import QApplication, QMainWindow

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

import sys


app = QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle("Начало")
win.setGeometry(0, 0, 500, 500)
win2 = QMainWindow()
win2.setWindowTitle("Нашёл")
win2.setGeometry(100, 100, 500, 500)
win.show()
i = 0
while 1:
    try:
        s.connect(('176.99.158.212', 7777))
        win.close()
        win2.show()
        break
    except WindowsError:
        i += 1
        print(i)


class GetMsg(Thread):
    def run(self):
        while True:
            data = s.recv(1024)
            if not data.decode('utf-8') == "":
                print(data.decode('utf-8'), end='\n')


class SendMsg(Thread):
    def run(self):
        while True:
            inp = input()
            s.sendall(inp.encode('utf-8'))


if __name__ == '__main__':
    get = GetMsg().start()
    snd = SendMsg().start()