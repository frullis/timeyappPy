from PySide2.QtWidgets import QApplication, QDialog, QMessageBox
from PySide2.QtGui import QIcon
from timerwindow import TimerWindow
from loginwindow import LoginWindow
from systemtray import SystemTrayIcon
from error import ApiException
from api import API
from config import Config
from _version import __version__
import sys
import os
import qtawesome as qta
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

api = API()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    data = api.whoami(Config.api_token)
    print(data)

    try:
        if data == None:
            raise ApiException('Error could not connect to api')
        if data.get('error'):
            login = LoginWindow()
            trayIcon = SystemTrayIcon(QIcon(Config.icon))
            #Maybe move this inside the SystemTray class, keep the main clean yo
            trayIcon.StartWorking.setEnabled(False)
            trayIcon.dashboard.setEnabled(False)
            trayIcon.settings.setEnabled(False)
            trayIcon.timer.setEnabled(False)
            trayIcon.show()
            #lol.button.clicked.connect(run)#self.button.clicked
            if login.exec_() == QDialog.Accepted:
                ex = TimerWindow()
                trayIcon.ex = ex
                trayIcon.StartWorking.setEnabled(True)
                trayIcon.dashboard.setEnabled(True)
                trayIcon.settings.setEnabled(True)
                trayIcon.timer.setEnabled(True)
                #trayIcon = SystemTrayIcon(QIcon(Config.icon), ex)
                #trayIcon.show()
                sys.exit(app.exec_())
        else:
            #For autologin
            ex = TimerWindow()
            trayIcon = SystemTrayIcon(QIcon(Config.icon), ex)
            ex.systray = trayIcon
            trayIcon.show()
            sys.exit(app.exec_())
    except ApiException as e:
        #No api access

        #database = readDb
        # if datetime.now > api_expire:
        #   sorry old login details. you need to login first..
        # elif database.apitoken
        #   we have database and we have an apitoken
        # its ok we let the user to autologin

        ex = TimerWindow()
        trayIcon = SystemTrayIcon(QIcon(Config.icon), ex) 
        ex.systray = trayIcon
        trayIcon.show()
        sys.exit(app.exec_())
        
        '''
        print(e)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(str(e))
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
        '''

