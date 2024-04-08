import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("GUI-Programmierung")

        # Layout erstellen:
        layout = QFormLayout()

        # Widget-Instanzen erstellen:
        self.nameLineEdit = QLineEdit()
        self.mailLineEdit = QLineEdit()
        self.birthdayDateEdit = QDateEdit()
        self.adressLineEdit = QLineEdit()
        self.plzLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()
        self.landComboBox = QComboBox()
        self.landComboBox.addItems(["Schweiz", "Deutschland", "Österreich"])
        button1 = QPushButton("Save")

        # Menüleiste erstellen:
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        save = QAction("Save", self) 
        quit = QAction("Quit", self)
        filemenu.addAction(save)
        filemenu.addAction(quit)

        # Layout füllen:
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Email:", self.mailLineEdit)
        layout.addRow("Geburtstag:", self.birthdayDateEdit)
        layout.addRow("Adresse:", self.adressLineEdit)
        layout.addRow("PostLeitzahl:", self.plzLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land", self.landComboBox)
        layout.addRow(button1)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

        ############
        # CONNECTS #
        ############

        button1.clicked.connect(self.button1_clicked)
        save.triggered.connect(self.button1_clicked)
        quit.triggered.connect(self.quit_clicked)
    
    def button1_clicked(self):
        name = self.nameLineEdit.text()
        mail = self.mailLineEdit.text()
        geburtstag = str(self.birthdayDateEdit.date())
        adresse = self.adressLineEdit.text()
        plz = self.plzLineEdit.text()
        ort = self.ortLineEdit.text()
        land = self.landComboBox.currentText()
        

        with open("Uebung4_output.csv", "w") as file:
            file.write(f"{name},{mail},{geburtstag},{adresse},{plz},{ort},{land}")

        QMessageBox.information(self, "Information", "Output gespeichert.")
    
    def quit_clicked(self):
        self.close()


def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()
