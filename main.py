from PySide2.QtCore import QApplication
from timerwindow import TimerWindow
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    lol = LoginWindow()
    lol.button.clicked.connect(run)#self.button.clicked
    ex = TimerWindow()
    trayIcon = SystemTrayIcon(QIcon(Config.icon), ex)
    trayIcon.show()
    sys.exit(app.exec_())

