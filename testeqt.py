import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 803)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.DevicesButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DevicesButton.sizePolicy().hasHeightForWidth())
        self.DevicesButton.setSizePolicy(sizePolicy)
        self.DevicesButton.setStyleSheet("border-color: rgba(255, 255, 255, 0);\n"
                                         "")
        self.DevicesButton.setText("")
        icon = QtGui.QIcon()

#        icon.addPixmap(QtGui.QPixmap("../../Images/png/Group 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("E:/_Qt/img/cat.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.DevicesButton.setIcon(icon)
        self.DevicesButton.setIconSize(QtCore.QSize(45, 45))       # (220, 45)
        self.DevicesButton.setObjectName("DevicesButton")

# ---
#        self.DevicesButton.clicked.connect(self.stackedWidget.setCurrentIndex(0))  # ---

        self.horizontalLayout.addWidget(self.DevicesButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.OptionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.OptionsButton.setText("")
        icon1 = QtGui.QIcon()

#        icon1.addPixmap(QtGui.QPixmap("../../Images/png/Services_45px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("E:/_Qt/img/qt-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.OptionsButton.setIcon(icon1)
        self.OptionsButton.setIconSize(QtCore.QSize(45, 45))
        self.OptionsButton.setObjectName("OptionsButton")
        self.horizontalLayout.addWidget(self.OptionsButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")

        self.DevicesTab = QtWidgets.QWidget()
        self.DevicesTab.setObjectName("DevicesTab")

        self.label = QtWidgets.QLabel(self.DevicesTab)
        self.label.setGeometry(QtCore.QRect(390, 220, 47, 13))
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.DevicesTab)

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton = QtWidgets.QPushButton(self.page_2)
        self.pushButton.setGeometry(QtCore.QRect(360, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page_2)

# +++
        self.DevicesButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0)) # +++
        self.OptionsButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1)) # +++

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "WELCOME"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
