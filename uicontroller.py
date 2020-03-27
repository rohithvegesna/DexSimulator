import sys
from pump import *
from carddetails import *


class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.cardinsert.clicked.connect(self.disableitems)

    def openDialog(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def disableitems(self):
        self.cardinsert.setEnabled(False)
        self.cardinsert.setStyleSheet("background-color: Silver")
