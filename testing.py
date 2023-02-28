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
