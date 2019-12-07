from pynput.keyboard import Key, Listener
from PySide2.QtWidgets import QMessageBox, QApplication
from PySide2.QtCore import QObject, QThread, Signal
import time


class IdleTime(QThread):


    time_start = time.time()
    elapsed_time = 0
    thread_exit = False
    showdialog = True

    def __init__(self, parent = None):
        QThread.__init__(self, parent)

    def run(self):
        with Listener(
            on_press=self._on_press,
            on_release=self._on_release) as listener:
                listener.join()



    def calc_time(self):
        return self.elapsed_time - self.time_start

    def thread_handle(self):
        self.time_start=time.time()
        while True:
            if self.thread_exit == True:
                break
            self.elapsed_time = time.time()
            if self.calc_time() > 5:
                f = open("loggy.txt", "a")
                f.write("yippie key yay mother fucker")
                f.close()
                print("yippie key yay mother fucker")
                self.time_start = time.time()
                #test = Signal("hej")
                #from timey import MessageBox
                #m = MessageBox()
                #self.m.signal_str.connect(parent.showMessage)
                #m.showMessage()
                if self.showdialog == True:
                    self.showdialog = False
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setText("You have been idle for 00:22:55 minutes do you want to continue working?")
                    msgBox.setWindowTitle("Select project")
                    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    returnValue = msgBox.exec()
                    print(returnValue)
                    if returnValue == QMessageBox.Cancel:
                        print("click!")
                        self.showdialog = True
                        self.thread_exit=True
                        break

            QApplication.processEvents()




    def _on_press(self,key):
        self.elapsed_time = time.time()
        print(self.time_start)
        diff = self.elapsed_time - self.time_start
        print("diff: " + str(diff))
        print('{0} pressed'.format(
            key))
        self.time_start = time.time()

    def _on_release(self,key):
        print('{0} release'.format(
            key))
        if key == Key.esc:
            # Stop listener
            return False



