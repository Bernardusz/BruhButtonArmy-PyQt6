from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QVBoxLayout, QGridLayout, 
                             QPushButton, QStackedWidget, QHBoxLayout, 
                             QLineEdit, QButtonGroup, QRadioButton,
                             QTextEdit)
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import (QSize, Qt, pyqtSignal, QDateTime,
                          QObject, QTimer)

import sys
import random
class BruhSpawner(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        

    def init_ui(self):
        self.setWindowTitle("BruhSpawner.exe")
        self.setGeometry(350, 350, 700, 700)
        self.setFixedSize(700, 700)
        self.ui_buider()

    def ui_buider(self):
        MainPage = BruhWidget()
        self.setCentralWidget(MainPage)


class BruhWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.UI_Builder()
        self.buttons = []
        self.counter = 0
        self.start_spamming()
        self.start_checker()
    def UI_Builder(self):
        self.central_widget = QWidget(self)

        self.label = QLabel("Are you getting crazy over projects ?", self)
        self.spawner = QPushButton("SPAWN BRUH !", self)

        self.label.setGeometry(160, 150, 400, 250)
        self.spawner.setGeometry(200, 350, 300, 200)

        self.label.setStyleSheet("font-weight: bold;")
        self.label.setFont(QFont("Arial", 15))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.spawner.setStyleSheet("font-weight: bold;")
        self.spawner.setFont(QFont("Arial", 15))
        
        self.spawner.clicked.connect(self.new_BRUH)

    def new_BRUH(self):
        self.button = QPushButton("BRUH!", self)
        self.button.setGeometry(self.randomizer(0, 700), self.randomizer(0, 700), 200, 100)
        self.button.clicked.connect(self.remove_BRUH)
        self.button.show()
        self.buttons.append(self.button)
        print("NEW BRUH !")

    def remove_BRUH(self):
        senderButton = self.sender()
        senderButton.deleteLater()
        self.counter += 1
        print("A BRUH HAS FALLEN")

    def randomizer(self, where, to):
        return random.randint(where, to)
    
    def start_spamming(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.new_BRUH)
        self.timer.start(1000)
        
    def start_checker(self):
        self.check_timer = QTimer(self)
        self.check_timer.timeout.connect(self.check_bruh_master)
        self.check_timer.start(100)

    def check_bruh_master(self):
        if self.counter >= 10:
            self.King_bruh()
            print("🔥-YOU ARE NOW BRUH MASTER 👑-🔥")
            self.stop_spamming()

    def King_bruh(self):
        self.KingBruh = QLabel("🔥-YOU ARE NOW BRUH MASTER 👑-🔥" , self)
        self.KingBruh.setGeometry(230, 480, 350, 90)
        self.KingBruh.setFont(QFont("Arial", 10))
        self.KingBruh.setStyleSheet("font-weight: bold;")
        self.KingBruh.show()

    def stop_spamming(self):
        self.timer.stop()
        self.check_timer.stop()
def main():
    app = QApplication(sys.argv)
    window = BruhSpawner()
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()