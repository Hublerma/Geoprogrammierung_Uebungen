import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("GUI-Programmierung")

        # Layout erstellen:
        layout = QFormLayout()

        # Widget-Instanzen erstellen:
        self.vornameLineEdit = QLineEdit()
        self.nachnameLineEdit = QLineEdit()
        self.mailLineEdit = QLineEdit()
        self.birthdayDateEdit = QDateEdit()
        self.strasseLineEdit = QLineEdit()
        self.nrLineEdit = QLineEdit()
        self.plzLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()
        self.landComboBox = QComboBox()
        self.landComboBox.addItems(["Schweiz", "Deutschland", "Österreich"])
        button1_save = QPushButton("Save")
        button2_laden = QPushButton("Laden")
        button3_show = QPushButton("Auf Karte zeigen")

        # Menüleiste erstellen:
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        save = QAction("Save", self) 
        quit = QAction("Quit", self)
        filemenu.addAction(save)
        filemenu.addAction(quit)

        # Layout füllen:
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Nachname:", self.nachnameLineEdit)
        layout.addRow("Email:", self.mailLineEdit)
        layout.addRow("Geburtstag:", self.birthdayDateEdit)
        layout.addRow("Strasse:", self.strasseLineEdit)
        layout.addRow("Nr:", self.nrLineEdit)
        layout.addRow("PostLeitzahl:", self.plzLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land", self.landComboBox)
        layout.addRow(button3_show)
        layout.addRow(button2_laden)
        layout.addRow(button1_save)

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

        button1_save.clicked.connect(self.button1_clicked)
        save.triggered.connect(self.button1_clicked)
        quit.triggered.connect(self.quit_clicked)
        button2_laden.clicked.connect(self.button2_clicked)
        button3_show.clicked.connect(self.button3_clicked)
    
    def button1_clicked(self):

        pfad, filter = QFileDialog.getSaveFileName(self, 
                                        "Datei speichern", 
                                        "",                 
                                        "csv (*.csv)")
        if pfad:
            vorname = self.vornameLineEdit.text()
            nachname = self.nachnameLineEdit.text()
            mail = self.mailLineEdit.text()
            geburtstag = self.birthdayDateEdit.date().toString("dd.MM.yyyy")
            strasse = self.strasseLineEdit.text()
            nr = self.nrLineEdit.text()
            plz = self.plzLineEdit.text()
            ort = self.ortLineEdit.text()
            land = self.landComboBox.currentText()
        
            with open(pfad, "w") as file:
                file.write(f"{vorname},{nachname},{mail},{geburtstag},{strasse},{nr},{plz},{ort},{land}")

        
    def button2_clicked(self):
        pfad, filter = QFileDialog.getOpenFileName(self, 
                                        "Datei laden", 
                                        "",                 
                                        "csv (*.csv)")
        if pfad:
            with open(pfad, "r") as file:
                data = file.read().split(",")
                self.vornameLineEdit.setText(data[0])
                self.nachnameLineEdit.setText(data[1])
                self.mailLineEdit.setText(data[2])
                self.birthdayDateEdit.setDate(QDate.fromString(data[3], "dd.MM.yyyy"))
                self.strasseLineEdit.setText(data[4])
                self.nrLineEdit.setText(data[5])
                self.plzLineEdit.setText(data[6])
                self.ortLineEdit.setText(data[7])
                self.landComboBox.setCurrentText(data[8])
    
    
    def button3_clicked(self):
        if self.strasseLineEdit.text() and self.nrLineEdit.text() and self.plzLineEdit.text() and self.ortLineEdit.text():
            link = f"https://www.google.ch/maps/place/{self.strasseLineEdit.text()}+{self.nrLineEdit.text()}+{self.plzLineEdit.text()}+{self.ortLineEdit.text()}+{self.landComboBox.currentText()}"
            QDesktopServices.openUrl(QUrl(link))
        else:
            QMessageBox.warning(self, "Warnung", "Angaben unvollständig!")

    def quit_clicked(self):
        self.close()

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()
    
    

        