import sys
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnects()

    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("Aufgabe X")
        ### LAYOUT WÄHLEN:
        layout = QFormLayout()
        self.setMinimumSize(800,200)

        ## Zentrierung der Widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        
        ## Widgets erstellen
        self.button1 = QPushButton("Beispiel 1: Information")
        self.button2 = QPushButton("Beispiel 2: About")
        self.button3 = QPushButton("Beispiel 3: Warning")
        self.button4 = QPushButton("Beispiel 4: Critical")
        self.button5 = QPushButton("Beispiel 5: Fragestellung")
        self.button6 = QPushButton("Beispiel 6: File Öffnen")
        self.button7 = QPushButton("Beispiel 7: File Speichern")
        self.button8 = QPushButton("Beispiel 8: Mehrere Files öffnen")
        self.button9 = QPushButton("Beispiel 9: Integer eingeben")
        self.button10 = QPushButton("Beispiel 10")
        self.button11 = QPushButton("Beispiel 11")
        self.button12 = QPushButton("Beispiel 12")




        ## Layout füllen
        layout.addRow(self.button1)
        layout.addRow(self.button2)
        layout.addRow(self.button3)
        layout.addRow(self.button4)
        layout.addRow(self.button5)
        layout.addRow(self.button6)
        layout.addRow(self.button7)
        layout.addRow(self.button8)
        layout.addRow(self.button9)
        layout.addRow(self.button10)
        layout.addRow(self.button11)
        layout.addRow(self.button12)



        ## Fenster anzeigen
        self.show()


    def createConnects(self):
        self.button1.clicked.connect(self.beispiel1)
        self.button2.clicked.connect(self.beispiel2)
        self.button3.clicked.connect(self.beispiel3)
        self.button4.clicked.connect(self.beispiel4)
        self.button5.clicked.connect(self.beispiel5)
        self.button6.clicked.connect(self.beispiel6)
        self.button7.clicked.connect(self.beispiel7)
        self.button8.clicked.connect(self.beispiel8)
        self.button9.clicked.connect(self.beispiel9)
        self.button10.clicked.connect(self.beispiel10)
        self.button11.clicked.connect(self.beispiel11)
        self.button12.clicked.connect(self.beispiel12)



    def beispiel1(self):
        QMessageBox.information(self, "Titel", "Hier ist eine Information")
    
    def beispiel2(self):
        QMessageBox.about(self, "Titel", "Hier ist der Text")
    
    def beispiel3(self):
        QMessageBox.warning(self, "Titel", "Vorsicht Speicher fast voll")

    def beispiel4(self):
        QMessageBox.critical(self, "Titel", "Speicher Voll, Datei kann nicht gespeichert werden!")

    def beispiel5(self):
        antwort = QMessageBox.question(self, "Titel", "Ist Pytho eine Gute Programmiersprache?") #,QmessageBox.cancel
        if antwort == QMessageBox.Yes:
            QMessageBox.information(self, "Danke", "Danke für die Antwort")
        if antwort == QMessageBox.No:
            QMessageBox.critical(self, "Schade", "Dann wirds halt beendet")
    

    #--------------------------------------------------------------------------------------
    def beispiel6(self):
        filename, typ = QFileDialog.getOpenFileName(self,
                                                    "Datei öffnen",
                                                    "",  
                                                    "Alle (*.*);;Python (*.py);; (*.txt)") 
    
    # ozput sihe code auf moodle
    
    def beispiel7(self):
        QFileDialog.getSaveFileName(self, 
                                    "Datei speichern", 
                                    "",                 #er könnte Standardpfad angegeben werden, so aktueller Ordner
                                    "Alle(*.*)")
    
    
    
    
    
    
    def beispiel8(self):
        filenamen = QFileDialog.getOpenFileNames(self, 
                                    "Datei äffnen", 
                                    "",
                                    "Alle(*.*)")
        print(filenamen)

    
    def beispiel9(self):
        wert, ok = QInputDialog.getInt(self, "Datei öffnen", "Was gibt 2 + 2 ?")
        print (wert)
        print (ok)
    
    def beispiel10(self):
        filename, typ = QFileDialog.getOpenFileName(self, "Datei öffnen", "", "Python (*.py):; (*.txt)")
    
    def beispiel11(self):
        filename, typ = QFileDialog.getOpenFileName(self, "Datei öffnen", "", "Python (*.py):; (*.txt)") 

    def beispiel12(self):
        filename, typ = QFileDialog.getOpenFileName(self, "Datei öffnen", "", "Python (*.py):; (*.txt)") 




def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()