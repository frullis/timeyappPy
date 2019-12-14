from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Qt, QObject , QCoreApplication
from PySide2.QtWidgets import QMessageBox, QApplication, QPushButton, QDialog, QLabel, QLineEdit, QVBoxLayout
from config import Config
from timerwindow import TimerWindow
from api import API
from _version import __version__
import qtawesome as qta
import logging


class LoginWindow(QDialog):

    api = API()


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
        self.setWindowIcon(QIcon(Config.icon))
        #self.setGeometry(self.left, self.top, self.width, self.height)
 
        logo = QLabel()
        logo.setPixmap(QPixmap('icon.png'))
        logo.setAlignment(Qt.AlignCenter)

        label_version = QLabel("version: "+__version__)
        label_version.setAlignment(Qt.AlignCenter)
        
        self.username = QLineEdit(self)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        fa5_icon = qta.icon('fa5.flag')
        self.button_login = QPushButton(fa5_icon, 'Login')
        self.button_login.clicked.connect(self.handleLogin)
        
        layout = QVBoxLayout(self)
        layout.addWidget(logo)
        layout.addWidget(label_version)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.button_login)
        print("hasdad")
        self.show()

    def handleLogin(self):
        data = self.api.auth(self.username.text(), self.password.text())
        print(data)
        try:
            if data.get('username'):
                logging.info("username and password accepted")
                self.accept()
            elif data.get('error'):
                logging.info("username and password is incorrect")
                QMessageBox.warning(
                    self, 'Error', data['error'])
        except (TypeError, AttributeError):
            logging.error("Unknown error not cover in API() class")
            QMessageBox.warning(self, 'Error', "Unknown error not cover in API() class")


