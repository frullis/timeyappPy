from PySide2.QtGui import QGuiApplication, QIcon, QDesktopServices
from PySide2.QtCore import Qt, QUrl, QThread, Slot, SIGNAL, QObject , QCoreApplication
from PySide2.QtWidgets import QSystemTrayIcon, QMenu, QMessageBox, QApplication, QWidget, QVBoxLayout, QPushButton, QPlainTextEdit, QLabel, QMainWindow, QListWidget, QListWidgetItem
from config import Config

class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Timey'
        self.left = 10
        self.top = 10
        self.width = 440
        self.height = 680
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        #self.setWindowIcon(QIcon(Config.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.button = QPushButton('Start', self)
        self.button.move(150,20)
        self.button.resize(100,48)
        #self.button.clicked.connect(self.clickStart)
        
        self.show()

