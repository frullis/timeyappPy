import sys
from PySide2.QtGui import QGuiApplication, QIcon, QDesktopServices
from PySide2.QtCore import Qt, QUrl, QThread, Slot, SIGNAL, QObject , QCoreApplication
from PySide2.QtWidgets import QSystemTrayIcon, QMenu, QMessageBox, QApplication, QWidget, QVBoxLayout, QPushButton, QPlainTextEdit, QLabel, QMainWindow, QListWidget, QListWidgetItem
import random
import requests
import time
import threading
from datetime import datetime
from api import API
from idletime import IdleTime
from dialogBox import DialogBox
from config import Config
from systemtray import SystemTrayIcon
from loginwindow import LoginWindow
import logging

logging.basicConfig(level=logging.DEBUG)

api = API()

class TimerWindow(QWidget):

    elapsed_time = 0
    thread_running=False
    api_token = 'fea20970f5bb1b75c96dfa8985fd15b2a3c0f8a8d3261381d0176a05475781ee88d9f7252511e5e085b99e1cee37efa86f7364b7ed5203bccd2c2fd9b76057fe'
    apa = IdleTime()
    workingthread=None

    def __init__(self):
        super().__init__()
        self.title = 'Timey'
        self.left = 10
        self.top = 10
        self.width = 440
        self.height = 680
        self.initUI()
        self.NetworkSetup()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(Config.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        style = """
            background-color: white;
            border-bottom: 1px solid #fff123;
            """

        self.setStyleSheet(style)
        self.label1 = QLabel('00:00:00', self)
        self.label1.move(20,20)
        self.label1.resize(150,30)
        self.label1.setStyleSheet("""QLabel {
    font: medium Ubuntu;
    font-size: 32px;
    color: #006325;     
} """)
        
        self.button = QPushButton('Start', self)
        self.button.move(150,20)
        self.button.resize(100,48)
        self.button.clicked.connect(self.clickStart)
        self.button.setStyleSheet("""QPushButton {
    background-color: #f06325;
    color: white;
    font-color: white;

    min-width:  70px;
    max-width:  70px;
    min-height: 70px;
    max-height: 70px;

    border-radius: 35px;
    border-width: 1px;
    border-color: #ae32a0;
    border-style: solid;
}
#QPushButton:hover {
#    background-color: #328930;
#}
QPushButton:pressed {
    background-color: black;
    color: black;
    border-width:10px;
}
""")
        
        self.label4 = QLabel('Working: ', self)
        self.label4.resize(150,32)
        self.label4.move(20,95)

        self.label3 = QLabel('None', self)
        self.label4.resize(150,32)
        self.label3.move(150,95)
        
        
        self.test = QListWidget(self)
        self.test.addItem("item4")
        self.test.move(20,200)
        self.test.resize(256,128)
        self.test.itemSelectionChanged.connect(self.selectItem)


        self.tasks = QListWidget(self)
        self.tasks.addItem("No tasks")
        self.tasks.move(20,400)
        #self.test.resize(256,128)

        #m = MessageBox
        #m
        #self.setSource(QUrl('main.qml'))
        self.show()

    def _update_timer(self):
        if self.thread_running == True:
            self.thread_running = False
            return 0
        while True:
            #self.elapsed_time = time.time()
            self.thread_running=True
            ''' this is little weired.. but works for now '''
            if self.apa.thread_exit == True or self.thread_exit == True:
                data = api.activity_current(self.api_token)
                print(data)
                if not data.get('error'):
                    api.activity_stop(self.api_token, data['id'])
                self.button.setText('Start')
                self.workingthread.exit()
                self.thread_running = False
                break
            self.elapsed_time += 1
            self.label1.setText(self._online_time(self.elapsed_time))
            time.sleep(1)
        


    def clickStart(self):
        logging.debug("click start/stop button")
        #self.test.clear()
        data={}

        ''' user click start timer '''
        if self.button.text() == 'Start':
            project_id=None
            task_id=None
            for _x in self.test.selectedItems():
                project_id = _x.data(Qt.UserRole)

            for _x in self.tasks.selectedItems():
                task_id = _x.data(Qt.UserRole)


            if project_id == None:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Please select a project first")
                msgBox.setWindowTitle("Select project")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
                print("Please select one of your project first")
            else:
                data = api.activity_start(self.api_token, project_id, task_id)

            ''' this need to be fix '''
            if data.get('error'):
                errorBox = DialogBox()
                returnValue = errorBox.MsgBox(data.get('error')+"Do you want to stop current activity?", "error")

                if returnValue == QMessageBox.Ok:
                    data = api.activity_current(self.api_token)
                    print(data)
                    api.activity_stop(self.api_token, data['id'])
                    print("Time to do something weired!")

                #print(data.get('error'))
            elif data:
                #apa = IdleTime()
                self.apa.thread_exit = False
                print(self.workingthread)
                self.workingthread = QThread()
                self.workingthread.started.connect(self.apa.thread_handle)
                #self.apa.moveToThread(self.workingthread)
                self.workingthread.start()

                self.thread_exit=False
                t = threading.Thread(target=self._update_timer)
                t.start()
                self.button.setText('Stop')
                self.test.setDisabled(True)
        
        else:

            data = api.activity_current(self.api_token)
            print(data)
            api.activity_stop(self.api_token, data['id'])
            self.thread_exit = True
            self.apa.thread_exit = True
            self.button.setText('Start')
            self.test.setDisabled(False)
        print("end of clickstart")


    def selectItem(self):
        for _x in self.test.selectedItems():
            self.label3.setText(_x.text())
            print(_x.text())
            print(_x.data(Qt.UserRole))
        data = api.task_get(self.api_token, _x.data(Qt.UserRole))
        print(data)
        self.tasks.clear()
        for _x in data:
            item = QListWidgetItem(_x["name"], self.tasks)
            item.setData(Qt.UserRole, _x["task_id"])
        
        print(data)
        #print(self.test.text())

    def NetworkSetup(self):
        self.test.clear()
        data = api.get_projects(self.api_token)
        for _x in data:
            #self.test.addItem(_x["name"])
            item = QListWidgetItem(_x["name"], self.test)
            item.setData(Qt.UserRole, _x["id"])


        item = QListWidgetItem('Text', self.test)
        data = ('foo', 'bar', [1, 2, 3])
        item.setData(Qt.UserRole, data)

        end_date = datetime.utcnow().isoformat()
        start_date = datetime.utcnow().replace(hour=0,minute=0,second=0,microsecond=0).isoformat()
        data = api.get_activity(self.api_token, start_date, end_date)
        for _x in data:
            self.elapsed_time += _x['duration']
        ''' Set timer '''
        self.label1.setText(self._online_time(self.elapsed_time))



    
    def _online_time(self, data):
        hour=0
        minute=0
        second=0
        hour = int(data/60/60)
        data = data - (hour*3600)
        minute = int(data/60)
        data = data - (minute*60)
        second = int(data)



        if hour < 10: 
            hour = "0"+str(hour)
        if minute < 10: 
            minute = "0"+str(minute)
        if second < 10: 
            second = "0"+str(second)

        time_string = str(hour) +":" +str(minute)+":"+str(second)

        return time_string


def run():
    print("from run")
    ex = App()
    trayIcon = SystemTrayIcon(QIcon(Config.icon), ex)
    trayIcon.show()

