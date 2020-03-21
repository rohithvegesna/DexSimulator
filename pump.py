from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(666, 917)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_11.addWidget(self.label)
        self.gallons = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.gallons.setFont(font)
        self.gallons.setObjectName("gallons")
        self.verticalLayout_11.addWidget(self.gallons)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_11.addWidget(self.label_2)
        self.dollars = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.dollars.setFont(font)
        self.dollars.setObjectName("dollars")
        self.verticalLayout_11.addWidget(self.dollars)
        self.verticalLayout.addLayout(self.verticalLayout_11)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout_3.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_18.setText("")
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout_3.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy)
        self.pushButton_19.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_19.setText("")
        self.pushButton_19.setObjectName("pushButton_19")
        self.verticalLayout_3.addWidget(self.pushButton_19)
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)
        self.pushButton_20.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_20.setText("")
        self.pushButton_20.setObjectName("pushButton_20")
        self.verticalLayout_3.addWidget(self.pushButton_20)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.screen = QtWidgets.QTextBrowser(self.centralwidget)
        self.screen.setMinimumSize(QtCore.QSize(288, 288))
        self.screen.setMaximumSize(QtCore.QSize(288, 288))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.screen.setFont(font)
        self.screen.setObjectName("screen")
        self.horizontalLayout_5.addWidget(self.screen)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        self.pushButton_21.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_21.setText("")
        self.pushButton_21.setObjectName("pushButton_21")
        self.verticalLayout_4.addWidget(self.pushButton_21)
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.pushButton_22.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_22.setText("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.verticalLayout_4.addWidget(self.pushButton_22)
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        self.pushButton_23.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_23.setText("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.verticalLayout_4.addWidget(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy)
        self.pushButton_24.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_24.setText("")
        self.pushButton_24.setObjectName("pushButton_24")
        self.verticalLayout_4.addWidget(self.pushButton_24)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cardinsert = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cardinsert.sizePolicy().hasHeightForWidth())
        self.cardinsert.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.cardinsert.setFont(font)
        self.cardinsert.setStyleSheet("background-color: rgb(200, 209, 197);")
        self.cardinsert.setObjectName("cardinsert")
        self.verticalLayout_2.addWidget(self.cardinsert)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(200, 209, 197);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_3.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_3.addWidget(self.pushButton_12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_4.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_4.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_4.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet(
            "background-color: rgb(200, 209, 197);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_4.addWidget(self.pushButton_16)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gradescreen_1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.gradescreen_1.setMinimumSize(QtCore.QSize(100, 75))
        self.gradescreen_1.setMaximumSize(QtCore.QSize(1000, 75))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.gradescreen_1.setFont(font)
        self.gradescreen_1.setObjectName("gradescreen_1")
        self.verticalLayout_5.addWidget(self.gradescreen_1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_5.addWidget(self.checkBox_7)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gradescreen_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.gradescreen_2.setMinimumSize(QtCore.QSize(100, 75))
        self.gradescreen_2.setMaximumSize(QtCore.QSize(1000, 75))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.gradescreen_2.setFont(font)
        self.gradescreen_2.setObjectName("gradescreen_2")
        self.verticalLayout_6.addWidget(self.gradescreen_2)
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_6.addWidget(self.checkBox_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gradescreen_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.gradescreen_3.setMinimumSize(QtCore.QSize(100, 75))
        self.gradescreen_3.setMaximumSize(QtCore.QSize(1000, 75))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.gradescreen_3.setFont(font)
        self.gradescreen_3.setObjectName("gradescreen_3")
        self.verticalLayout_7.addWidget(self.gradescreen_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_7.addWidget(self.checkBox_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gradescreen_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.gradescreen_4.setMinimumSize(QtCore.QSize(100, 75))
        self.gradescreen_4.setMaximumSize(QtCore.QSize(1000, 75))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.gradescreen_4.setFont(font)
        self.gradescreen_4.setObjectName("gradescreen_4")
        self.verticalLayout_8.addWidget(self.gradescreen_4)
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_8.addWidget(self.checkBox_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gradescreen_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.gradescreen_5.setMinimumSize(QtCore.QSize(100, 75))
        self.gradescreen_5.setMaximumSize(QtCore.QSize(1000, 75))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.gradescreen_5.setFont(font)
        self.gradescreen_5.setObjectName("gradescreen_5")
        self.verticalLayout_9.addWidget(self.gradescreen_5)
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_9.addWidget(self.checkBox_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gradescreen_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.gradescreen_6.setMinimumSize(QtCore.QSize(100, 75))
        self.gradescreen_6.setMaximumSize(QtCore.QSize(1000, 75))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.gradescreen_6.setFont(font)
        self.gradescreen_6.setObjectName("gradescreen_6")
        self.verticalLayout_10.addWidget(self.gradescreen_6)
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_10.addWidget(self.checkBox_6)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "7-11 DexSimulator"))
        self.label.setText(_translate("MainWindow", "DOLLARS"))
        self.label_2.setText(_translate("MainWindow", "GALLONS"))
        self.cardinsert.setText(_translate("MainWindow", "CARD INSERT"))
        self.pushButton.setText(_translate("MainWindow", "QZ\n"
                                           "1"))
        self.pushButton_2.setText(_translate("MainWindow", "ABC\n"
                                             "2"))
        self.pushButton_3.setText(_translate("MainWindow", "DEF\n"
                                             "3"))
        self.pushButton_4.setText(_translate("MainWindow", "YES\n"
                                             "RECEIPT"))
        self.pushButton_5.setText(_translate("MainWindow", "GHI\n"
                                             "4"))
        self.pushButton_6.setText(_translate("MainWindow", "JKL\n"
                                             "4"))
        self.pushButton_7.setText(_translate("MainWindow", "MNO\n"
                                             "5"))
        self.pushButton_8.setText(_translate("MainWindow", "NO"))
        self.pushButton_9.setText(_translate("MainWindow", "PRS\n"
                                             "7"))
        self.pushButton_10.setText(_translate("MainWindow", "TUV\n"
                                              "8"))
        self.pushButton_11.setText(_translate("MainWindow", "WXY\n"
                                              "9"))
        self.pushButton_12.setText(_translate("MainWindow", "CANCEL"))
        self.pushButton_13.setText(_translate("MainWindow", "CLEAR"))
        self.pushButton_14.setText(_translate("MainWindow", "0"))
        self.pushButton_15.setText(_translate("MainWindow", "ENTER\n"
                                              "OK"))
        self.pushButton_16.setText(_translate("MainWindow", "HELP"))
        self.checkBox_7.setText(_translate("MainWindow", "GRADE 1"))
        self.checkBox_5.setText(_translate("MainWindow", "GRADE 2"))
        self.checkBox_2.setText(_translate("MainWindow", "GRADE 3"))
        self.checkBox_3.setText(_translate("MainWindow", "GRADE 4"))
        self.checkBox_4.setText(_translate("MainWindow", "GRADE 5"))
        self.checkBox_6.setText(_translate("MainWindow", "GRADE 6"))
        self.checkBox.setText(_translate("MainWindow", "Nozzle"))
