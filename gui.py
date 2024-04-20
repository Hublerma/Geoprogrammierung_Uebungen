# Qt

from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dies ist ein Fenster")
        self.show

app = QApplication([])
w = Fenster()
app.exec_()