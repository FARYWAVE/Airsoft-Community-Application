from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFontDatabase

app = QApplication([])

font_db = QFontDatabase()
available_fonts = font_db.families()
print(available_fonts)