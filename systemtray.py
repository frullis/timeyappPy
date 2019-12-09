from PySide2.QtGui import  QDesktopServices
from PySide2.QtWidgets import QSystemTrayIcon, QMenu
from PySide2.QtCore import QUrl, QCoreApplication


class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, icon, parent=None):
       QSystemTrayIcon.__init__(self, icon, parent)
       menu = QMenu(parent)
       exitAction = menu.addAction("Exit")
       self.StartWorking = menu.addAction("Start Working")
       #self.StartWorking.setEnabled(False)
       OpenTimer = menu.addAction("Open timer")
       dashboard = menu.addAction("Open Dashboard")
       settings = menu.addAction("Settings")
       self.setContextMenu(menu)
       #QObject.connect(exitAction,SIGNAL('triggered()'), self.exit)
       exitAction.triggered.connect(self.exit)
       dashboard.triggered.connect(self.OpenDashboard)
       settings.triggered.connect(self.OpenSettings)
       self.StartWorking.triggered.connect(self.start)

       

    def exit(self):
      QCoreApplication.exit()

    def start(self):
        if self.StartWorking.text() == "Start Working":
            self.StartWorking.setText("Stop Working")
        else:
            self.StartWorking.setText("Start Working")
        return 0
    def OpenTimer(self):
        return 0
    def OpenDashboard(self):
        url = QUrl("http://www.google.com")
        QDesktopServices.openUrl(url)

        return 0
    def OpenSettings(self):
        print("settings")
        return 0

