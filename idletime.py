from pynput.keyboard import Key, Listener
from PySide2.QtWidgets import QMessageBox, QApplication
from PySide2.QtCore import QObject, QThread, Signal
import time
from dialogBox import DialogBox
from config import Config

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
        #self.elapsed_time = time.time()
        while True:
            if self.thread_exit == True:
                break
            self.elapsed_time = time.time()
            if self.calc_time() > Config.idletime:
                if self.showdialog == True:
                    self.showdialog = False
                    self.run()
                    test = DialogBox()
                    self.elapsed_time = time.time()
                    returnValue = test.MsgBox("You have been idle for "+str(self.calc_time())+" seconds do you want to continue working?", "IdleTime")
                    print(returnValue)
                    if returnValue == QMessageBox.Cancel:
                        print("click!")
                        self.showdialog = True
                        self.thread_exit=True
                        break
                    elif returnValue == QMessageBox.Ok:
                        self.showdialog = True

                self.time_start = time.time()
            QApplication.processEvents()




    def _on_press(self,key):
        #self.elapsed_time = time.time()
        print(self.time_start)
        #diff = self.elapsed_time - self.time_start
        #print("diff: " + str(diff))
        print('{0} pressed'.format(
            key))
        #self.time_start = time.time()

    def _on_release(self,key):
        print('{0} release'.format(
            key))
        #Stop for any keystroke
        if key:
            return False
        if key == Key.esc:
            # Stop listener
            return False



