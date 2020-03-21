from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.carddata = QtWidgets.QPlainTextEdit(Dialog)
        self.carddata.setObjectName("carddata")
        self.verticalLayout.addWidget(self.carddata)
        self.Insert = QtWidgets.QDialogButtonBox(Dialog)
        self.Insert.setOrientation(QtCore.Qt.Horizontal)
        self.Insert.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.Insert.setObjectName("Insert")
        self.verticalLayout.addWidget(self.Insert)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.Insert.accepted.connect(Dialog.accept)
        self.Insert.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Card Details"))
