import sys
import sqlite3
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QLineEdit, QCheckBox, QInputDialog, QPlainTextEdit, QDesktopWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QTableWidget, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPainter, QColor

kx = 0
ky = 0
km = 0


def set_sizes(widget, size_x, size_y, pos_x, pos_y):
    widget.resize(round(size_x * kx), round(size_y * ky))
    widget.move(round(pos_x * kx), round(pos_y * ky))
    return widget

class Loading_Screen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global kx, ky, km
        self.all_right = False
        self.screen = QDesktopWidget()
        self.size_x = self.screen.width()
        self.size_y = self.screen.height()
        self.size_x = 540
        self.size_y = 1050
        kx = self.size_x / 1080
        ky = self.size_y / 2100
        km = min(kx, ky)
        self.setGeometry(0, 0, round(1080 * kx), round(2100 * ky))
        self.setWindowTitle(' ')

class Loading_Screen2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global kx, ky, km
        self.all_right = False
        self.screen = QDesktopWidget()
        self.size_x = self.screen.width()
        self.size_y = self.screen.height()
        self.size_x = 540
        self.size_y = 1050
        kx = self.size_x / 1080
        ky = self.size_y / 2100
        km = min(kx, ky)
        self.setGeometry(0, 0, round(1080 * kx), round(2100 * ky))
        self.setWindowTitle('loading')


if __name__ == '__main__':
    waiting = True
    app = QApplication(sys.argv)
    ex = Loading_Screen2()

    con = 0
    while waiting:
        if con == '1':
            waiting = False
            ex.close()
            ex = Loading_Screen()
            ex.show()
            sys.exit(app.exec())
        else:
            con = input()
            ex = Loading_Screen2()
            ex.show()
            sys.exit(app.exec())
