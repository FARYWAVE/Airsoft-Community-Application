import sys
import sqlite3
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QLineEdit, QCheckBox, QInputDialog, QPlainTextEdit, QDesktopWidget, \
    QComboBox
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QTableWidget, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPainter, QColor, QIcon

kx = 0
ky = 0
km = 0

profile_on = ''
profile_off = ''
games_on = ''
games_off = ''
team_on = ''
team_off = ''
create_on = ''
create_off = ''


def set_sizes(widget, size_x, size_y, pos_x, pos_y):
    widget.resize(round(size_x * kx), round(size_y * ky))
    widget.move(round(pos_x * kx), round(pos_y * ky))
    return widget


class Loading_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global kx, ky, km
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
        self.size = QDesktopWidget()
        self.info = str(self.size.width()) + ' ' + str(self.size.height())
        self.data = QLabel(self)
        self.data.setText(self.info)
        start()


class Registration_Window(QWidget):  # Создаем окно регистрации
    def __init__(self):
        super().__init__()
        self.save = False
        self.nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                     '0']  # Элементы, которые останутся в номере после преобразований
        self.initUI()
        self.cams = [False, False, False, False, False, False, False]  # Камуфляжи выбраннные игроком
        self.type_chosen = False
        self.end_type = "SQB (120м/c)"

    def initUI(self):
        self.setGeometry(0, 0, round(1080 * kx), round(2100 * ky))
        self.setWindowTitle('Регистрация')

        self.welcome = QLabel(self)
        self.welcome.setText('<h1 style="color: rgb(0, 0, 0);">Приветствуем!</h1>')
        self.welcome = set_sizes(self.welcome, 900, 100, 260, 50)
        self.welcome.setFont(QFont('Calibri', round(14 * km) * 2))

        self.please = QLabel(self)
        self.please.setText("Зарегистрируйтесь чтобы продолжить")
        self.please = set_sizes(self.please, 900, 100, 200, 120)
        self.please.setFont(QFont('Calibri', round(14 * km) * 2))

        self.enter = QPushButton('войти', self)  # Кнопка для перехода к окну входа
        self.enter = set_sizes(self.enter, 180, 70, 650, 1750)
        self.enter.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter.clicked.connect(self.open_enter_window)

        self.hate = QLabel(self)
        self.hate.setText("Уже зарегистрированы?")
        self.hate.setFont(QFont('Calibri', round(18 * km) * 2))
        self.hate = set_sizes(self.hate, 600, 70, 60, 1750)

        self.enter_number = QLabel(self)  # Поля для ввода данных
        self.enter_number.setText("Номер телефона")
        self.enter_number.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_number = set_sizes(self.enter_number, 500, 100, 60, 250)

        self.input_number = QLineEdit(self)
        self.input_number = set_sizes(self.input_number, 500, 60, 500, 270)
        self.input_number.setFont(QFont('Calibri', round(18 * km) * 2))

        self.enter_pw = QLabel(self)
        self.enter_pw.setText("Пароль")
        self.enter_pw.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_pw = set_sizes(self.enter_pw, 500, 100, 60, 320)

        self.input_pw = QLineEdit(self)
        self.input_pw = set_sizes(self.input_pw, 500, 60, 500, 340)
        self.input_pw.setFont(QFont('Calibri', round(18 * km) * 2))

        self.enter_name = QLabel(self)
        self.enter_name.setText("Фамилия и Имя")
        self.enter_name.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_name = set_sizes(self.enter_name, 500, 100, 60, 390)

        self.input_name = QLineEdit(self)
        self.input_name = set_sizes(self.input_name, 500, 60, 500, 410)
        self.input_name.setFont(QFont('Calibri', round(18 * km) * 2))

        self.enter_nick = QLabel(self)
        self.enter_nick.setText("Позывной")
        self.enter_nick.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_nick = set_sizes(self.enter_nick, 500, 100, 60, 460)

        self.input_nick = QLineEdit(self)
        self.input_nick = set_sizes(self.input_nick, 500, 60, 500, 480)
        self.input_nick.setFont(QFont('Calibri', round(18 * km) * 2))

        self.enter_date = QLabel(self)
        self.enter_date.setText("Дата рождения")
        self.enter_date.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_date = set_sizes(self.enter_date, 500, 100, 60, 530)

        self.input_date = QLineEdit(self)
        self.input_date = set_sizes(self.input_date, 500, 60, 500, 550)
        self.input_date.setFont(QFont('Calibri', round(18 * km) * 2))

        self.enter_cam = QLabel(self)
        self.enter_cam.setText("Камуфляж")
        self.enter_cam.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_cam = set_sizes(self.enter_cam, 500, 100, 60, 600)

        self.mc = QCheckBox('MC', self)
        self.mc = set_sizes(self.mc, 200, 100, 510, 600)
        self.mc.stateChanged.connect(self.MC)
        self.mc.setFont(QFont('Calibri', round(18 * km) * 2))

        self.mox = QCheckBox('MOX', self)
        self.mox = set_sizes(self.mox, 200, 100, 770, 600)
        self.mox.stateChanged.connect(self.MOX)
        self.mox.setFont(QFont('Calibri', round(18 * km) * 2))

        self.emr = QCheckBox('EMP', self)
        self.emr = set_sizes(self.emr, 200, 100, 510, 670)
        self.emr.stateChanged.connect(self.EMR)
        self.emr.setFont(QFont('Calibri', round(18 * km) * 2))

        self.bk = QCheckBox('BK', self)
        self.bk = set_sizes(self.bk, 200, 100, 770, 670)
        self.bk.stateChanged.connect(self.BK)
        self.bk.setFont(QFont('Calibri', round(18 * km) * 2))

        self.tan = QCheckBox('TAN', self)
        self.tan = set_sizes(self.tan, 200, 100, 510, 740)
        self.tan.stateChanged.connect(self.TAN)
        self.tan.setFont(QFont('Calibri', round(18 * km) * 2))

        self.olive = QCheckBox('OLIVE', self)
        self.olive = set_sizes(self.olive, 200, 100, 770, 740)
        self.olive.stateChanged.connect(self.OLIVE)
        self.olive.setFont(QFont('Calibri', round(18 * km) * 2))

        self.other = QCheckBox('ДРУГОЙ', self)
        self.other = set_sizes(self.other, 300, 100, 510, 810)
        self.other.stateChanged.connect(self.OTHER)
        self.other.setFont(QFont('Calibri', round(18 * km) * 2))

        self.enter_type = QLabel(self)
        self.enter_type.setText("Тип игрока")
        self.enter_type.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_type = set_sizes(self.enter_type, 500, 100, 60, 890)

        self.choose_type = QComboBox(self)
        self.choose_type.addItems(["SQB (120м/c)", "Штурмовик (150м/с)", "Снайпер (170м/c)"])
        self.choose_type.setFont(QFont('Calibri', round(18 * km) * 2))
        self.choose_type = set_sizes(self.choose_type, 500, 60, 490, 910)
        self.choose_type.activated[str].connect(self.TYPE)

        self.input = QPushButton('Регистрация', self)
        self.input = set_sizes(self.input, 380, 90, 350, 1090)
        self.input.clicked.connect(self.register)
        self.input.setFont(QFont('Calibri', round(22 * km) * 2))

        self.error = QLabel(self)
        self.error.setText('<h1 style="color: rgb(150, 0, 0);">⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h1>')
        self.error.setFont(QFont('Calibri', round(10 * km) * 2))
        self.error = set_sizes(self.error, 910, 90, 60, 1850)

        self.remember = QCheckBox('Запомнить меня', self)
        self.remember = set_sizes(self.remember, 410, 90, 335, 1000)
        self.remember.stateChanged.connect(self.rem)
        self.remember.setFont(QFont('Calibri', round(18 * km) * 2))

    def TYPE(self, text):
        self.end_type = text

    def rem(self, a):  # функция для кнопки запомнить меня
        if a == Qt.Checked:
            self.save = True
        else:
            self.save = False

    def open_enter_window(self):  # Открываем окно для входа
        self.Enter_Window = Enter_Window()
        self.Enter_Window.show()
        self.close()

    # Функции для добавления камуфляжей

    def MC(self, a):
        if a == Qt.Checked:
            self.cams[0] = True
        else:
            self.cams[0] = False

    def MOX(self, a):
        if a == Qt.Checked:
            self.cams[1] = True
        else:
            self.cams[1] = False

    def EMR(self, a):
        if a == Qt.Checked:
            self.cams[2] = True
        else:
            self.cams[2] = False

    def BK(self, a):
        if a == Qt.Checked:
            self.cams[3] = True
        else:
            self.cams[3] = False

    def TAN(self, a):
        if a == Qt.Checked:
            self.cams[4] = True
        else:
            self.cams[4] = False

    def OLIVE(self, a):
        if a == Qt.Checked:
            self.cams[5] = True
        else:
            self.cams[5] = False

    def OTHER(self, a):
        if a == Qt.Checked:
            self.cams[6] = True
        else:
            self.cams[6] = False

    def register(self):  # Пробуем зарегистрироваться, если данные корректны открываем основное приложение
        self.end_number = []
        self.number = list(self.input_number.text())
        for x in self.number:
            if x in self.nums:
                self.end_number.append(x)
        self.phone_number = ''
        if self.end_number:
            if self.end_number[0] == '7':
                self.end_number[0] = '8'

            for x in self.end_number:
                self.phone_number += x
            if len(self.end_number) != 11:
                self.error.setText('<h1 style="color: rgb(150, 0, 0);">Не корректный номер</h1>')
                return ''
            else:
                self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Введите номер телефона</h1>')
            return ''
        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.available_phones = self.cur.execute("""SELECT phone FROM Players
                                WHERE phone = ?""", (self.phone_number,)).fetchall()
        self.a = self.cur.execute("""SELECT phone FROM PLAYERS""")
        self.cursed_number = "[('" + self.phone_number + "',)]"
        self.con.commit()
        self.con.close()
        if self.cursed_number == str(self.available_phones):
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Номер телефона занят</h1>')
            return ''
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')

        self.password = self.input_pw.text()
        if not (self.password):
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Ведите пароль</h1>')
            return ''
        elif self.password.isdigit() is True:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Пароль должен содержать букву</h1>')
            return ''
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        self.name = self.input_name.text()
        if self.name:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Введите фамилию и имя</h1>')
            return ''

        self.date = self.input_date.text()
        if self.date and '.' in self.date and len(self.date) == 10:
            if len(self.date.split('.')) == 3:
                self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        elif not (self.date) or len(self.date) != 10 or not ('.' in self.date):
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Введите дату в формате 18.10.2022</h1>')
            return ''

        self.nick = self.input_nick.text()
        if self.nick:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Не корректный позывной</h1>')
            return ''

        if True in self.cams:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Выберете хотя бы один камуфляж</h1>')
            return ''

        self.cams_cout = 0
        self.end_cams = ''
        for x in self.cams:
            self.cams_cout += 1
            if x is True:
                if self.cams_cout == 1:
                    self.end_cams = self.end_cams + 'MC, '
                elif self.cams_cout == 2:
                    self.end_cams = self.end_cams + 'MOX, '
                elif self.cams_cout == 3:
                    self.end_cams = self.end_cams + 'EMR, '
                elif self.cams_cout == 4:
                    self.end_cams = self.end_cams + 'BK, '
                elif self.cams_cout == 5:
                    self.end_cams = self.end_cams + 'TAN, '
                elif self.cams_cout == 6:
                    self.end_cams = self.end_cams + 'OLIVE, '
                elif self.cams_cout == 7:
                    self.end_cams = self.end_cams + 'Другой, '
        self.end_cams = self.end_cams[:-2]
        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.cur.execute("""INSERT INTO Players VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (
            self.phone_number, self.password, self.name, self.date, self.nick, self.end_cams, self.end_type,
            'Одиночка'))
        self.con.commit()
        self.con.close()
        self.user = open('User.txt', mode='w')
        if self.save is True:
            self.user.write('TRUE!')
        else:
            self.user.write('FALSE!')
        self.user.write(str(self.phone_number))
        self.user.write('!')
        self.user.write(str(self.password))
        self.user.write('!')
        self.user.write(str(self.name))
        self.user.write('!')
        self.user.write(str(self.date))
        self.user.write('!')
        self.user.write(str(self.nick))
        self.user.write('!')
        self.user.write(str(self.end_cams))
        self.user.write('!')
        self.user.write(str(self.end_type))
        self.user.write('!Одиночка')
        self.user.close()
        self.close()
        self.Main_Window = Games_Window()
        self.Main_Window.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.title(qp)
        qp.end()

    def title(self, qp):
        qp.setBrush(QColor(214, 218, 191))
        qp.drawRect(0, 0, round(1080 * kx), round(250 * ky))
        qp.drawRect(0, round(1850 * ky), round(1080 * kx), round(250 * ky))


class Enter_Window(QWidget):  # Создаем окно для входа
    def __init__(self):
        super().__init__()
        self.save = False
        self.initUI()
        self.nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                     '0']  # Элементы, которые останутся в номере после преобразований

    def initUI(self):
        self.setGeometry(0, 0, round(1080 * kx), round(2100 * ky))
        self.setWindowTitle('Вход')

        self.welcome = QLabel(self)
        self.welcome.setText('<h1 style="color: rgb(0, 0, 0);">Вход в аккаунт</h1>')
        self.welcome = set_sizes(self.welcome, 900, 100, 260, 60)
        self.welcome.setFont(QFont('Calibri', round(14 * km) * 2))

        self.go_back = QPushButton('Вернуться к регистрации', self)  # Кнопка для возврата на экран регистрации
        self.go_back = set_sizes(self.go_back, 700, 70, 40, 1000)
        self.go_back.clicked.connect(self.open_registration_window)
        self.go_back.setFont(QFont('Calibri', round(18 * km) * 2))

        self.enter_number = QLabel(self)  # Поля для ввода данных
        self.enter_number.setText("Номер телефона")
        self.enter_number.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_number = set_sizes(self.enter_number, 500, 100, 60, 750)

        self.input_number = QLineEdit(self)
        self.input_number = set_sizes(self.input_number, 500, 60, 500, 770)
        self.input_number.setFont(QFont('Calibri', round(18 * km) * 2))

        self.enter_pw = QLabel(self)
        self.enter_pw.setText("Пароль")
        self.enter_pw.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_pw = set_sizes(self.enter_pw, 500, 100, 60, 820)

        self.input_pw = QLineEdit(self)
        self.input_pw = set_sizes(self.input_pw, 500, 60, 500, 840)
        self.input_pw.setFont(QFont('Calibri', round(18 * km) * 2))

        self.enter = QPushButton('Войти', self)  # Кнопка для входа
        self.enter = set_sizes(self.enter, 300, 70, 740, 1000)
        self.enter.clicked.connect(self.open_main_window)
        self.enter.setFont(QFont('Calibri', round(18 * km) * 2))

        self.error = QLabel(self)
        self.error.setText('<h1 style="color: rgb(150, 0, 0);">⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h1>')
        self.error.setFont(QFont('Calibri', round(10 * km) * 2))
        self.error = set_sizes(self.error, 910, 90, 60, 1850)

        self.remember = QCheckBox('Запомнить меня', self)
        self.remember = set_sizes(self.remember, 410, 90, 335, 910)
        self.remember.stateChanged.connect(self.rem)
        self.remember.setFont(QFont('Calibri', round(18 * km) * 2))

    def rem(self, a):  # функция для кнопки запомнить меня
        if a == Qt.Checked:
            self.save = True
        else:
            self.save = False

    def open_main_window(self):  # проверка введеных данных
        self.end_number = []
        self.number = list(self.input_number.text())
        for x in self.number:
            if x in self.nums:
                self.end_number.append(x)
        self.phone_number = ''
        if self.end_number:
            if self.end_number[0] == '7':
                self.end_number[0] = '8'

            for x in self.end_number:
                self.phone_number += x
            if len(self.end_number) != 11:
                self.error.setText('<h1 style="color: rgb(150, 0, 0);">Не корректный номер</h1>')
                return ''
            else:
                self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Введите номер телефона</h1>')
            return ''
        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.available_phones = self.cur.execute("""SELECT phone FROM Players
                                WHERE phone = ?""", (self.phone_number,)).fetchall()
        self.a = self.cur.execute("""SELECT phone FROM PLAYERS""")
        self.cursed_number = "[('" + self.phone_number + "',)]"
        self.con.commit()
        self.con.close()
        if self.cursed_number == str(self.available_phones):
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Не зарегистрированный номер</h1>')
            return ''
        self.password = self.input_pw.text()
        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.available_passsword = self.cur.execute("""SELECT password FROM Players
                                        WHERE phone = ?""", (self.phone_number,)).fetchall()
        self.cursed_password = "[('" + self.password + "',)]"
        self.con.commit()
        self.con.close()
        if str(self.available_passsword) == self.cursed_password:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Неверный пароль</h1>')
            return ''

        self.user = open('User.txt', mode='w')
        if self.save is False:
            self.user.write('FALSE')
        else:
            self.con = sqlite3.connect("ASA.sqlite")
            self.cur = self.con.cursor()
            self.data = self.cur.execute("""SELECT * FROM Players WHERE phone = ?""",
                                         (self.phone_number,)).fetchall()
            self.con.close()
            self.user.write('TRUE')
        for x in self.data:
            for i in x:
                self.user.write('!')
                self.user.write(str(i))
        self.con.close()
        self.user.close()
        self.close()

        self.Main_Window = Games_Window()
        self.Main_Window.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.title(qp)
        qp.end()

    def title(self, qp):
        qp.setBrush(QColor(214, 218, 191))
        qp.drawRect(0, 0, round(1080 * kx), round(250 * ky))
        qp.drawRect(0, round(1850 * ky), round(1080 * kx), round(250 * ky))

    def open_registration_window(self):  # Функция возвращения на экран регистрации
        self.Registration_Window = Registration_Window()
        self.Registration_Window.show()
        self.close()


class Games_Window(QWidget):  # окно с играми
    def __init__(self):
        super().__init__()
        self.initUI()

        self.profile_opened = False
        self.team_opened = False

    def initUI(self):
        global profile_on, profile_off, games_on, games_off, create_on, create_off, team_on, team_off, kx, ky
        global qprofile_on, qprofile_off, qgames_on, qgames_off, qcreate_on, qcreate_off, qteam_on, qteam_off

        profile_on = QPixmap('pictures/profile_on.png').scaled(50, 50)
        profile_off = QPixmap('pictures/profile_off.png').scaled(50, 50)
        games_on = QPixmap('pictures/games_on.png').scaled(50, 50)
        games_off = QPixmap('pictures/games_off.png').scaled(50, 50)
        team_on = QPixmap('pictures/team_off.png').scaled(50, 50)
        team_off = QPixmap('pictures/team_on.png').scaled(50, 50)
        create_on = QPixmap('pictures/create_on.png').scaled(50, 50)
        create_off = QPixmap('pictures/create_off.png').scaled(50, 50)

        qprofile_on = QIcon()
        qprofile_off = QIcon()
        qgames_on = QIcon()
        qgames_off = QIcon()
        qteam_on = QIcon()
        qteam_off = QIcon()
        qcreate_on = QIcon()
        qcreate_off = QIcon()

        qprofile_on.addPixmap(profile_on)
        qprofile_off.addPixmap(profile_off)
        qgames_on.addPixmap(games_on)
        qgames_off.addPixmap(games_off)
        qteam_on.addPixmap(team_on)
        qteam_off.addPixmap(team_off)
        qcreate_on.addPixmap(create_on)
        qcreate_off.addPixmap(create_off)



        self.setGeometry(0, 0, round(1080 * kx), round(2100 * ky))
        self.setWindowTitle('Games')

        self.create_btn = QPushButton(self)
        self.create_btn.setIcon(qcreate_off)
        self.create_btn.setIconSize(profile_on.rect().size())
        self.create_btn.move(round(kx * 156), round(ky * 1900))
        self.create_btn.setStyleSheet('QPushButton {background-color: rgb(214, 218, 191)}')

        self.team_btn = QPushButton(self)
        self.team_btn.setIcon(qteam_off)
        self.team_btn.setIconSize(team_on.rect().size())
        self.team_btn.move(round(kx * 352), round(ky * 1900))
        self.team_btn.clicked.connect(self.open_team_win)
        self.team_btn.setStyleSheet('QPushButton {background-color: rgb(214, 218, 191)}')

        self.games_btn = QPushButton(self)
        self.games_btn.setIcon(qgames_on)
        self.games_btn.setIconSize(games_on.rect().size())
        self.games_btn.move(round(kx * 578), round(ky * 1900))
        self.games_btn.setStyleSheet('QPushButton {background-color: rgb(214, 218, 191)}')

        self.profile_btn = QPushButton(self)
        self.profile_btn.setIcon(qprofile_off)
        self.profile_btn.setIconSize(profile_on.rect().size())
        self.profile_btn.move(round(kx * 804), round(ky * 1900))
        self.profile_btn.clicked.connect(self.open_profile_win)
        self.profile_btn.setStyleSheet('QPushButton {background-color: rgb(214, 218, 191)}')

        self.welcome = QLabel(self)
        self.welcome.setText('<h1 style="color: rgb(0, 0, 0);">Ближайшие игры</h1>')
        self.welcome = set_sizes(self.welcome, 900, 100, 230, 60)
        self.welcome.setFont(QFont('Calibri', round(14 * km) * 2))

        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.games_data = self.cur.execute("""SELECT * FROM Games""").fetchall()
        self.con.close()

        self.games = QTableWidget(self)
        self.games.setColumnCount(6)
        self.games.setRowCount(30)
        self.games.setHorizontalHeaderLabels(['Название', 'Тип', 'Организатор', 'Дата', 'Полигон', 'Цена'])
        self.games = set_sizes(self.games, 1000, 1500, 35, 260)
        for x in range(5):
            data = self.games_data[x]
            for i in range(6):
                self.games.setItem(x, i, QTableWidgetItem(data[i][:14]))
        self.games.setFont(QFont('Calibri', 10))
        self.games.resizeColumnsToContents()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.title(qp)
        qp.end()

    def title(self, qp):
        qp.setBrush(QColor(214, 218, 191))
        qp.drawRect(0, 0, round(1080 * kx), round(250 * ky))
        qp.drawRect(0, round(1850 * ky), round(1080 * kx), round(250 * ky))

    def open_team_win(self):  # открытие окна команды
        self.user = open('User.txt')
        self.data = self.user.read().split('!')
        self.user.close()
        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.data2 = self.cur.execute("""SELECT name FROM Teams WHERE Commander = ?""",
                                      (self.data[1],)).fetchall()
        self.con.close()
        if self.data2:
            self.app1 = My_Team_Window()
        elif self.data[8] == 'Одиночка':
            self.app1 = No_Team_Window()
        else:
            self.app1 = Team_Window()
        self.app1.show()
        self.close()

    def open_profile_win(self):  # открытие окна профиля
        self.app2 = Profile_Window()
        self.close()
        self.app2.show()

    def open_create_win(self):  # закрытие всех окон
        pass


class No_Team_Window(QWidget):  # окно игроков без команды
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(244, 400, 415, 430)
        self.setWindowTitle(' ')

        self.info = QLabel(self)
        self.info.setText('На данный момент вы не состоите в команде,')
        self.info.move(22, 72)
        self.info.setFont(QFont('Calibri', 12))
        self.info.resize(400, 20)

        self.info2 = QLabel(self)
        self.info2.setText('попросите командира команды добавить вас.')
        self.info2.move(22, 92)
        self.info2.setFont(QFont('Calibri', 12))
        self.info2.resize(400, 20)

        self.info2 = QLabel(self)
        self.info2.setText('Или вы можете')
        self.info2.move(120, 150)
        self.info2.setFont(QFont('Calibri', 17))
        self.info2.resize(400, 30)

        self.create_team = QPushButton('Создать свою\nкоманду', self)
        self.create_team.resize(200, 70)
        self.create_team.move(107, 180)
        self.create_team.clicked.connect(self.crt_team)
        self.create_team.setFont(QFont('Calibri', 17))

        self.title_txt = QLabel(self)
        self.title_txt.setText('Команда')
        self.title_txt.move(150, 10)
        self.title_txt.setFont(QFont('Calibri', 20))
        self.title_txt.resize(150, 35)

    def crt_team(self):  # функция для создания команды
        self.crt_tm = Create_Team_Window()
        self.crt_tm.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.title(qp)
        qp.end()

    def title(self, qp):
        qp.setBrush(QColor(200, 200, 200))
        qp.drawRect(0, 0, 415, 50)
        qp.setBrush(QColor(0, 0, 0))
        qp.drawLine(0, 50, 415, 50)


class Profile_Window(QWidget):  # окно профиля
    def __init__(self):
        super().__init__()
        self.initUI()

        self.nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                     '0']  # Элементы, которые останутся в номере после преобразований

        self.initUI()

    def initUI(self):
        self.end_type = "SQB (120м/c)"
        self.setGeometry(0, 0, round(1080 * kx), round(2100 * ky))
        self.setWindowTitle('Profile')

        self.cams = [False, False, False, False, False, False, False]

        self.create_btn = QPushButton(self)
        self.create_btn.setIcon(qcreate_off)
        self.create_btn.setIconSize(profile_on.rect().size())
        self.create_btn.move(round(kx * 156), round(ky * 1900))
        self.create_btn.setStyleSheet('QPushButton {background-color: rgb(214, 218, 191)}')

        self.team_btn = QPushButton(self)
        self.team_btn.setIcon(qteam_off)
        self.team_btn.setIconSize(team_on.rect().size())
        self.team_btn.move(round(kx * 352), round(ky * 1900))
        self.team_btn.clicked.connect(self.open_team_win)
        self.team_btn.setStyleSheet('QPushButton {background-color: rgb(214, 218, 191)}')

        self.games_btn = QPushButton(self)
        self.games_btn.setIcon(qgames_off)
        self.games_btn.setIconSize(games_off.rect().size())
        self.games_btn.move(round(kx * 578), round(ky * 1900))
        self.games_btn.clicked.connect(self.open_games_win)
        self.games_btn.setStyleSheet('QPushButton {background-color: rgb(214, 218, 191)}')

        self.profile_btn = QPushButton(self)
        self.profile_btn.setIcon(qprofile_on)
        self.profile_btn.setIconSize(profile_on.rect().size())
        self.profile_btn.move(round(kx * 804), round(ky * 1900))
        self.profile_btn.setStyleSheet('QPushButton {background-color: rgb(214, 218, 191)}')

        self.welcome = QLabel(self)
        self.welcome.setText('<h1 style="color: rgb(0, 0, 0);">Профиль</h1>')
        self.welcome = set_sizes(self.welcome, 900, 100, 350, 60)
        self.welcome.setFont(QFont('Calibri', round(14 * km) * 2))

        self.user = open('User.txt')  # поля с данными, все аналогично окну регистрациии
        self.data = self.user.read().split('!')
        self.cams_data = self.data[6]
        self.enter_number = QLabel(self)  # Поля для ввода данных
        self.enter_number.setText("Номер телефона")
        self.enter_number.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_number = set_sizes(self.enter_number, 500, 100, 60, 250)

        self.input_number = QLineEdit(self)
        self.input_number = set_sizes(self.input_number, 500, 60, 500, 270)
        self.input_number.setFont(QFont('Calibri', round(18 * km) * 2))
        self.input_number.setReadOnly(True)

        self.enter_pw = QLabel(self)
        self.enter_pw.setText("Пароль")
        self.enter_pw.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_pw = set_sizes(self.enter_pw, 500, 100, 60, 320)

        self.input_pw = QLineEdit(self)
        self.input_pw = set_sizes(self.input_pw, 500, 60, 500, 340)
        self.input_pw.setFont(QFont('Calibri', round(18 * km) * 2))

        self.enter_name = QLabel(self)
        self.enter_name.setText("Фамилия и Имя")
        self.enter_name.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_name = set_sizes(self.enter_name, 500, 100, 60, 390)

        self.input_name = QLineEdit(self)
        self.input_name = set_sizes(self.input_name, 500, 60, 500, 410)
        self.input_name.setFont(QFont('Calibri', round(18 * km) * 2))

        self.enter_nick = QLabel(self)
        self.enter_nick.setText("Позывной")
        self.enter_nick.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_nick = set_sizes(self.enter_nick, 500, 100, 60, 460)

        self.input_nick = QLineEdit(self)
        self.input_nick = set_sizes(self.input_nick, 500, 60, 500, 480)
        self.input_nick.setFont(QFont('Calibri', round(18 * km) * 2))

        self.enter_date = QLabel(self)
        self.enter_date.setText("Дата рождения")
        self.enter_date.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_date = set_sizes(self.enter_date, 500, 100, 60, 530)

        self.input_date = QLineEdit(self)
        self.input_date = set_sizes(self.input_date, 500, 60, 500, 550)
        self.input_date.setFont(QFont('Calibri', round(18 * km) * 2))

        self.enter_cam = QLabel(self)
        self.enter_cam.setText("Камуфляж")
        self.enter_cam.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_cam = set_sizes(self.enter_cam, 500, 100, 60, 600)

        self.mc = QCheckBox('MC', self)
        self.mc = set_sizes(self.mc, 200, 100, 510, 600)
        self.mc.stateChanged.connect(self.MC)
        self.mc.setFont(QFont('Calibri', round(18 * km) * 2))

        self.mox = QCheckBox('MOX', self)
        self.mox = set_sizes(self.mox, 200, 100, 770, 600)
        self.mox.stateChanged.connect(self.MOX)
        self.mox.setFont(QFont('Calibri', round(18 * km) * 2))

        self.emr = QCheckBox('EMP', self)
        self.emr = set_sizes(self.emr, 200, 100, 510, 670)
        self.emr.stateChanged.connect(self.EMR)
        self.emr.setFont(QFont('Calibri', round(18 * km) * 2))

        self.bk = QCheckBox('BK', self)
        self.bk = set_sizes(self.bk, 200, 100, 770, 670)
        self.bk.stateChanged.connect(self.BK)
        self.bk.setFont(QFont('Calibri', round(18 * km) * 2))

        self.tan = QCheckBox('TAN', self)
        self.tan = set_sizes(self.tan, 200, 100, 510, 740)
        self.tan.stateChanged.connect(self.TAN)
        self.tan.setFont(QFont('Calibri', round(18 * km) * 2))

        self.olive = QCheckBox('OLIVE', self)
        self.olive = set_sizes(self.olive, 200, 100, 770, 740)
        self.olive.stateChanged.connect(self.OLIVE)
        self.olive.setFont(QFont('Calibri', round(18 * km) * 2))

        self.other = QCheckBox('ДРУГОЙ', self)
        self.other = set_sizes(self.other, 300, 100, 510, 810)
        self.other.stateChanged.connect(self.OTHER)
        self.other.setFont(QFont('Calibri', round(18 * km) * 2))

        self.enter_type = QLabel(self)
        self.enter_type.setText("Тип игрока")
        self.enter_type.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_type = set_sizes(self.enter_type, 500, 100, 60, 890)

        self.choose_type = QComboBox(self)
        self.choose_type.addItems(["SQB (120м/c)", "Штурмовик (150м/с)", "Снайпер (170м/c)"])
        self.choose_type.setFont(QFont('Calibri', round(18 * km) * 2))
        self.choose_type = set_sizes(self.choose_type, 500, 60, 490, 910)
        self.choose_type.activated[str].connect(self.TYPE)

        self.error = QLabel(self)
        self.error.setText('<h1 style="color: rgb(150, 0, 0);">⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h1>')
        self.error.setFont(QFont('Calibri', round(10 * km) * 2))
        self.error = set_sizes(self.error, 910, 90, 60, 1850)

        if 'MC' in self.cams_data:
            self.cams[0] = True
            self.mc.setChecked(True)

        if 'MOX' in self.cams_data:
            self.cams[1] = True
            self.mox.setChecked(True)

        if 'EMR' in self.cams_data:
            self.cams[2] = True
            self.emr.setChecked(True)

        if 'BK' in self.cams_data:
            self.cams[3] = True
            self.bk.setChecked(True)

        if 'TAN' in self.cams_data:
            self.cams[4] = True
            self.tan.setChecked(True)

        if 'OLIVE' in self.cams_data:
            self.cams[5] = True
            self.olive.setChecked(True)

        if 'OTHER' in self.cams_data:
            self.cams[6] = True
            self.other.setChecked(True)

        self.team = QLabel(self)
        self.team.setText("Команда")
        self.team.setFont(QFont('Calibri', round(18 * km) * 2))
        self.team = set_sizes(self.team, 500, 100, 60, 960)

        self.team_data = QLineEdit(self)
        self.team_data.setText(self.data[8])
        self.team_data.setFont(QFont('Calibri', round(18 * km) * 2))
        self.team_data = set_sizes(self.team_data, 500, 60, 500, 980)
        self.team_data.setReadOnly(True)

        self.save_data = QPushButton('Сохранить', self)
        self.save_data = set_sizes(self.save_data, 330, 70, 40, 1090)
        self.save_data.clicked.connect(self.save)
        self.save_data.setFont(QFont('Calibri', round(18 * km) * 2))

        self.refresh_data = QPushButton('Вернуть', self)
        self.refresh_data = set_sizes(self.refresh_data, 340, 70, 370, 1090)
        self.refresh_data.clicked.connect(self.refresh)
        self.refresh_data.setFont(QFont('Calibri', round(18 * km) * 2))

        self.leave_account = QPushButton('Выйти', self)
        self.leave_account = set_sizes(self.leave_account, 330, 70, 710, 1090)
        self.leave_account.clicked.connect(self.leave)
        self.leave_account.setFont(QFont('Calibri', round(18 * km) * 2))

    def open_games_win(self):
        self.app1 = Games_Window()
        self.app1.show()
        self.close()
    def open_team_win(self):  # открытие окна команды
        self.user = open('User.txt')
        self.data = self.user.read().split('!')
        self.user.close()
        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.data2 = self.cur.execute("""SELECT name FROM Teams WHERE Commander = ?""",
                                      (self.data[1],)).fetchall()
        self.con.close()
        if self.data2:
            self.app1 = My_Team_Window()
        elif self.data[8] == 'Одиночка':
            self.app1 = No_Team_Window()
        else:
            self.app1 = Team_Window()
        self.app1.show()
        self.close()

    def TYPE(self, text):
        self.end_type = text

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.title(qp)
        qp.end()

    def title(self, qp):
        qp.setBrush(QColor(214, 218, 191))
        qp.drawRect(0, 0, round(1080 * kx), round(250 * ky))
        qp.drawRect(0, round(1850 * ky), round(1080 * kx), round(250 * ky))

    def save(self):  # проверка изменений и их сохранение
        self.end_number = []
        self.number = list(self.input_number.text())
        for x in self.number:
            if x in self.nums:
                self.end_number.append(x)
        self.phone_number = ''
        if self.end_number:
            if self.end_number[0] == '7':
                self.end_number[0] = '8'

            for x in self.end_number:
                self.phone_number += x
            if len(self.end_number) != 11:
                self.error.setText('<h1 style="color: rgb(150, 0, 0);">Не корректный номер</h1>')
                return ''
            else:
                self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Введите номер телефона</h1>')
            return ''
        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.available_phones = self.cur.execute("""SELECT phone FROM Players
                                WHERE phone = ?""", (self.phone_number,)).fetchall()
        self.a = self.cur.execute("""SELECT phone FROM PLAYERS""")
        self.cursed_number = "[(" + self.phone_number + ",)]"
        self.con.commit()
        self.con.close()
        if self.cursed_number == str(self.available_phones):
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Номер телефона занят</h1>')
            return ''
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')

        self.password = self.input_pw.text()
        if not (self.password):
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Ведите пароль</h1>')
            return ''
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')

        self.name = self.input_name.text()
        if self.name:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Введите фамилию и имя</h1>')
            return ''

        self.date = self.input_date.text()
        if self.date and '.' in self.date and len(self.date) == 10:
            if len(self.date.split('.')) == 3:
                self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        elif not (self.date) or len(self.date) != 10 or not ('.' in self.date):
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Введите дату в формате 18.10.2022</h1>')
            return ''

        self.nick = self.input_nick.text()
        if self.nick:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Не корректный позывной</h1>')
            return ''

        if True in self.cams:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Выберете хотя бы один камуфляж</h1>')
            return ''

        self.cams_cout = 0
        self.end_cams = ''
        for x in self.cams:
            self.cams_cout += 1
            if x is True:
                if self.cams_cout == 1:
                    self.end_cams = self.end_cams + 'MC, '
                elif self.cams_cout == 2:
                    self.end_cams = self.end_cams + 'MOX, '
                elif self.cams_cout == 3:
                    self.end_cams = self.end_cams + 'EMR, '
                elif self.cams_cout == 4:
                    self.end_cams = self.end_cams + 'BK, '
                elif self.cams_cout == 5:
                    self.end_cams = self.end_cams + 'TAN, '
                elif self.cams_cout == 6:
                    self.end_cams = self.end_cams + 'OLIVE, '
                elif self.cams_cout == 7:
                    self.end_cams = self.end_cams + 'Другой, '
        self.end_cams = self.end_cams[:-2]
        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.cur.execute("""UPDATE Players SET password = ?
                WHERE phone = ?""", (self.password, self.phone_number))
        self.cur.execute("""UPDATE Players SET name = ?
                WHERE phone = ?""", (self.name, self.phone_number))
        self.cur.execute("""UPDATE Players SET date = ?
                WHERE phone = ?""", (self.date, self.phone_number))
        self.cur.execute("""UPDATE Players SET nick = ?
                WHERE phone = ?""", (self.nick, self.phone_number))
        self.cur.execute("""UPDATE Players SET cams = ?
                WHERE phone = ?""", (self.end_cams, self.phone_number))
        self.cur.execute("""UPDATE Players SET type = ?
                WHERE phone = ?""", (self.type2.text(), self.phone_number))
        self.con.commit()
        self.con.close()
        self.user = open('User.txt')
        self.data2 = self.user.read()
        self.user.close()
        self.user = open('User.txt', mode='w')
        if 'TRUE' in self.data2:
            self.user.write('TRUE!')
        else:
            self.user.write('FALSE!')
        self.user.write(str(self.phone_number))
        self.user.write('!')
        self.user.write(str(self.password))
        self.user.write('!')
        self.user.write(str(self.name))
        self.user.write('!')
        self.user.write(str(self.date))
        self.user.write('!')
        self.user.write(str(self.nick))
        self.user.write('!')
        self.user.write(str(self.end_cams))
        self.user.write('!')
        self.user.write(str(self.type2.text()))
        self.user.write('!Одиночка')
        self.user.close()

    def refresh(self):  # функция обновления данных
        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.data3 = self.cur.execute("""SELECT * FROM Players
            WHERE phone = ?""", (self.data[1],)).fetchall()
        self.data3 = self.data3[0]
        self.input_pw.setText(self.data3[1])
        self.input_name.setText(self.data3[2])
        self.input_date.setText(self.data3[3])
        self.input_nick.setText(self.data3[4])
        self.type2.setText(self.data3[6])
        self.input_number.setText(self.data3[0])
        self.cams_data2 = self.data3[5]
        if 'MC' in self.cams_data2:
            self.cams[0] = True
            self.mc.setChecked(True)
        else:
            self.cams[0] = False
            self.mc.setChecked(False)

        if 'MOX' in self.cams_data2:
            self.cams[1] = True
            self.mox.setChecked(True)
        else:
            self.cams[1] = False
            self.mox.setChecked(False)

        if 'EMR' in self.cams_data2:
            self.cams[2] = True
            self.emr.setChecked(True)
        else:
            self.cams[2] = False
            self.emr.setChecked(False)

        if 'BK' in self.cams_data2:
            self.cams[3] = True
            self.bk.setChecked(True)
        else:
            self.cams[3] = False
            self.bk.setChecked(False)

        if 'TAN' in self.cams_data2:
            self.cams[4] = True
            self.tan.setChecked(True)
        else:
            self.cams[4] = False
            self.tan.setChecked(False)

        if 'OLIVE' in self.cams_data2:
            self.cams[5] = True
            self.olive.setChecked(True)
        else:
            self.cams[5] = False
            self.olive.setChecked(False)

        if 'OTHER' in self.cams_data2:
            self.cams[6] = True
            self.other.setChecked(True)
        else:
            self.cams[6] = False
            self.other.setChecked(False)

        self.con.commit()
        self.con.close()

    def leave(self):  # выход из аккаунта
        self.user = open('User.txt', mode='w')
        self.user.write("FALSE! ")
        self.user.close()
        self.destr = '6' + 6

    def MC(self, a):
        if a == Qt.Checked:
            self.cams[0] = True
        else:
            self.cams[0] = False

    def MOX(self, a):
        if a == Qt.Checked:
            self.cams[1] = True
        else:
            self.cams[1] = False

    def EMR(self, a):
        if a == Qt.Checked:
            self.cams[2] = True
        else:
            self.cams[2] = False

    def BK(self, a):
        if a == Qt.Checked:
            self.cams[3] = True
        else:
            self.cams[3] = False

    def TAN(self, a):
        if a == Qt.Checked:
            self.cams[4] = True
        else:
            self.cams[4] = False

    def OLIVE(self, a):
        if a == Qt.Checked:
            self.cams[5] = True
        else:
            self.cams[5] = False

    def OTHER(self, a):
        if a == Qt.Checked:
            self.cams[6] = True
        else:
            self.cams[6] = False


class Team_Window(QWidget):  # окно игрока состоящего в команде
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(244, 400, 415, 430)
        self.setWindowTitle('   ')

        self.title_txt = QLabel(self)
        self.title_txt.setText('Команда')
        self.title_txt.move(150, 10)
        self.title_txt.setFont(QFont('Arial', 20))
        self.title_txt.resize(150, 35)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.title(qp)
        qp.end()

    def title(self, qp):
        qp.setBrush(QColor(200, 200, 200))
        qp.drawRect(0, 0, 415, 50)
        qp.setBrush(QColor(0, 0, 0))
        qp.drawLine(0, 50, 415, 50)


class Create_Team_Window(QWidget):  # окно создания команды
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(752, 400, 415, 430)
        self.setWindowTitle('   ')

        self.title_txt = QLabel(self)
        self.title_txt.setText('Создание команды')
        self.title_txt.move(90, 10)
        self.title_txt.setFont(QFont('Calibri', round(18 * km) * 2))
        self.title_txt.resize(240, 35)

        self.enter_name = QLabel(self)
        self.enter_name.setText("Название")
        self.enter_name.move(22, 75)
        self.enter_name.setFont(QFont('Arial', 14))

        self.input_name = QLineEdit(self)
        self.input_name.move(157, 75)
        self.input_name.setFont(QFont('Arial', 13))
        self.input_name.resize(235, 24)

        self.enter_cam = QLabel(self)
        self.enter_cam.setText("Камуфляж")
        self.enter_cam.move(22, 100)
        self.enter_cam.setFont(QFont('Arial', 14))

        self.input_cam = QLineEdit(self)
        self.input_cam.move(157, 100)
        self.input_cam.setFont(QFont('Arial', 13))
        self.input_cam.resize(235, 24)

        self.enter_discription = QLabel(self)
        self.enter_discription.setText("Описание")
        self.enter_discription.move(22, 125)
        self.enter_discription.setFont(QFont('Arial', 14))

        self.input_discription = QPlainTextEdit(self)
        self.input_discription.setGeometry(QRect(157, 125, 235, 200))
        self.input_discription.setFont(QFont('Arial', 13))

        self.create_team = QPushButton('Создать', self)
        self.create_team.resize(100, 30)
        self.create_team.move(157, 340)
        self.create_team.clicked.connect(self.crt_team)
        self.create_team.setFont(QFont('Arial', 14))

        self.error = QLabel(self)
        self.error.setText('<h1 style="color: rgb(150, 0, 0);">⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</h1>')
        self.error.setFont(QFont('Arial', 7))
        self.error.move(22, 380)

    def crt_team(self):  # добавление команды в базу
        self.name = self.input_name.text()

        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.available_names = self.cur.execute("""SELECT name FROM Teams
                                        WHERE name = ?""", (self.name,)).fetchall()
        self.cursed_number = "[('" + self.name + "',)]"
        self.con.commit()
        self.con.close()

        if not (self.name):
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Ведите название</h1>')
            return ''
        elif self.cursed_number == self.available_names:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Название команды занято</h1>')
            return ''
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')

        self.cam = self.input_cam.text()
        if self.cam:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Введите камуфляж</h1>')
            return ''

        self.description = self.input_discription.toPlainText()
        if self.description:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);"> </h1>')
        else:
            self.error.setText('<h1 style="color: rgb(150, 0, 0);">Введите описание</h1>')
            return ''

        self.user = open('User.txt')
        self.data = self.user.read().split('!')
        self.user.close()
        self.number = self.data[1]
        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.cur.execute("""INSERT INTO Teams VALUES (?, ?, ?, ?, ?)""", (
            self.number, self.number, self.description, self.name, self.cam))
        self.con.commit()
        self.cur.execute("""UPDATE Players SET team = ?
                        WHERE phone = ?""", (self.name, self.number))
        self.con.commit()
        self.con.close()
        self.error.setText('<h1 style="color: rgb(0, 150, 0);">Команда создана. Перезапустите приложение</h1>')
        self.error.setFont(QFont('Arial', 6))

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.title(qp)
        qp.end()

    def title(self, qp):
        qp.setBrush(QColor(200, 200, 200))
        qp.drawRect(0, 0, 415, 50)
        qp.setBrush(QColor(0, 0, 0))
        qp.drawLine(0, 50, 415, 50)


class My_Team_Window(QWidget):  # окно команды для капитана
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, round(1080 * kx), round(2100 * ky))
        self.setWindowTitle('   ')

        self.user = open('User.txt')
        self.data = self.user.read().split('!')
        self.user.close()

        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.team_data = self.cur.execute("""SELECT * FROM Teams
                                                        WHERE name = ?""", (self.data[8],)).fetchall()
        self.con.commit()
        self.con.close()

        self.create_btn = QPushButton(self)
        self.create_btn.setIcon(qcreate_off)
        self.create_btn.setIconSize(profile_on.rect().size())
        self.create_btn.move(round(kx * 156), round(ky * 1900))
        self.create_btn.setStyleSheet('QPushButton {background-color: rgb(214, 218, 191)}')

        self.team_btn = QPushButton(self)
        self.team_btn.setIcon(qteam_on)
        self.team_btn.setIconSize(team_on.rect().size())
        self.team_btn.move(round(kx * 352), round(ky * 1900))
        self.team_btn.setStyleSheet('QPushButton {background-color: rgb(214, 218, 191)}')

        self.games_btn = QPushButton(self)
        self.games_btn.setIcon(qgames_off)
        self.games_btn.setIconSize(games_off.rect().size())
        self.games_btn.move(round(kx * 578), round(ky * 1900))
        self.games_btn.setStyleSheet('QPushButton {background-color: rgb(214, 218, 191)}')

        self.profile_btn = QPushButton(self)
        self.profile_btn.setIcon(qprofile_off)
        self.profile_btn.setIconSize(profile_off.rect().size())
        self.profile_btn.move(round(kx * 804), round(ky * 1900))
        self.profile_btn.clicked.connect(self.open_profile_win)
        self.profile_btn.setStyleSheet('QPushButton {background-color: rgb(214, 218, 191)}')


        self.welcome = QLabel(self)
        self.welcome.setText('<h1 style="color: rgb(0, 0, 0);">Моя команда</h1>')
        self.welcome = set_sizes(self.welcome, 900, 100, 270, 60)
        self.welcome.setFont(QFont('Calibri', round(14 * km) * 2))

        self.enter_number = QLabel(self)  # Поля для ввода данных
        self.enter_number.setText("Название")
        self.enter_number.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_number = set_sizes(self.enter_number, 500, 100, 60, 250)

        self.input_number = QLineEdit(self)
        self.input_number = set_sizes(self.input_number, 500, 60, 500, 270)
        self.input_number.setFont(QFont('Calibri', round(18 * km) * 2))
        self.input_number.setText(self.team_data[0][3])
        self.input_number.setReadOnly(True)

        self.enter_pw = QLabel(self)
        self.enter_pw.setText("Камуфляж")
        self.enter_pw.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_pw = set_sizes(self.enter_pw, 500, 100, 60, 320)

        self.input_pw = QLineEdit(self)
        self.input_pw = set_sizes(self.input_pw, 500, 60, 500, 340)
        self.input_pw.setFont(QFont('Calibri', round(18 * km) * 2))
        self.input_pw.setText(self.team_data[0][4])

        self.players_count = len(self.team_data[0][1].split(', '))
        self.players = QLabel(self)
        self.players.setText('Члены команды (' + str(self.players_count) + ')')
        self.players = set_sizes(self.players, 500, 60, 60, 940)
        self.players.setFont(QFont('Calibri', round(18 * km) * 2))

        self.enter_discription = QLabel(self)
        self.enter_discription.setText("Описание")
        self.enter_discription.setFont(QFont('Calibri', round(18 * km) * 2))
        self.enter_discription = set_sizes(self.enter_discription, 500, 100, 60, 390)

        self.input_discription = QPlainTextEdit(self)
        self.input_discription.setGeometry(QRect(round(kx * 500), round(ky * 410), round(kx * 500), round(ky * 500)))
        self.input_discription.setFont(QFont('Calibri', round(18 * km) * 2))
        self.input_discription.setPlainText(self.team_data[0][2])
        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.data_players = self.cur.execute("""SELECT nick, name, phone FROM Players
                                                WHERE team = ?""", (self.team_data[0][3],)).fetchall()
        self.con.commit()
        self.con.close()

        self.list = QTableWidget(self)
        self.list.setColumnCount(3)
        self.list.setRowCount(1)
        self.list.setHorizontalHeaderLabels(['Позывной', 'Имя', 'Телефон'])
        self.list = set_sizes(self.list, 980, 500, 60, 1010)
        for x in range(1):
            data = self.data_players[x]
            for i in range(3):
                self.list.setItem(x, i, QTableWidgetItem(data[i]))
        self.list.setFont(QFont('Calibri', round(18 * km) * 2))
        self.list.resizeColumnsToContents()
    '''''''''
    def change_squad(self):  # функция добавления и удаления членов команды
        self.number = self.input_player.text()
        self.con = sqlite3.connect("ASA.sqlite")
        self.cur = self.con.cursor()
        self.data = self.cur.execute("""SELECT team FROM Players
                                        WHERE phone = ?""", (self.number,)).fetchall()
        self.con.commit()
        self.con.close()
        if self.input_name.text() == self.data[0][0]:
            self.new_teammates = ''
            self.new_teammate = self.teammates.remove(self.number)
            for x in self.new_teammate:
                self.new_teammates += x
            self.con = sqlite3.connect("ASA.sqlite")
            self.cur = self.con.cursor()
            self.cur.execute("""UPDATE Teams SET Teammates = ? WHERE name = ?""",
                             (self.new_teammates, self.input_name.text()))
            self.con.commit()
            self.con.close()
    '''''''''
    def open_profile_win(self):  # открытие окна профиля
        self.app2 = Profile_Window()
        self.close()
        self.app2.show()

    def open_games_win(self):
        self.app1 = Games_Window()
        self.app1.show()
        self.close()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.title(qp)
        qp.end()

    def title(self, qp):
        qp.setBrush(QColor(214, 218, 191))
        qp.drawRect(0, 0, round(1080 * kx), round(250 * ky))
        qp.drawRect(0, round(1850 * ky), round(1080 * kx), round(250 * ky))


def start():  # Запуск и выключение программы
    app = QApplication(sys.argv)
    user = open('User.txt')
    text = user.read()
    user.close()
    if text.split('!')[0] == "FALSE":
        ex = Registration_Window()
        user = open('User.txt', mode='w')
        user.write('FALSE! ')
        user.close()
    else:
        con = sqlite3.connect("ASA.sqlite")
        cur = con.cursor()
        data = cur.execute("""SELECT * FROM Players
                                WHERE phone = ?""", (int(text.split('!')[1]),)).fetchall()
        con.commit()
        if not (data):
            user = open('User.txt', mode='w')
            user.write('FALSE! ')
            user.close()
        con.close()
        user = open('User.txt', mode='w')
        user.write('TRUE')
        for x in data[0]:
            user.write('!')
            user.write(x)
        user.close()
        ex = Games_Window()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Loading_Window()
    ex.show()
