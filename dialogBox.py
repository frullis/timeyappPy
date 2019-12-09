from PySide2.QtWidgets import QMessageBox
class DialogBox:


    def MsgBox(self,text, title):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
        returnValue = msgBox.exec()
        return returnValue

