# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 641)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color:rgb(24, 1, 86)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"background-color:rgb(24, 1, 86)\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(221, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(411, 261))
        self.groupBox_2.setMaximumSize(QtCore.QSize(411, 261))
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"background-color:\"white\";\n"
"border-radius: 5%;\n"
"border: 1px solid black\n"
"\n"
"}\n"
"\n"
"QWidget{\n"
"background-color:white\n"
"}\n"
"")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 50, 351, 151))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"background-color:\"white\";\n"
"border-radius: 5%;\n"
"border:1px solid black\n"
"}\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 20, 47, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.input_email = QtWidgets.QLineEdit(self.groupBox)
        self.input_email.setGeometry(QtCore.QRect(50, 40, 261, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.input_email.setFont(font)
        self.input_email.setStyleSheet("QLineEdit {\n"
"    background-color: #c8c4c4;\n"
"    border-radius:5%;\n"
"}")
        self.input_email.setObjectName("input_email")
        self.input_password = QtWidgets.QLineEdit(self.groupBox)
        self.input_password.setGeometry(QtCore.QRect(50, 100, 261, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.input_password.setFont(font)
        self.input_password.setStyleSheet("QLineEdit {\n"
"    background-color: #c8c4c4;\n"
"    border-radius:5%;\n"
"}")
        self.input_password.setObjectName("input_password")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(170, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.btn_login = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_login.setGeometry(QtCore.QRect(310, 220, 75, 23))
        self.btn_login.setStyleSheet("QPushButton {\n"
"    background-color: #c8c4c4;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    border-radius: 5%\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color:#3f01ff;\n"
"    color:#fff;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#3000e0;\n"
"    color:#fff;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:#2000c0;\n"
"    color:#fff;\n"
"}")
        self.btn_login.setObjectName("btn_login")
        self.link_register = QtWidgets.QLabel(self.groupBox_2)
        self.link_register.setGeometry(QtCore.QRect(190, 220, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.link_register.setFont(font)
        self.link_register.setStyleSheet("QLabel { color:blue }")
        self.link_register.setObjectName("link_register")
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(221, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 22))
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
        self.label.setText(_translate("MainWindow", "Email"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "Login"))
        self.btn_login.setText(_translate("MainWindow", "Masuk"))
        self.link_register.setText(_translate("MainWindow", "Belum punya akun?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
