import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 200)

        button = QPushButton(self)
        button.move(100, 50)
        button.clicked.connect(self.on_click)

    def on_click(self):
        print('Button clicked')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())