import sqlite3

con = sqlite3.connect("ASA.sqlite")
cur = con.cursor()
a = cur.execute("""SELECT password from Players""").fetchall()
con.commit()
con.close()
print(a)