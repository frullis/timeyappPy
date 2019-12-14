from PySide2.QtGui import  QDesktopServices
from PySide2.QtWidgets import QSystemTrayIcon, QMenu
from PySide2.QtCore import QUrl, QCoreApplication
#from main import App

class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, icon, ex=None, parent=None):
       QSystemTrayIcon.__init__(self, icon, parent)
       self.ex = ex
       menu = QMenu(parent)
       self.StartWorking = menu.addAction("Start Working")
       #self.StartWorking.setEnabled(False)
       self.timer = menu.addAction("Open timer")
       self.dashboard = menu.addAction("Open Dashboard")
       self.editaddtime = menu.addAction("Edit/Add time")
       self.settings = menu.addAction("Settings")
       exitAction = menu.addAction("Quit")
       self.setContextMenu(menu)
       #QObject.connect(exitAction,SIGNAL('triggered()'), self.exit)
       exitAction.triggered.connect(self.exit)
       self.dashboard.triggered.connect(self.OpenDashboard)
       self.timer.triggered.connect(self.OpenTimer)
       self.settings.triggered.connect(self.OpenSettings)
       self.StartWorking.triggered.connect(self.start)


       

    def exit(self):
      QCoreApplication.exit()

    def start(self):
        if self.StartWorking.text() == "Start Working":
            if self.ex.clickStart() == 0:
                pass
            else:
                self.StartWorking.setText("Stop Working")
            #self.ex.button.setText("Stop")
            #self.ex.clickStart()
        else:
            self.ex.clickStart()
            #self.ex.button.setText("Start")
            self.StartWorking.setText("Start Working")
        return 0
    def OpenTimer(self):
        self.ex.activateWindow()
        #self.ex.showNormal()
        return 0

    def OpenEditAddTime(self):
        url = QUrl("http://www.google.com")
        QDesktopServices.openUrl(url)
    def OpenDashboard(self):
        url = QUrl("http://www.google.com")
        QDesktopServices.openUrl(url)

        return 0
    def OpenSettings(self):
        print("settings")
        return 0

